import pandas as pd
nameBook = "2.1. CONEXIONES DE INTERNET FIJO.xlsx"
df = pd.read_excel(nameBook, sheet_name="Dataset", skiprows=3)

df['Mes'] = pd.to_datetime(df['Mes'], dayfirst=True, errors='coerce')
poblacion2023 = df[df['Mes'].dt.year == 2023]
#print(poblacion2023.tail(3))
#print(len(poblacion2023))
muestra = poblacion2023.sample(n=376, random_state=42)
#print(len(muestra))
#borramos la primera
muestra = muestra.drop(muestra.columns[0], axis=1)
#agregamos la muestra en una nueva hoja de calculo en el mismo libro
try:
    with pd.ExcelWriter(nameBook, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        muestra.to_excel(writer, sheet_name="Muestra2023", index=False)
        print("Se guardo con excelencia")
except Exception as e:
    print("Hubo un error", e)