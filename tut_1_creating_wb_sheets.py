import xlsxwriter

wb = xlsxwriter.Workbook('stats.xlsx')

ws = ['tab1', 'tab2', 'tab3']

for i, x in enumerate(ws):
    wb.add_worksheet(x)

wb.close()