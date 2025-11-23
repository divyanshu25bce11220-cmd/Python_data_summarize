import pandas as pd
import os

class DatasetInspector:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        if not os.path.isfile(file_path):
            print(f"Oops! Could not find the file '{file_path}'. Make sure it's located in the current directory.")
            return
        try:
            if file_path.lower().endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(file_path)
            elif file_path.lower().endswith('.csv'):
                self.data = pd.read_csv(file_path)
            else:
                print("Unsupported file format. Please provide an Excel or CSV file.")
        except Exception as error:
            print(f"Failed to load the file due to: {error}")

    def preprocess(self):
        if self.data is not None:
            # Replace empty strings or whitespace-only cells with NaN and drop those rows
            self.data.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
            self.data.dropna(inplace=True)

    def generate_summary(self):
        if self.data is None:
            return None

        summary_report = {}

        numeric_cols = self.data.select_dtypes(include=['number']).columns
        categorical_cols = self.data.select_dtypes(include=['object', 'category']).columns

        if len(numeric_cols) > 0:
            numeric_summary = self.data[numeric_cols].describe().to_dict()
            summary_report['Numeric Data Overview'] = numeric_summary

        categorical_summary = {}
        for col in categorical_cols:
            unique_vals = self.data[col].nunique()
            top_vals = self.data[col].value_counts().head(3).to_dict()
            categorical_summary[col] = {
                'Unique Values Count': unique_vals,
                'Most Frequent (Top 3)': top_vals
            }
        if categorical_summary:
            summary_report['Categorical Data Overview'] = categorical_summary

        summary_report['Total Rows'] = len(self.data)
        summary_report['Total Columns'] = len(self.data.columns)

        return summary_report

    def save_report(self, summary):
        if summary is None:
            print("No data summary available to save.")
            return

        report_file = 'summary_report.txt'
        with open(report_file, 'w', encoding='utf-8') as file:
            file.write("### Dataset Summary Report ###\n\n")
            file.write(f"Total Rows: {summary.get('Total Rows', 'Unknown')}\n")
            file.write(f"Total Columns: {summary.get('Total Columns', 'Unknown')}\n\n")

            numeric = summary.get('Numeric Data Overview', {})
            if numeric:
                file.write("Numeric Data Summary:\n")
                for column, stats in numeric.items():
                    file.write(f"  - {column}:\n")
                    for stat_name, stat_val in stats.items():
                        if isinstance(stat_val, float):
                            file.write(f"      {stat_name}: {stat_val:.4f}\n")
                        else:
                            file.write(f"      {stat_name}: {stat_val}\n")
                    file.write("\n")

            categorical = summary.get('Categorical Data Overview', {})
            if categorical:
                file.write("Categorical Data Summary:\n")
                for column, details in categorical.items():
                    file.write(f"  - {column}:\n")
                    file.write(f"      Unique Values Count: {details['Unique Values Count']}\n")
                    file.write(f"      Most Frequent Values (Top 3):\n")
                    for val, count in details['Most Frequent (Top 3)'].items():
                        file.write(f"          {val}: {count}\n")
                    file.write("\n")

        print(f"Summary report has been generated and saved to '{report_file}'.")
        print("\n--- Here is a preview of the report ---\n")
        with open(report_file, 'r', encoding='utf-8') as file:
            print(file.read())


if __name__ == "__main__":
    data_file = "input_data.csv"
    inspector = DatasetInspector(data_file)
    if inspector.data is not None:
        inspector.preprocess()
        summary_result = inspector.generate_summary()
        inspector.save_report(summary_result)
