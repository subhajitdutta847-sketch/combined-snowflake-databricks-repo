CREATE TABLE IF NOT EXISTS economies_enriched
USING DELTA
LOCATION 's3://srh-data-engineering-project-storage/delta/economies_enriched/';

select country_name, year, gdp_percapita from economies_enriched
