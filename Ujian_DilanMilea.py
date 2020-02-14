import requests
import json


#Dilan (Sampora, Cisauk, Tangerang)
#Milea (Citarum, Bandung Wetan, Bandung)
#url = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
# data = requests.get(url)
# hasil = data.json()
# print (hasil['11'][0]['strTeam'])
   




#Jarak
url3 = 'https://www.zipcodeapi.com/rest/4so5q9zrJyhfJHCqYpmlZWVZBn5ocQTcQ9wMmtGPZk7nTiFTum5zyKb3JiLcEZPH/distance.json/15345/40115/km'
data = requests.get(url3)
hasilJarak = data.json()

print ("Kode Pos lokasi Dilan adalah", "15345")
print ("Kode Pos lokasi Milea adalah", "40115")
print ("Jarak Dilan & Milea adalah", (hasilJarak['distance']), "km")