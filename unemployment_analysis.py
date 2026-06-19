import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Unemployment Rate by Region
# -----------------------------

plt.figure(figsize=(12,6))

sns.barplot(
    x="Region",
    y="Estimated Unemployment Rate (%)",
    data=df
)

plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")

plt.tight_layout()
plt.savefig("region_unemployment.png")
plt.show()

# -----------------------------
# Heatmap
# -----------------------------

plt.figure(figsize=(8,5))

numeric_df = df.select_dtypes(include='number')

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()

# -----------------------------
# State-wise Analysis
# -----------------------------

plt.figure(figsize=(12,6))

sns.boxplot(
    x="Region",
    y="Estimated Unemployment Rate (%)",
    data=df
)

plt.xticks(rotation=90)

plt.title("State-wise Unemployment Distribution")

plt.tight_layout()
plt.savefig("state_analysis.png")
plt.show()

print("\nAnalysis Completed Successfully!")