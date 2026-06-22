joined_df = economies_df.join(
    countries_df,
    on="code",
    how="left"
)

joined_df.write.format("delta") \
    .mode("overwrite") \
    .save("s3://srh-data-engineering-project-storage/delta/economies_enriched/")
