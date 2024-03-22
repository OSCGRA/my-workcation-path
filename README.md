<!-- PROJECT LOGO -->
<br />
<div align="center">

  <a href="https://github.com/OSCGRA/my-jobcation-path">
    <img src="https://raw.githubusercontent.com/OSCGRA/my-jobcation-path/master/00_images/logo.png" alt="Logo">
  </a>

<h3 align="center">MY JOBCATION PATH</h3>

  <p align="center">
    In a world where vacations and work sometimes merge.
    <br />
    <a href="https://github.com/OSCGRA/my-jobcation-path"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://myjobcationpath.streamlit.app/">View Demo</a>

  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#setup">Setup</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installations</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#eda">EDA: A Path model to Encoding</a></li>
    <li><a href="#model">Model</a></li>
    <li><a href="#recomender">Recomender</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<br />

During the summer of 2023 I left the screens and meetings to embark on a different professional experience: managing the opening of one of the glampings of an important company in Portugal. 
An incredible experience! 
People from all places, backgrounds and ages came to "my space". For everyone, I had some advice to give them to help them in their stay with us, families, couples, groups of friends... 
However, there was one question that always had a "half-answer": 

- I need to work. Where is there a good internet connection here?
- There isn't, try a café into the village.

<strong>Business Idea:</strong>


In our ever more interconnected world, the lines between work and leisure are becoming increasingly blurred, particularly noticeable in remote work settings. Occasionally, we face challenges in locating suitable workspaces while travelling to different places. To streamline travel arrangements for working individuals, the concept of this app emerged—an application designed to suggest accommodations in natural settings, considering the proximity of coworking spaces.

<strong>Project Objective:</strong>

Our overarching goal is to create an interactive app where we can select certain parameters of the travel experience we want: proximity to an urban centre, proximity to a beach, rating, or some remote place.
Depending on these parameters and the maximum distance we would like to travel to find a workspace, the app will give us different options in the form of related campgrounds and co-workings. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SETUP -->
## Setup

This section should list any major frameworks/libraries used to bootstrap this project.

* Python installed on your system (Python 3.10.1 recommended).
  
* Required Python libraries installed:
  
    - **Pandas:** [v1.3.3](https://pandas.pydata.org/)  
    - **NumPy:** [v1.21.4](https://numpy.org/)  
    - **Matplotlib:** [v3.4.3](https://matplotlib.org/)  
    - **Os:** [Latest Version](https://docs.python.org/3/library/os.html)
    - **Sys:** [Latest Version](https://docs.python.org/3/library/sys.html)
    - **WordCloud:** [Latest Version](https://github.com/amueller/word_cloud)
    - **GoogleMaps:** [Latest Version](https://github.com/googlemaps/google-maps-services-python)
    - **GeoPandas:** [v0.10.2](https://geopandas.org/)
    - **Geopy:** [Latest Version](https://geopy.readthedocs.io/en/latest/)
    - **Scikit-Learn:** [Latest Version](https://scikit-learn.org/stable/)
    - **Streamlit:** [Latest Version](https://www.streamlit.io/)
    - **Base64:** [Latest Version](https://docs.python.org/3/library/base64.html)
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

  ```sh
    pip install -U googlemaps
    pip install geopandas
    pip install geopy
  ```
or:
  ```sh
    conda install -U googlemaps
    conda install -U geopandas
    conda install -U googlemaps
  ```

### Installation

1. Clone the repo
   
   ```sh
    git clone https://github.com/OSCGRA/my-jobcation-path.git
   ```

3. API Configuration:
   
      Create a _.py_ file like this:

   ![api_key](https://github.com/OSCGRA/my-jobcation-path/assets/77927558/72f11821-8711-4e47-b552-40364d34c0e3)


      Into these folders:
   
       -  my-jobcation-path/01_data_mining_phase/scrapper_app/
       -  my-jobcation-path/02_data_cleaning_phase/01_Preprocessing&Clean/

      Open it and write:

      ```sh
      api_key = GOOGLE_MAPS_API_KEY

      ```

      Example to call it:

     ```sh
      from api_key import GOOGLE_MAPS_API_KEY

     ```

     ```sh
      API_KEY = GOOGLE_MAPS_API_KEY

     ```
     
     ```sh
      gmaps = googlemaps.Client(key=API_KEY)

     ```
    _(IMPORTANT: This step is optional, you can use the .csv provided. You will need it if you want to restart the data provided, retrieving new data from Google Maps.)_

2. Install packages:

    You can open each notebook in each folder and look for other installations and repeat point 1 with them, or do it directly in the corresponding notebook.
  
   
3. Follow the **Roadmap** section in this README.
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

This section is under construction, thanks for your understanding.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- EDA: A Path model to Encoding -->
## EDA: A Path model to Encoding

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MODEL -->
## MODEL

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

This section is under construction, thanks for your understanding.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- RECOMMENDER -->
## RECOMMENDER

This section is under construction, thanks for your understanding.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a href="mailto:oscarmanuel.re@gmail.com">
  
<!-- CONTACT -->
## Contact

Feel free to reach out to me via email, LinkedIn, or Reddit for any inquiries, contributions to projects, or potential job opportunities:

- **Email:** [oscarmanuel.re@gmail.com](mailto:oscarmanuel.re@gmail.com)
- **LinkedIn:** [Oscar Reinoso Estevez](https://www.linkedin.com/in/oscar-reinoso-estevez/)
- **Reddit:** [u/posore01](https://www.reddit.com/user/posore01)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* To Ainara Guerra for her [project](https://github.com/ainaraguerraf/final-project-ironhack-data), an inspiration for a "crazy" idea.
* To [Isi](https://github.com/isi-mube), my lead teacher data at Ironhack for all the knowledge provided.
* To Xisca for the SQL masterclass.
* To my dog "Loja" who patiently waited every day longer than necessary to go for a walk.
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
