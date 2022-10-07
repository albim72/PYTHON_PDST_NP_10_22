import pandas as pd
import xlsxwriter

df = pd.DataFrame({'Data':[10,20,30,40,50,60,70,110,150,160,220,300]})

writer = pd.ExcelWriter('pandas_podstawowy.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='ramka')
writer.save()
