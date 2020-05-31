import xlsxwriter

wb = xlsxwriter.Workbook('esp.xlsx')
ws = wb.add_worksheet('Jan')

bold = wb.add_format({'bold': True})
currency_format = wb.add_format({'num_format': '$#,##0'})

ws.write('A1', 'Item', bold)
ws.write('B1', 'Cost', bold)

data = (
    ['Rent', 14000],
    ['Gas', 650],
    ['Food', 5000],
    ['Light Bill', 1000],)

row = 1
col = 0

for item, cost in data:
    ws.write(row, col, item)
    ws.write(row, col +1, cost, currency_format)
    row +=1

ws.write(row, 0, 'Total', bold)
ws.write(row, 1, '=sum(B2:B5)', currency_format)

chart = wb.add_chart({'type': 'column'})

wb.close()