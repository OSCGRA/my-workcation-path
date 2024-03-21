import pandas as pd
import numpy as np
import os
import sys
import streamlit as st
import base64

from geopy.distance import great_circle
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score

# Find Nearby

def find_nearby_coworks(campsite, coworks, max_distance_km):
    nearby_coworks = []
    for _, cowork in coworks.iterrows():
        dist = great_circle((campsite.latitude, campsite.longitude), (cowork.latitude, cowork.longitude)).kilometers
        if dist <= max_distance_km:
            nearby_coworks.append(cowork)
    return nearby_coworks

# Load the data
df_campsites = pd.read_csv("campsites_encoding.csv")
df_coworks = pd.read_csv("coworkings_encoding.csv")

# Reverse dictionaries for decoding
type = {0: 'City', 1: 'Town', 2: 'Village'}
luxury = {0: 'Campsite', 1: 'Glamping', 2: 'Camper'}
beach = {0: 'No', 1: 'Yes'}
wild = {0: 'No', 1: 'Yes'}


# Prepare data for model training
Xca = df_campsites

# Initialize and fit DBSCAN for campsites with results EPS: 30, Min_Samples: 9


dbscan_optimal_campsites = DBSCAN(eps=30, min_samples=9, metric='euclidean').fit(Xca)

# Assign cluster labels
df_campsites['cluster'] = dbscan_optimal_campsites.labels_


# Streamlit app

def main():
    # add background image
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
            unsafe_allow_html=True
        )
        
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "landscape_back.jpeg")
    add_bg_from_local('image_path')

    # Custom CSS styles for title and click effect
    custom_css = """
    <style>
    /* Set title color to pink */
    .title-wrapper {
        color: pink;
    }

    /* Set click effect color to light green */
    .css-1g8ra89:hover {
        background-color: lightgreen !important;
        color: black !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    new_title = '<p style= color:Grey; font-size: 280px;"> Project by Nara Guerra 👽</p>'
    st.markdown(new_title, unsafe_allow_html=True)


    st.title("Find the :pink[best places] with this personalised browser")

    st.markdown("Enter your preferences to get the site category you can't missed in Spain and top places to visit.")

    # User input form
    with st.form(key='site_recommender_form'):
        user_sentiment_input = st.selectbox("Select your mood for this travel:", [""] + list(sentiment_decoded.values()))
        user_age_input = st.selectbox("Select your age group:", [""] + list(user_age_decoded.values()))
        user_way_input = st.selectbox("Select your way of travel:", [""] + list(user_way_decoded.values()))
        user_destination_input = st.selectbox("Select your destination in Spain:", [""] + list(destination_decoded.values()))
        user_rating_input = st.slider("Rate for this experience (1-5):", 1, 5, 3)
        submit_button = st.form_submit_button(label='Get Recommendations')

    # Perform predictions and show the results when the form is submitted
    if submit_button:
        # Convert user inputs to encoded values
        user_age_encoded = list(user_age_decoded.keys())[list(user_age_decoded.values()).index(user_age_input)]
        user_way_encoded = list(user_way_decoded.keys())[list(user_way_decoded.values()).index(user_way_input)]
        user_sentiment_encoded = list(sentiment_decoded.keys())[list(sentiment_decoded.values()).index(user_sentiment_input)]
        user_destination_encoded = list(destination_decoded.keys())[list(destination_decoded.values()).index(user_destination_input)]

        # Make the prediction using the model
        user_category_encoded = rf_content.predict([[user_age_encoded, user_way_encoded, user_sentiment_encoded, user_destination_encoded, user_rating_input]])[0]
        user_category = cat_sites_decoded[user_category_encoded]

        # Display results at the bottom of the page
        st.markdown("## Results")
        st.write("#### Category more adequate to you:", user_category)

        # Get top three sites to visit
        top_sites_names = get_top_three_sites_by_category(df, user_category_encoded, user_destination_encoded)
        st.markdown("## Places you shouldn't miss:")
        for idx, site_name in enumerate(top_sites_names):
            st.write(f"{idx+1}. {site_name}")

        # Display sites on a map
        st.subheader("Map of these sites")
        map_data = df[df['name'].isin(top_sites_names)][['latitud', 'longitud', 'name']]
        map_data.rename(columns={'latitud': 'LAT', 'longitud': 'LON'}, inplace=True)
        st.map(map_data)

def get_top_three_sites_by_category(df, user_category_encoded, user_destination_encoded):
    # Filter sites of this category and destination
    category_sites = df[(df['cat_sites_reduced_encoded'] == user_category_encoded) & (df['destination_encoded'] == user_destination_encoded)]

    # Sort the sites by the column "rating" in descending order
    sorted_sites = category_sites.sort_values(by='rating', ascending=False)

    # Take the top three sites with the highest ratings and get only the "name" column
    top_three_sites = sorted_sites.head(3)['name']

    return top_three_sites.tolist()

if __name__ == "__main__":
    main()
