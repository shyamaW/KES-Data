import pandas as pd

def get_spreadsheet_data(file_path, sheet_name):
    try:
        # Read the specified sheet from the Excel file
        print("reading a spreadsheet!!!")
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None