# Python_data_summarize
 A lightweight Python script that loads CSV or Excel files, cleans the data, and generates a detailed summary report featuring numeric and categorical statistics. Ideal for quick exploratory analysis and dataset inspection.

🚀 Features

Multi-Format Support: Easily ingest data from both CSV (.csv) and Excel (.xlsx, .xls) files.

Automated Data Cleaning: Intelligent pre-processing to identify and remove rows containing empty strings or whitespace-only values across all columns.

Numeric Summary: Generates a full descriptive statistics table (count, mean, std, min, max, quartiles) for all numeric columns.

Categorical Insight: Provides the count of unique values (cardinality) and the top 3 most frequent values for all categorical columns.

Report Generation: Saves a clean, human-readable summary report to a local text file (summary_report.txt).

⚙️ Prerequisites

To run this utility, you need Python and the core data science libraries installed.

Python (3.7+)

pandas

💻 Installation

1. Clone the repository

git clone [https://github.com/YourUsername/Python-Data-Summarizer.git](https://github.com/YourUsername/Python-Data-Summarizer.git)
cd Python-Data-Summarizer


2. Install Dependencies

You only need the pandas library, which can be installed via pip:

pip install pandas openpyxl


(The openpyxl package is necessary for reading Excel files.)

3. Usage Example

Place your data file (e.g., input_data.csv) in the same directory.

Run the script from your terminal:

python data_inspector.py
