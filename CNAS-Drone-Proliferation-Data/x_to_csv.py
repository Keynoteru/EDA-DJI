import pandas as pd

# Cargar el archivo .xlsx
df = pd.read_excel('Proliferation_Master.xlsx')

# Guardar como archivo .csv
df.to_csv('Proliferation_Master.csv', index=False)

print("Archivo convertido exitosamente a CSV")
