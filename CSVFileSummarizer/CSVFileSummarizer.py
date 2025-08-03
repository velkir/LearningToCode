import pandas as pd


class CSVFileSummarizer:
    """Main class to summarize data from csv-file."""
    def __init__(self, csv_path):
        self.df = self._load_csv(csv_path)

    def _load_csv(self, csv_path):
        """Load data from csv-file."""
        try:
            df = pd.read_csv(csv_path)
            return df
        except FileNotFoundError:
            print('Please provide a correct path to csv-file.')
        # with open(csv_path, 'r') as csv_file:
        #     csv_reader = csv.reader(csv_file)
        #     if header:
        #         fields = next(csv_reader)
        #     else:
        #         fields = None
        #     rows = []
        #     for row in csv_reader:
        #         rows.append(row)
        #     return fields, rows

    def count_rows(self):
        """Count rows."""
        return len(self.df)

    def count_average_on_numeric_fields(self):
        """Count average value of all numeric fields in data."""
        return self.df.mean(numeric_only=True)

    def detect_missing_data(self):
        """Detect and return rows with missing data."""
        return self.df[self.df.isnull().any(axis=1)]

    def export_to_json(self, json_path="data.json"):
        """Export data to json-file."""
        return self.df.to_json(json_path)

    def print_info(self):
        """Print all information about the data."""
        print(f"Number of rows: \n{self.count_rows()}")
        print(f"Average values of all numeric fields: \n{self.count_average_on_numeric_fields()}")
        print(f"All rows with missing data: \n{self.detect_missing_data()}")

