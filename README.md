# 🎮 Game Industry Analytics Pipeline

A Data Engineering project that extracts video game data from the RAWG API, transforms and normalizes nested JSON structures through an ETL pipeline, stores the data in PostgreSQL, and generates business insights through SQL analytics and Power BI dashboards.

## Project Overview

This project simulates a real-world data engineering workflow by building a complete pipeline from data ingestion to analytics.

The pipeline:

1. Extracts video game data from the RAWG API.
2. Transforms and cleans nested JSON datasets.
3. Normalizes entities and relationships into a relational database.
4. Loads data into PostgreSQL.
5. Generates analytical reports and dashboards in Power BI.

## Architecture

RAWG API
↓
Python ETL Pipeline
↓
Data Transformation & Normalization
↓
PostgreSQL Data Warehouse
↓
SQL Analytics
↓
Power BI Dashboards

## Technologies

* Python
* PostgreSQL
* SQLAlchemy
* RAWG API
* Power BI
* Git
* GitHub

## Data Model

### Core Entity

* Games

### Dimension Tables

* Genres
* Platforms
* Stores
* Tags

### Relationship Tables

* Game_Genres
* Game_Platforms
* Game_Stores
* Game_Tags

## ETL Process

### Extract

Data is collected from the RAWG API using paginated requests.

### Transform

The transformation layer:

* Cleans and validates raw data
* Extracts relevant attributes
* Generates derived fields (e.g., release year)
* Removes duplicates
* Flattens nested JSON structures
* Creates relational mapping tables

### Load

Processed datasets are loaded into PostgreSQL using SQLAlchemy with idempotent loading strategies.

## Dataset Statistics

Current dataset contains:

* 1,000 Games
* 19 Genres
* 32 Platforms
* 10 Stores
* 825 Tags

Relationship records:

* 2,511 Game-Genre relationships
* 4,352 Game-Platform relationships
* 3,565 Game-Store relationships
* 18,093 Game-Tag relationships

## Business Questions

This project explores questions such as:

* Which genres receive the highest ratings?
* Which platforms host the best-rated games?
* Do longer games receive better reviews?
* Which tags are most common among highly rated games?
* How has game quality evolved over time?
* What is the relationship between Metacritic scores and user ratings?

## Skills Demonstrated

* Data Extraction from REST APIs
* ETL Pipeline Development
* Data Cleaning and Transformation
* Relational Data Modeling
* Many-to-Many Relationships
* SQL Analytics
* Database Design
* Data Visualization
* Business Intelligence
* Power BI Dashboard Development

## Future Improvements

* Incremental data loading
* Cloud deployment (Azure / GCP)
* Data orchestration with Airflow
* Containerization with Docker
* Automated testing
* CI/CD pipelines

## Author

Alejandro Castañeda
