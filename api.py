import requests

# bigKode  = requests.get("http://jendela.data.kemdikbud.go.id/api/index.php/cwilayah/wilayahKabGet")
# getKode  = bigKode.json()

# namaKota = 'Kota Bogor'

# for key,value in getKode.items():
#     myKota  = []
#     myKode = []
#     for kode in value:
#         myKota.append(kode['nama'])
#         myKode.append(kode['kode_wilayah'])
    
# if namaKota in myKota:
#     idx = myKota.index(namaKota)
#     print("index ke-{},\n{}-{}".format(idx,myKota[idx],myKode[idx]))

#     # request data

#     data=requests.get("http://jendela.data.kemdikbud.go.id/api/index.php/Csekolah/detailSekolahGET?mst_kode_wilayah={}&bentuk={}".format(myKode[idx],"sd"))
#     db_data = data.json()

#     print(db_data['data'][0])

#     for x,i in db_data.items():
#         for v in i:
#             print(v['sekolah'])

# else :
#     print('not found')

nSekolah = "SMAS PESAT"
detailSekolah = requests.get("http://jendela.data.kemdikbud.go.id/api/index.php/Csekolah/detailSekolahGET?mst_kode_wilayah=026100&bentuk=sma")

list = detailSekolah.json()

for key,value in list.items():
    mySchool  = []
    myId=[]
    myProv=[]
    myCity=[]
    myKecamatan=[]
    myNpsn=[]
    myStreet=[]
    for kode in value:
        mySchool.append(kode['sekolah'])
        myStreet.append(kode['alamat_jalan'])
        myKecamatan.append(kode['kecamatan'])
        myCity.append(kode['kabupaten_kota'])
        myProv.append(kode['propinsi'])
        myNpsn.append(kode['npsn'])
        myId.append(kode['id'])
    
if nSekolah in mySchool:
    idx = mySchool.index(nSekolah)
    print("index ke-{},\nNama Sekolah : {}\nAlamat : {},{},{},{}\nNPSN : -{}\nID : -{}".format(idx,mySchool[idx],myStreet[idx],myKecamatan[idx],myCity[idx],myProv[idx],myNpsn[idx],myId[idx]))