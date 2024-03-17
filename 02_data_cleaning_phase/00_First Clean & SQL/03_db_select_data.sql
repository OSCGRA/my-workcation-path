USE workcation_db;

SELECT ca.name, ca.address, ca.rating, ca.website,ca.schedule, ca.latitude, ca.longitude, ca.city
FROM workcation_db.campsites AS ca
WHERE ca.name IN (SELECT DISTINCT name FROM workcation_db.campsites);

SELECT co.name, co.address, co.rating, co.website, co.schedule, co.latitude, co.longitude, co.city
FROM workcation_db.coworkings AS co
WHERE co.name IN (SELECT DISTINCT name FROM workcation_db.coworkings);

SELECT epa.location, epa.site_type, epa.comments, epa.latitude, epa.longitude, epa.town
FROM example_path AS epa
WHERE epa.country IN ('France', 'Spain', 'Italy', 'Portugal');

SELECT  ca.name, ca.city, 'camp' as type
FROM workcation_db.campsites AS ca
UNION
SELECT co.name, co.city, 'cowork' as type
FROM workcation_db.coworkings AS co;

