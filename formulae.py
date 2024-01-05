import openpyxl
"""
Aim :- Aapply the given Excel formula to the given input cell 
A class for loading and manipulating Excel files.

"""
class Excelload:
    """
    A class attribute representing the loaded Excel workbook.
    Attributes:
        workbook (openpyxl.Workbook): The loaded Excel workbook.
        sheet (openpyxl.Worksheet): The active sheet in the workbook.

    Methods:
        __init__(path): Initializes the Excelload object with the path to the Excel file.
        calculate_formula(cell_reference): Calculates a formula based on the value in the specified cell.

    """
    def __init__(self, path):
        self.workbook = openpyxl.load_workbook(path)
        self.sheet = self.workbook.active

    def calculate_formula(self, cell_reference):
        """
          calculate_formula(cell_reference): Calculates a formula based on the value in the specified cell.
        """
        cv = self.sheet[cell_reference].value
        req = cv * (cv - 1) * (cv - 2) / 6
        return req

if __name__=="__main__":
    excel_obj = Excelload('Financial Sample.xlsx')
    result = excel_obj.calculate_formula('G236')
    print(result)
