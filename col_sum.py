import re
import openpyxl
"""
Aim:- Find the sum of the range of given cells in a column 
Initializes an instance of the ExcelSum class.

Parameters:
- excel_file_path (str): The path to the Excel file.

Attributes:
- workbook (openpyxl.Workbook): The loaded workbook object.
- sheet (openpyxl.Worksheet): The active worksheet in the workbook.
"""
class ExcelSum:
    
    def __init__(self, excel_file_path):
        self.workbook = openpyxl.load_workbook(excel_file_path)
        self.sheet = self.workbook.active

    def summation(self, start_cell, end_cell):
        """
            Calculates the sum of a range of cells in a column.

            Parameters:
            - start_cell (str): The starting cell of the range, in the format 'A1'.
            - end_cell (str): The ending cell of the range, in the format 'A1'.

            Returns:
            - int: The sum of the values in the range of cells.

            Example:
                excel_calculator = ExcelSum('Financial Sample.xlsx')
                result = excel_calculator.summation('K2', 'K6')
                print(result)  # Output: 25000
            """
        s = 0
        x = int(start_cell[1:])
        y = int(end_cell[1:])

        for cell in range(x, y + 1):  # Adjust the range to include the end_cell
            values_to_sum = self.sheet[str(start_cell[0] + str(cell))].value

            if values_to_sum is not None:
                s += values_to_sum

        return s

if __name__ == "__main__":
    excel_calculator = ExcelSum('Financial Sample.xlsx')
    
    s = '=SUM(F390:F395)'
    match = re.search(r'\((.*?)\:', s)
    match2 = re.search(r'\:(.*?)\)', s)

    if match and match2:
        start_cell = match.group(1)
        end_cell = match2.group(1)

        result = excel_calculator.summation(start_cell, end_cell)
        print("Result:", result)
    else:
        print("Invalid formula format")
