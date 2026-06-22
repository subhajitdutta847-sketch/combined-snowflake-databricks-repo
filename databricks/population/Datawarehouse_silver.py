joined_df = population_df.join(
    countries_df,
    population_df["country_code"] == countries_df["code"],
    "left"
)

joined_df.write.format("delta") \
    .mode("overwrite") \
    .save("s3://srh-data-engineering-project-storage/delta/population_enriched/")
