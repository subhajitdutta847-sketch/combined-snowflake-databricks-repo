economies_df = spark.read.csv(
    "s3://srh-data-engineering-project-storage/raw/economies/",
    header=True,
    inferSchema=True
)

countries_df = spark.read.csv(
    "s3://srh-data-engineering-project-storage/raw/countries/",
    header=True,
    inferSchema=True
)
