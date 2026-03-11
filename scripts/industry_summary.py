import pandas as pd
df_certified_latest = pd.read_csv("D:\\Projects\\B-Crop-Social-Impact\\data\\processed\\bcorp_certified_latest.csv")

industry_summary = (
    df_certified_latest.groupby("industry_category")
    .agg(company_count=("company_id", "nunique"),
         avg_score=("overall_score", "mean"))
    .sort_values("avg_score", ascending=False)
)

print(industry_summary.head(15))