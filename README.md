# Iris EDA App with Streamlit

## Overview

This is an interactive **Exploratory Data Analysis (EDA)** web application built using **Streamlit**. The app allows users to load, explore, and visualize the famous **Iris dataset**. Users can preview the dataset, view summary statistics, plot value counts, and visualize correlations and other plots like bar charts and pie charts.

### Features:
- **Preview Dataset**: View the first few rows of the dataset.
- **Shape of Dataset**: Display the number of rows and columns in the dataset.
- **Select Columns**: Display selected columns from the dataset.
- **Summary Statistics**: Generate summary statistics (mean, standard deviation, etc.) for the dataset.
- **Value Counts**: Display value counts for the target column.
- **Data Visualizations**:
  - Correlation plots using Matplotlib or Seaborn
  - Pie chart of the target column
  - Bar chart of value counts

---

## Requirements

Before running the app, make sure you have the following installed:

### 1. Python (version 3.7 or later)
Ensure Python is installed on your machine. You can download it from [here](https://www.python.org/downloads/).

### 2. Install Required Libraries
Use the following command to install the necessary libraries:

### 3. Iris Dataset
The app assumes the iris.csv file is located in the same directory as the script. If you don't have the dataset, you can download it online.

### 4. Libraries required
```bash
pip install streamlit pandas matplotlib seaborn
```
## Run the Streamlit app:
### Run the following command to launch the Streamlit app:
```
streamlit run app.py
```