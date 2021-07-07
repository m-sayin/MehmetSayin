import json
kisilerDosya=open("MehmetSayin.json")
veri=json.load(kisilerDosya)
print(veri["kimlik"]["ad"])
print(veri["kimlik"]["soyad"])
kisilerDosya.close()
#değişiklik yapıldı.