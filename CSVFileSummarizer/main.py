from CSVFileSummarizer import CSVFileSummarizer


path = "employees.csv"
csvSummarizer = CSVFileSummarizer(path)
# print(csvSummarizer.count_rows())
# print(csvSummarizer.count_average_on_numeric_fields())
# print(csvSummarizer.detect_missing_data())
# csvSummarizer.export_to_json()
csvSummarizer.print_info()