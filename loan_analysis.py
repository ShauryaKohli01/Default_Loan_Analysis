import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Read CSV files
df = pd.read_csv("lending_club_loan_two.csv")
meta_data = pd.read_csv("lending_club_info.csv", encoding="ISO-8859-1")

# View meta description
print(meta_data["Description"])       # Entire column
print(meta_data["Description"][0])    # First row only

# ------------------ BASIC INFO ------------------
print(df.shape)
print(df.head().T)

# ------------------ LOAN STATUS DISTRIBUTION ------------------
sns.countplot(x="loan_status", data=df)
plt.title("Loan Status Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(df["loan_status"].value_counts() * 100 / len(df))

# ------------------ LOAN AMOUNT HISTOGRAM ------------------
plt.figure(figsize=(12, 4))
sns.histplot(df["loan_amnt"], bins=50)
plt.title("Loan Amount Distribution")
plt.tight_layout()
plt.show()

# ------------------ HEATMAP OF NUMERIC CORRELATIONS ------------------
plt.figure(figsize=(12, 7))
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="viridis")
plt.title("Numeric Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

# ------------------ SCATTERPLOT: INSTALLMENT vs LOAN AMOUNT ------------------
plt.figure(figsize=(12, 7))
sns.scatterplot(x="installment", y="loan_amnt", data=df)
plt.title("Installment vs Loan Amount")
plt.tight_layout()
plt.show()

# ------------------ BOXPLOT: LOAN STATUS VS LOAN AMOUNT ------------------
plt.figure(figsize=(12, 7))
sns.boxplot(x="loan_status", y="loan_amnt", data=df)
plt.title("Loan Amount by Loan Status")
plt.tight_layout()
plt.show()

# ------------------ GROUP BY LOAN STATUS ------------------
print(df.groupby("loan_status")["loan_amnt"].describe())
print(df["grade"].unique())
print(meta_data)

# ------------------ COUNT PLOT BY GRADE ------------------
plt.figure(figsize=(12, 7))
sns.countplot(x="grade", hue="loan_status", data=df)
plt.title("Grade vs Loan Status")
plt.tight_layout()
plt.show()

# ------------------ PERCENT FULLY PAID / CHARGED OFF BY GRADE ------------------
for grade in ["A", "B", "G"]:
    subset = df[df["grade"] == grade]
    percentage = subset.groupby("loan_status")["grade"].count() * 100 / len(subset)
    print(f"\nGrade {grade} Distribution:\n{percentage}")

# ------------------ SUBGRADE ORDERED PLOT ------------------
plt.figure(figsize=(14, 7))
sub_order = sorted(df["sub_grade"].dropna().unique())
sns.countplot(x="sub_grade", hue="loan_status", order=sub_order, data=df)
plt.title("Subgrade vs Loan Status")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# ------------------ EMPLOYMENT LENGTH PLOT ------------------
plt.figure(figsize=(12, 7))
sns.countplot(x="emp_length", hue="loan_status", data=df)
plt.title("Employment Length vs Loan Status")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------ VERIFICATION STATUS ------------------
plt.figure(figsize=(12, 7))
sns.countplot(x="verification_status", hue="loan_status", data=df)
plt.title("Verification Status vs Loan Status")
plt.tight_layout()
plt.show()

# ------------------ LOAN STATUS CORRELATION ------------------
# Convert 'Fully Paid' to 1 and others to 0
df["loan_status"] = df["loan_status"].apply(lambda x: 1 if x == "Fully Paid" else 0)

# Plot correlation with loan_status
plt.figure(figsize=(12, 6))
df.select_dtypes(include="number").corr()["loan_status"].sort_values().drop("loan_status").plot(kind="bar")
plt.title("Correlation with Loan Status")
plt.tight_layout()
plt.show()





