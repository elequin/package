import openpyxl
import re

"""
Aim:- Calculate the sum of given range of cell values in a row in a excel. 
The Row_sum class is used to calculate the sum of values in a row of an Excel spreadsheet.

Attributes:
    workbook (openpyxl.Workbook): The workbook object representing the Excel file.
    sheet (openpyxl.Worksheet): The active worksheet in the workbook.

Methods:
    __init__(self, path): Initializes the Row_sum object with the path to the Excel file.
   
Example usage:
    excel_val = Row_sum('Financial Sample.xlsx')
    formula_result = excel_val.calculate_sum('=SUM(J401:L401)')
    print("Result:", formula_result)
"""
class Row_sum:
    def __init__(self, path):
        self.workbook = openpyxl.load_workbook(path)
        self.sheet = self.workbook.active

    def extract_columns_and_row(self, formula):
        """
        extract_columns_and_row(self, formula): Extracts the start and end columns 
        and the row number from a formula. 
        """
        start_column = re.search(r'\((.*?)\:', formula).group(1)[0].lower()
        end_column = re.search(r'\:(.*?)\)', formula).group(1)[0].lower()

        first = ord(start_column) - ord('a') + 1
        second = ord(end_column) - ord('a') + 1

        row_number = re.search(r'\d+', formula).group()
        return first, second, row_number

    def calculate_sum(self, formula):
        """
        calculate_sum(self, formula): Calculates the sum of values in the specified row 
        based on the given formula.
        """
        first, second, row_number = self.extract_columns_and_row(formula)

        row_values = [cell.value for cell in self.sheet[row_number]]
        summ = 0
        for i in range(first - 1, second):
            summ += row_values[i]

        return summ

if __name__ == "__main__":
    excel_val = Row_sum('Financial Sample.xlsx')
    formula_result = excel_val.calculate_sum('=SUM(J401:L401)')
    print("Result:", formula_result)
