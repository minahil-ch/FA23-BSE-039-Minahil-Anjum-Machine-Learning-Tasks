# Graded Lab 3 – Machine Learning Fundamentals
Linear Regression / Multiple Linear Regression / Logistic Regression / Logistic Regression (Multiclass) / Polynomial Regression

## Folder contents

```
notebooks/
  Lab_Task_1_Linear_Regression.ipynb
  Lab_Task_2_Multiple_Linear_Regression.ipynb
  Lab_Task_3_Logistic_Regression.ipynb
  Lab_Task_4_Logistic_Regression_Multiclass.ipynb
  Lab_Task_5_Polynomial_Regression.ipynb
datasets/
  canada_per_capita_income.csv   -> used by Lab Task 1
  hiring.csv                     -> used by Lab Task 2
  HR_comma_sep.csv               -> used by Lab Task 3
  Position_Salaries.csv          -> used by Lab Task 5
  (Lab Task 4 needs no csv - it uses sklearn's built-in iris dataset)
```

## How to run each notebook in Google Colab

1. Go to https://colab.research.google.com and choose **Upload** → select the `.ipynb` file.
2. Run the cells from top to bottom (Runtime → Run all, or Shift+Enter cell by cell).
3. Whenever a cell calls `files.upload()`, a file picker will pop up — select the
   matching `.csv` from the `datasets` folder in this zip.
4. Everything else (installing `word2number`, training, plotting, predicting) runs
   automatically — just read the markdown text above each cell, it explains what that
   step is doing and why.

## A note on Lab Task 3's dataset

The task asks for the Kaggle dataset `giripujar/hr-analytics` (`HR_comma_sep.csv`).
Kaggle needs a login/API key to script-download, so this zip ships a synthetic
`HR_comma_sep.csv` built with **the exact same column names** (satisfaction_level,
last_evaluation, number_project, average_montly_hours, time_spend_company,
Work_accident, left, promotion_last_5years, sales, salary) and realistic
salary/satisfaction/department patterns, so the notebook runs immediately without
any account. If your instructor wants the real Kaggle file specifically:
1. Download the real `HR_comma_sep.csv` from the Kaggle link.
2. Upload that file instead, in Step 1 of the Lab Task 3 notebook.
The rest of the code needs no changes since the schema is identical.

## Submitting

Zip the whole `notebooks/` + `datasets/` folders (or this entire folder) and submit
as instructed. Each notebook already contains the pre-run outputs from testing, but
it's a good idea to re-run all cells yourself in Colab (Runtime → Run all) right
before exporting/submitting, so the outputs reflect your own execution.
