
import pandas as pd

tabela = pd.read_csv("generatedBy_react-csv.csv", sep=";")
display(tabela)

tabela2 = tabela.fillna(value="Não Registrado!")
tmax = list(tabela2['Temp. Max. (C)'])
data = list(tabela2['Data'])
hora = list(tabela2['Hora (UTC)'])


ttemp = [temperatura for temperatura in tmax if temperatura != "Não Registrado!"]

tmax2 = [temperatura.replace(',', '.') for temperatura in ttemp ]

tmax3 = [float(temperatura) for temperatura in tmax2 ]

temperatura = pd.Series(tmax3, name = "Temp. Max. (C)")

data_comp = list()
for dt in data:
  for hr in hora:
    temp = dt +" - "+ str(hr)
    data_comp.append(temp)

print(data_comp) 

data = pd.Series(data_comp, name = "Data")

# create a dataframe
tabela3 = pd.DataFrame(data)
  
tabela4 = tabela3.join(temperatura)
  
# show the dataframe
display(tabela4)

