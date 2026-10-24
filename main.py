"""Perform EDA on a bundled student study-habits dataset."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

HERE = Path(__file__).resolve().parent

def main():
    df = pd.read_csv(HERE / "student_habits.csv")
    numeric = df.select_dtypes(include="number")
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")
    print("\nData types:\n", df.dtypes.to_string())
    print("\nMissing values per column:\n", df.isna().sum().to_string())
    print("\nSummary statistics:\n", df.describe(include="all").to_string())
    print("\nNumeric outlier counts (IQR rule):")
    for column in numeric.columns:
        q1, q3 = numeric[column].quantile([0.25, 0.75])
        iqr = q3 - q1
        count = ((numeric[column] < q1 - 1.5 * iqr) | (numeric[column] > q3 + 1.5 * iqr)).sum()
        print(f"  {column}: {count}")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", center=0, fmt=".2f", ax=ax)
    ax.set_title("Correlation heatmap: student habits")
    fig.tight_layout()
    output = HERE / "correlation_heatmap.png"
    fig.savefig(output, dpi=140); plt.close(fig)
    print(f"\nCorrelation heatmap saved to: {output}")
    print("\nStudy-hours / score correlation:", round(df["study_hours_per_day"].corr(df["exam_score"]), 3))

if __name__ == "__main__": main()
