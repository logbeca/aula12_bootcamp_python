from interface.classes.csv_class import CsvProcessor
import pandas as pd

arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv  = CsvProcessor(arquivo_csv)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_por(['estado','preco'],['SP','10,50']))
print(arquivo_csv.df)

print ('###############')
#arquivo_csv2 = '../exemplo2.csv'
#filtro2 = 'estado'
#limite2 = 'SP'

#arquivo_csv2  = CsvProcessor(arquivo_csv2)
#arquivo_csv2.carregar_csv()
#print(arquivo_csv.filtrar_por(['estado','preco'],['SP','10,50']))
#print(arquivo_csv2.df)
