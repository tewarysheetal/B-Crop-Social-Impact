import pandas as pd
df_certified_latest = pd.read_csv("D:\\Projects\\B-Crop-Social-Impact\\data\\processed\\bcorp_certified_latest.csv")

industry_impact = df_certified_latest.groupby("industry_category")[[
    "impact_area_community",
    "impact_area_customers",
    "impact_area_environment",
    "impact_area_governance",
    "impact_area_workers"
]].mean()

print(industry_impact.head())

industry_impact.to_string(
    r"D:\Projects\B-Crop-Social-Impact\outputs\industry_impact_summary.csv"
)
