import openpyxl

wb = openpyxl.load_workbook('Rocket2.xlsx')

ws = wb['Sheet1']

for cell in ws['A']:
    if isinstance(cell.value, str) and len(cell.value.split()) < 4:
        cell.value = ''

wb.save('new.xlsx')
