# LendingClub Loan Data EDA Project

This project performs Exploratory Data Analysis (EDA) on LendingClub’s peer-to-peer lending dataset using Python. 
The goal is to uncover credit risk trends and understand borrower behavior based on real-world data. 
By visually analyzing features like loan amount, grade, employment, verification, and repayment status. 
We explore patterns that could eventually help predict loan defaults a valuable insight for lenders, banks, and financial analysts.


# What is Exploratory Data Analysis (EDA)?

Exploratory Data Analysis (EDA) is the process of visually and statistically exploring a dataset to summarize its main characteristics, detect patterns, and uncover relationships.
EDA is often the first step in any data science or machine learning project, used before modeling.

# Dataset Description

We use two CSVs:

1. lending_club_loan_two.csv – The main dataset containing thousands of individual loans, including features like:

2. loan_amnt: amount of loan issued

3. loan_status: whether the loan was fully paid or charged off

4. grade, sub_grade: creditworthiness scores

5. installment, emp_length, verification_status: borrower details

6. lending_club_info.csv – A metadata file describing each column in the main dataset, useful for interpretation.


# Importing Reqquired Libraries

<img width="554" alt="image" src="https://github.com/user-attachments/assets/97f7da50-4e19-4f00-9d34-ef6a4abfd54d" />

# Breakdown with Visuals

1. Loan Status Distribution
A countplot shows the balance between Fully Paid vs Charged Off loans. This gives us an idea of overall default rates in the dataset. 
It's critical for understanding how imbalanced the dataset is and provides a base for risk analysis.




<img width="630" alt="image" src="https://github.com/user-attachments/assets/f16de3db-e127-4850-bb6b-4f7849ed8ce2" />





2. Loan Amount Histogram
This histogram displays the distribution of loan sizes. Most loans are centered around $10,000–$15,000, with a few larger loans.
This helps identify common borrowing patterns and possible outliers.


<img width="1188" alt="image" src="https://github.com/user-attachments/assets/9ababd3b-a991-4bda-a05a-5ee79b5d8833" />



3. Correlation Heatmap
The heatmap shows pairwise correlations between numerical variables like loan_amnt, installment, annual_inc, etc.
It reveals that loan_amnt and installment are highly correlated, which makes sense (larger loans → larger monthly installments).


<img width="1132" alt="image" src="https://github.com/user-attachments/assets/24a6e6b6-516a-4522-b74b-148343e0ac6f" />



4. Installment vs Loan Amount Scatterplot
This scatterplot confirms the linear relationship between installment and loan_amnt.
It shows a strong positive correlation, helping validate feature quality and logic.


<img width="1184" alt="image" src="https://github.com/user-attachments/assets/ba06ed14-aebe-419f-8bd6-34269d127f23" />



5. Loan Status vs Loan Amount Boxplot
This boxplot compares loan sizes between fully paid and defaulted loans.
Loans that were charged off tend to be slightly larger, showing that higher loan amounts may carry higher default risk.


<img width="1187" alt="image" src="https://github.com/user-attachments/assets/63bb88db-0251-4863-a4c4-0908a9438adb" />



6. Grade vs Loan Status Countplot
Loan grade is a risk rating assigned by LendingClub. This figure shows that lower grades (F, G) have a higher proportion of defaults,
indicating that credit grade is a powerful predictor of risk.


<img width="1187" alt="image" src="https://github.com/user-attachments/assets/781118eb-5ab5-4a43-8663-c64fac529c37" />



7. Grade-Wise Default Percentages
We computed the percentage of defaults vs full payments for grades A, B, and G. Grade G had the highest default rate, reinforcing what we saw in the previous plot.


<img width="1190" alt="image" src="https://github.com/user-attachments/assets/cf2d30ea-92d8-4c11-9ba5-cc58be48503b" />



8. Subgrade vs Loan Status
Subgrades (e.g., A1–A5, B1–B5) provide more granularity.
This visualization shows increasing default risk as we move from A1 to G5, supporting the idea that finer credit classifications help in risk prediction.


<img width="1398" alt="image" src="https://github.com/user-attachments/assets/5bbad7b6-b4b3-4765-b1b1-151a6cbc5832" />



9. Employment Length vs Loan Status
This plot examines how borrower employment length relates to repayment.
There’s no strong visual trend, but some variation exists — short or uncertain employment periods may correlate with risk.


<img width="1190" alt="image" src="https://github.com/user-attachments/assets/cf2d30ea-92d8-4c11-9ba5-cc58be48503b" />



10. Verification Status vs Loan Status
Here we analyze if verification of income or employment influences default.
Surprisingly, even verified applications have defaults — suggesting verification alone isn’t a strong filter, though it still provides context.


<img width="1193" alt="image" src="https://github.com/user-attachments/assets/1f14e98a-e833-403f-a213-d34947258f88" />



11. Correlation with Loan Status (Bar Plot)
Finally, we converted loan_status into binary (1 = Fully Paid, 0 = Charged Off) and plotted correlations.
Features like installment, dti, and annual_inc showed moderate correlation with repayment outcomes, offering clues for future predictive modeling.


<img width="1185" alt="image" src="https://github.com/user-attachments/assets/c224599a-343c-4434-8592-f91d2b0e66e8" />



# Conclusion

This project showcases how Exploratory Data Analysis (EDA) helps uncover patterns in lending behavior. 

1. Identified which borrower traits affect loan repayment.

2. Verified that LendingClub’s grading system is fairly accurate.

3. Learned that loan size, employment, and subgrades all influence risk — but not in isolation.

4. Found that no single factor predicts default, reinforcing the need for modeling approaches like logistic regression or machine learning.

This analysis is a foundation for building credit risk models, automating loan approvals, or setting interest rates based on applicant risk.

















