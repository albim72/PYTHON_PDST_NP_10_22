import xlsxwriter
workbook = xlsxwriter.Workbook("wydatki.xlsx")
worksheet = workbook.add_worksheet("moje_wydatki")
#deklaracja formatów
bold = workbook.add_format({'bold':True})
money = workbook.add_format({'num_format':'#.##0 zł'})
worksheet.write('A1','id',bold)
worksheet.write('B1','rodzaj wydatku',bold)
worksheet.write('C1','kwota',bold)

wydatki  =(
    ['1','żywność',2500],
    ['2','czynsz',1200],
    ['3','gaz',680],
    ['4','prąd',590],
    ['5','utrzymanie samochodu',900],
    ['6','ubrania',500],
    ['7','edukacja',700],
    ['8','hobby',300],
    ['9','inne',200],
)
row =1
col =0
for id, rodzaj, koszt in (wydatki):
    worksheet.write(row,col,id)
    worksheet.write(row,col+1,rodzaj)
    worksheet.write(row,col+2,koszt,money)
    row += 1
worksheet.write(row,0,'Koszt całkowity',bold)
worksheet.write(row,2,'=SUM(C2:C10)',money)
workbook.close()
