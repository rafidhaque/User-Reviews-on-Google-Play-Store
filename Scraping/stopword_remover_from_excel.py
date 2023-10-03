import stopword_remover as sr
import openpyxl

wb = openpyxl.load_workbook("new.xlsx")

ws = wb['Sheet1']

for cell in ws['A']:
    if isinstance(cell.value, str):
        cell.value = sr.clean_sentence(cell.value)


wb.save("rocket_stop_word_removed.xlsx")
