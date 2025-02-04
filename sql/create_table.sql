CREATE TABLE wildfires (
    id SERIAL PRIMARY KEY,
    fire_year INT,
    discovery_date DATE,
    discovery_doy INT,
    nwcg_cause_classification VARCHAR(255),
    nwcg_general_cause VARCHAR(255),
    cont_date DATE,
    cont_doy INT,
    fire_size FLOAT,
    fire_size_class VARCHAR(50),
    owner_descr VARCHAR(255),
    month INT,
    season VARCHAR(50)
);
