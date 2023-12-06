import pandas as pd

try:
    # Load the dataset
    df = pd.read_csv('Auto_Sales_data.csv')
       
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except pd.errors.ParserError:
    print("There was an error parsing the CSV file.")
except FileNotFoundError:
    print("The CSV file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")