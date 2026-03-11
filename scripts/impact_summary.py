import pandas as pd
df_certified_latest = pd.read_csv("D:\\Projects\\B-Crop-Social-Impact\\data\\processed\\bcorp_certified_latest.csv")

impact_summary = df_certified_latest[[
    "impact_area_community",
    "impact_area_customers",
    "impact_area_environment",
    "impact_area_governance",
    "impact_area_workers"
]].mean().sort_values(ascending=False)

print(impact_summary)

impact_summary.to_string(
    r"D:\Projects\B-Crop-Social-Impact\outputs\impact_summary.csv"
)
