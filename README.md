## Exploratory Data Analysis: Student Study Habits
### Problem Statement
Systematically inspect study habits and exam scores, including missingness, distributions, outliers, and relationships between numeric variables.
### Dataset
A bundled, illustrative dataset of 25 fictional students with study hours, sleep, screen time, attendance, exam score, and study method. It is synthetic and should not be used to draw conclusions about real students.
### Approach
Use pandas for data types, missing-value counts, descriptive statistics, and IQR-based outlier counts. Use a Seaborn correlation heatmap for numeric relationships.
### Result
The script prints a compact EDA report, reports the study-hours/score correlation, and saves `correlation_heatmap.png`.
### Key Insight
The deliberately unusual record with high screen time and low attendance reminds us that a simple positive study-hours/score relationship does not explain every student's result; outliers deserve context, not automatic deletion.
### How to Run
```bash
python -m pip install -r requirements.txt
python main.py
```
