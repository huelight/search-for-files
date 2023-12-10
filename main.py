import os
from datetime import datetime


def search_files_by_extension_and_month_year(folder_path, target_extension, target_month, target_year):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[-1].lower()

            # Check if the file has the target extension
            if file_extension == target_extension.lower():
                # Get the file's last modification timestamp
                last_modified_timestamp = os.path.getmtime(file_path)
                last_modified_date = datetime.fromtimestamp(last_modified_timestamp)

                # Check if the file was modified in the target month and year
                if last_modified_date.month == target_month and last_modified_date.year == target_year:
                    print(f"File Name: {file}")
                    print(f"File Path: {file_path}")
                    print("------------------------")


year = input("Year you want to search: must be in format e.g '2000'\n")
month = input("Month you want to search: must be in format e.g '01'\n")
extension = input("Extension of what you want to search for, e.g  '.pdf' \n")

try:
    year = int(year)
    month = int(month)
    now = datetime.now()

    if month > 12:
        print("Month is greater than 12")
    elif year > now.year:
        print("Year exceeds today's date")
    else:
        search_files_by_extension_and_month_year("C:\\", target_extension=extension, target_month=month, target_year=year)

except ValueError:
    print("Wrong format, type(int) expected,  please restart the program and enter proper input.")


