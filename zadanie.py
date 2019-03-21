import pandas as pd

dataset=pd.read_csv('test.csv')

#podpunkt 1
data_urodzenia=dataset['data_urodzenia'].str.split('.', expand=True)
lista_indeskow=data_urodzenia[data_urodzenia[2]>='2000'].index
osoby_ur_2000=dataset.iloc[lista_indeskow]

#print(osoby_ur_2000)

data_set=pd.concat([dataset[['imie','nazwisko']],dataset['data_urodzenia'].str.split('.', expand=True)],axis=1)
data_set=data_set.rename(columns={0: "dzien", 1: "miesiac",2:"rok"})
data_set.rok=pd.to_numeric(data_set.rok)
print(data_set[data_set.rok>='2000'])


# data_urodzenia[data_urodzenia[2]>='2000']  
#podpunkt 2
#wykrycie uniklanych imion zenskich
lista_imion_zenskich=dataset[dataset['imie'].str.endswith('a')]['imie'].unique().tolist()
for i in lista_imion_zenskich:
    print(i, end=" ")