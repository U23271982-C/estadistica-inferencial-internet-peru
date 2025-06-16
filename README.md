# 📊 Análisis Estadístico Inferencial sobre el Acceso a Internet en Perú (Datos Abiertos)

Este proyecto aplica técnicas de **estadística inferencial** utilizando datos reales del gobierno peruano, provenientes del portal [datosabiertos.gob.pe](https://www.datosabiertos.gob.pe/). El objetivo es analizar **el número de conexiones a internet por tipo de tecnología** y su relación con la región geográfica del país, identificando diferencias significativas mediante pruebas paramétricas y no paramétricas.

---

## 🎯 Objetivo del Proyecto

Realizar un análisis estadístico inferencial para Determinar la relación estadísticamente significativa entre el tipo de tecnología de acceso a internet y la cantidad de conexiones por departamento en el Perú durante el año 2023., utilizando Python como herramienta de análisis.

---

## 📊 Variables Analizadas
### Variable Independiente
- `Tipo de tecnología de conexión a internet` (cualitativa nominal): Clasificación del tipo de conexión a internet, tales como Fibra óptica, Cablemódem, ADSL, Satelital, entre otros.
- `Mes del Reporte` (cuantitativa de intervalo):Indica el mes en que se registraron los datos; permite analizar el comportamiento temporal.
- 
- `Rango de Velocidad de Bajada` (cualitativa ordinal):Clasificación de la velocidad del servicio en rangos ordenados (de menor a mayor velocidad).
### Variable Dependiente
- `Número de conexiones a internet` (cuantitativa de razón): Representa la cantidad total de conexiones a internet reportadas por los departamentos del Perú, sin importar la tecnología empleada.
---

## 🧪 Hipótesis Planteadas

### 📌 Grupo 1: Hipótesis Paramétricas
1. Hipótesis referida a la media poblacional
-	H₀: La media de conexiones a internet en Perú es igual a 5,000.
- H₁: La media de conexiones a internet en Perú es diferente de 5,000.
2. Hipótesis referida a la proporción poblacional  
- Hipótesis nula (H₀): La proporción de conexiones que usan tecnología de fibra óptica es igual al 50%.
- Hipótesis alternativa (H₁): La proporción de conexiones que usan tecnología de fibra óptica es diferente al 50%.50%.
3. Hipótesis referida a la varianza poblacional
- Hipótesis nula (H₀): La varianza de las conexiones a internet en todo el país es igual a 1,000,000.
- Hipótesis alternativa (H₁): La varianza de las conexiones a internet en todo el país es diferente de 1,000,000.
4. Hipótesis sobre la diferencia entre dos medias poblacionales (grupos independientes)
- Hipótesis nula (H₀): La media de conexiones con fibra óptica es igual a la media de conexiones con cablemódem.
- Hipótesis alternativa (H₁): La media de conexiones con fibra óptica es diferente a la media de conexiones con cablemódem.
5. Hipótesis estadísticas para muestras relacionadas
- Hipótesis nula (H₀): No existen diferencias significativas en el número promedio de conexiones de internet con fibra óptica entre los distintos meses del 2023.
6. Hipotesis estadisticas para diferencia entre dos proporciones
- Hipótesis alternativa (H₁):  La proporción de conexiones por Fibra Óptica es igual a la proporción de conexiones por Cablemódem.
- Hipótesis alternativa (H₁): La proporción de conexiones por Fibra Óptica es diferente a la proporción de conexiones por Cablemódem.
7. Hipótesis para la razón entre varianzas
-Hipótesis nula (H₀): La varianza en el número de conexiones de fibra óptica es igual a la varianza de cablemódem.
- Hipótesis alternativa (H₁): Las varianzas en el número de conexiones entre ambas tecnologías son diferentes.
### 📌 Grupo 2: Hipótesis No Paramétricas


---

## 🧰 Tecnologías Utilizadas

- Python 3.11+
- Pandas
- Openpyxl (para leer Excel)

---

## 📎 Fuente de los Datos

Los datos utilizados en este proyecto fueron obtenidos del portal oficial de datos abiertos del Perú:

> **Título del Dataset**: Conexiones a Internet por Tipo de Tecnología  
> **Fuente**: [datosabiertos.gob.pe](https://www.datosabiertos.gob.pe/dataset)  
> **Entidad**: Ministerio de Transportes y Comunicaciones (MTC)

---

## 💡 Conclusiones

Este proyecto permitió aplicar conocimientos de estadística inferencial en un contexto real, fortaleciendo habilidades en la manipulación de datos, formulación de hipótesis, y aplicación de pruebas estadísticas. Además, se demostró la capacidad de usar herramientas modernas de análisis en Python, lo cual es altamente relevante en el ámbito de la ingeniería de sistemas.

---

## 👨‍💻 Autor

**Israel Cubas**  
Estudiante de Ingeniería de Sistemas  
[LinkedIn](https://www.linkedin.com/) · [GitHub](https://github.com/)  
