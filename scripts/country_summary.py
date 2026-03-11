import pandas as pd
df_certified_latest = pd.read_csv("D:\\Projects\\B-Crop-Social-Impact\\data\\processed\\bcorp_certified_latest.csv")

country_summary = (
    df_certified_latest.groupby("country")
    .agg(company_count=("company_id", "nunique"),
         avg_score=("overall_score", "mean"))
    .sort_values("avg_score", ascending=False)
)

print(country_summary.head(15))

country_summary.to_string(
    r"D:\Projects\B-Crop-Social-Impact\outputs\country_summary.csv"
)


print('--------------------------------------------------------------------------------------------------')

country_summary_filtered = country_summary[country_summary["company_count"] >= 10] \
    .sort_values("avg_score", ascending=False)

print(country_summary_filtered.head(15))

country_summary_filtered.to_string(
    r"D:\Projects\B-Crop-Social-Impact\outputs\country_summary_filtered.csv"
)