# ETL Pipeline in Docker

## Project overview
Building ETL Pipeline with Docker. Extracting data from California Wildfires dataset from Kaggle, cleaning and transforming it and loading into a PostgreSQL database.

This project contains the following files:
- ``src/extract.py`` - a python script with instructions on extracting data from a dataframe<br>
- ``src/transform.py`` - a python script that contains instructions on querying, cleaning and transforming data<br>
- ``src/load.py`` - a python script with instructions on loading data in the postgreSQL database<br>
- ``main.py`` - a python script that executes all the steps to extract, transform, and load the transformed data using the functions from extract.py, transform.py, and load_data_to_s3.py<br>
- ``sql/create_table.sql`` - sql script for creating a table for postgres database
- ``requirements.txt`` - a text document that contains all the libraries required to execute the code<br>
- ``Dockerfile`` - a text document that contains all the instructions a user could call on the command line to assemble an image<br>
- ``.gitignore`` - a text document that specifies intentionally untracked files that Git should ignore<br>


## How to Run ETL Pipeline
### 1. run from a command line:

  - Download a dataset from Kaggle:
    https://www.kaggle.com/datasets/behroozsohrabi/us-wildfire-records-6th-edition

  - Install all the libraries needed to execute main.py.
 ```
  pip3 install -r requirements.txt
```
  - Create a postgres database and a table using script from ``sql/create_table.sql``

  - Run the main.py script
```
  python3 main.py
```

### 2. run using docker:

! Ensure Docker is running locally
  

- Build an image

```bash
docker build -t etl_pipeline .

```

- Run the etl

```bash
docker run -d --name etl-container etl_pipeline

```
