database_creation_query = """
CREATE DATABASE smooth_database;
"""

show_databases_query = """
SHOW DATABASES;
"""

enter_database_query = """
USE smooth_database;
"""

show_current_database_query = """
SELECT DATABASE();
"""

landlord_query = """
CREATE TABLE landlords (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    zip_code VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    street_number INT,
    building_number INT,
    apartment_number INT,
    floor INT,
    other_specification VARCHAR(255),
    phone_number VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    average_ratings FLOAT(2)
);
"""

apartments_query = """
CREATE TABLE apartments (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    landlord_id INT,
    apartment_name VARCHAR(255),
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    zip_code VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    street_number INT,
    building_number INT,
    apartment_number INT,
    floor INT,
    other_specification VARCHAR(255),
    surface INT,
    exposition VARCHAR(255),
    year_of_construction INT,
    shared_flat BOOLEAN,
    number_of_rooms INT,
    average_ratings FLOAT(2)
);
"""

tenants_query = """
CREATE TABLE tenants (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    zip_code VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    street_number INT,
    building_number INT,
    apartment_number INT,
    floor INT,
    other_specification VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255),
    marital_status VARCHAR(255),
    monthly_income FLOAT(2),
    employment_situation VARCHAR(255),
    occupation VARCHAR(255),
    average_ratings FLOAT(2)
);
"""

apartments_reviews_query = """
CREATE TABLE apartments_reviews (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    overall_review TINYINT(1) NOT NULL CHECK (overall_review >=0 AND overall_review <=5),
    overall_location TINYINT(1) NOT NULL CHECK (overall_location >=0 AND overall_location <=5),
    general_condition TINYINT(1) NOT NULL CHECK (general_condition >=0 AND general_condition <=5),
    building_condition TINYINT(1) NOT NULL CHECK (building_condition >=0 AND building_condition <=5),
    lighting TINYINT(1) NOT NULL CHECK (lighting >=0 AND lighting <=5),
    noise TINYINT(1) NOT NULL CHECK (noise >=0 AND noise <=5),
    energy_performance TINYINT(1) NOT NULL CHECK (energy_performance >=0 AND energy_performance <=5),
    neighbourhood_safety TINYINT(1) NOT NULL CHECK (neighbourhood_safety >=0 AND neighbourhood_safety <=5),
    neighbourhood_services TINYINT(1) NOT NULL CHECK (neighbourhood_services >=0 AND neighbourhood_services <=5),
    transports_proximity TINYINT(1) NOT NULL CHECK (transports_proximity >=0 AND transports_proximity <=5),
    occupancy_duration INT NOT NULL,
    comment TEXT
);
"""

landlord_reviews_query = """
CREATE TABLE landlord_reviews (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    overall_review TINYINT(1) NOT NULL CHECK (overall_review >=0 AND overall_review <=5),
    reactivity_to_issues TINYINT(1) NOT NULL CHECK (reactivity_to_issues >=0 AND reactivity_to_issues <=5),
    communication TINYINT(1) NOT NULL CHECK (communication >=0 AND communication <=5),
    comment TEXT
);
"""

tenants_reviews_query = """
CREATE TABLE tenants_reviews (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    care_for_the_property TINYINT(1) NOT NULL CHECK (care_for_the_property >=0 AND care_for_the_property <=5),
    respect_for_neighbors TINYINT(1) NOT NULL CHECK (respect_for_neighbors >=0 AND respect_for_neighbors <=5),
    communication TINYINT(1) NOT NULL CHECK (communication >=0 AND communication <=5),
    payments_punctuality TINYINT(1) NOT NULL CHECK (payments_punctuality >=0 AND payments_punctuality <=5),
    comment TEXT
);
"""

landlords_data_insertion_query = """
INSERT INTO landlords (first_name, last_name, date_of_birth, country, city, zip_code, street, street_number, building_number, apartment_number, floor, other_specification, phone_number, email, average_ratings)
VALUES ('John', 'Doe', '1980-01-01', 'United States', 'New York', '10001', 'Broadway', 1, 1, 1, 1, '', '555-555-5555', 'johndoe@example.com', 4.5);
"""

apartments_data_insertion_query = """
INSERT INTO apartments (landlord_id, apartment_name, country, city, zip_code, street, street_number, building_number, apartment_number, floor, other_specification, surface, exposition, year_of_construction, shared_flat, number_of_rooms, average_ratings)
VALUES (FLOOR(RAND()*100), 'The Place', 'United States', 'New York', '10001', 'Fifth Ave', FLOOR(RAND()*100), FLOOR(RAND()*100), FLOOR(RAND()*100), FLOOR(RAND()*10), '', FLOOR(RAND()*200), 'West', FLOOR(RAND()*100+1900), FLOOR(RAND()*1), FLOOR(RAND()*10), RAND()*5);
"""

tenants_data_insertion_query = """
INSERT INTO tenants (first_name, last_name, date_of_birth, country, city, zip_code, street, street_number, building_number, apartment_number, floor, other_specification, phone_number, email, marital_status, monthly_income, employment_situation, occupation, average_ratings)
VALUES ("John", "Smith", "1998-05-20", "USA", "New York", "10001", "Fifth Avenue", "1", "1", "1", "1", "None", "555-555-5555", "john.smith@email.com", "Single", "5000", "Employed", "Software Engineer", "4.5");
"""

apartments_reviews_data_insertion_query = """
INSERT INTO apartments_reviews (overall_review, overall_location, general_condition, building_condition, lighting, noise, energy_performance, neighbourhood_safety, neighbourhood_services, transports_proximity, occupancy_duration, comment)
VALUES (ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*12), "This place was lit");
"""

landlords_reviews_data_insertion_query = """
INSERT INTO landlord_reviews (overall_review, reactivity_to_issues, communication, comment)
VALUES (ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), "That guy was not very nice. He kept asking me for money");
"""

tenants_reviews_data_insertion_query = """
INSERT INTO tenants_reviews (care_for_the_property, respect_for_neighbors, communication, payments_punctuality, comment)
VALUES (ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), "That tenant was a human with lots of fingers");
"""
