from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    listWilayah = requests.get("http://jendela.data.kemdikbud.go.id/api/index.php/cwilayah/wilayahKabGet")
    daftarWilayah = listWilayah.json()
    if request.method == 'POST':
        namaKota = request.form['namaKota']
        strata = request.form['strata']
        detailSekolah = requests.get("http://jendela.data.kemdikbud.go.id/api/index.php/Csekolah/detailSekolahGET?mst_kode_wilayah={}&bentuk={}".format(namaKota,strata))
        dataSekolah = detailSekolah.json()
        return render_template('detail.html',dataSekolah=dataSekolah)
    return render_template('index.html',daftarWilayah=daftarWilayah)

@app.route('/detail/<kode>/<strata>/<namaSekolah>')
def detailSekolah(kode,strata,namaSekolah):
    detailSekolah = requests.get("http://jendela.data.kemdikbud.go.id/api/index.php/Csekolah/detailSekolahGET?mst_kode_wilayah={}&bentuk={}".format(kode,strata))
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

    if namaSekolah in mySchool:
        idx = mySchool.index(namaSekolah)
        data = []
        data.append((mySchool[idx],myStreet[idx],myKecamatan[idx],myCity[idx],myProv[idx],myNpsn[idx],myId[idx]))

    return render_template('detailSekolah.html',data=data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 