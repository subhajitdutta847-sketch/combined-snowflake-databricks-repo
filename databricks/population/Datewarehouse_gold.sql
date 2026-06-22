CREATE TABLE IF NOT EXISTS population_enriched
USING DELTA
LOCATION 's3://srh-data-engineering-project-storage/delta/population_enriched/';

SELECT country_name, year, size
FROM population_enriched;
