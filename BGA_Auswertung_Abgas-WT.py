import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

filename = 'BGA\\empuron_export_2.csv'

custom_date_parser = lambda x: datetime.strptime(x, "%d.%m.%Y %H:%M")
headerlist = ["Datum/Zeit","V_trGas", "Vs_trGas", "Restfeuchte","Vs_Betrieb", "P_BHKW1", "P_BHKW2", "T_Gas"]

#create Dataframe 'df' from csv values as Energiedaten
Energiedaten = pd.read_csv(filename, sep=';',parse_dates=[0], date_parser=custom_date_parser,header=1, low_memory=False)
#del data2020_1D_Ges ["QBHKW1"]
#data2020_no_BHKW1 = data2020_1D_Ges.drop(["QBHKW1"], axis=1)
del Energiedaten['Unnamed: 8']
del Energiedaten['Unnamed: 9']

Energiedaten=Energiedaten.set_axis(headerlist,axis="columns")
Energiedaten = Energiedaten.set_index(['Datum/Zeit'])

Vs_trGas = Energiedaten[["Vs_trGas"]]
Vs_trGas_1h = Vs_trGas.resample("1H").mean()
Vs_trGas_1h_2020 = Vs_trGas_1h.loc['2020-01-01 00:00' : '2020-12-31 23:59' ]
#print(Vs_trGas_1h_2020)

#print(Energiedaten)

#s = Energiedaten.values.tolist()
#Energiedaten_float = pd.to_numeric(s,errors="coerce")
#s = Energiedaten.values.tolist()

#Energiedaten[["V_trGas", "Vs_trGas","Vs_Betrieb", "P_BHKW1", "P_BHKW2", "T_Gas"]] = Energiedaten[["V_trGas", "Vs_trGas","Vs_Betrieb", "P_BHKW1", "P_BHKW2", "T_Gas"]].astype(int)
#print(Energiedaten_float.dtypes)

P_Strom_BHKW2 = Energiedaten[["P_BHKW2"]]
a = P_Strom_BHKW2.dtypes
c = P_Strom_BHKW2.astype("int32")
#P_Strom_BHKW2_1h = P_Strom_BHKW2.resample("1H").mean()
#P_Strom_BHKW2_2020 = P_Strom_BHKW2_1h.loc['2020-01-01 00:00' : '2020-12-31 23:59']

#print(a)
print(c)



#print(Vs_trGas_1h_2020.describe(),'\n')

#Daten exportieren:
#np.savetxt(r'c:\data\np.txt', df.values, fmt='%d')
#f = np.savetxt("2020_1M_P_Ges.txt",data2020_1M_P_Ges, fmt='%.2f')
#f = np.savetxt("2020_1M_Q_Ges.txt",data2020_1M_Q_Ges.values, fmt='%.0f')

#Export to Excel:
#writer = pd.ExcelWriter("P_Strom_BHKWs_2020.xlsx")
#f_excel = P_Strom_BHKWs_1h_2020.to_excel(writer)
#writer.save()
