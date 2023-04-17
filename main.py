from flask import Flask,render_template
print("3 Contries of my choice: Thailand, Thaiwan and Turkey")
import bigmacdata
import currencydata
import restcountries

big_data  = bigmacdata.get_data()
general = restcountries.get_data()
print(general)

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("index.html", data = big_data, flag_th = general[0]["flag"],flag_tw = general[1]["flag"], flag_tu = general[2]["flag"],
                          pop_th = general[0]["population"],pop_tw = general[1]["population"], pop_tu = general[2]["population"],
                          lat_th = general[0]["latitude"],lat_tw = general[1]["latitude"], lat_tu = general[2]["latitude"],
                          lng_th = general[0]["longitude"],lng_tw = general[1]["longitude"], lng_tu = general[2]["longitude"],
                          mg_th = general[0]["map_g"],mg_tw = general[1]["map_g"], mg_tu = general[2]["map_g"],
                          mo_th = general[0]["map_o"],mo_tw = general[1]["map_o"], mo_tu = general[2]["map_o"], all = general)
@app.route('/gen')
def gen():
    
    return render_template("result.html",data = big_data, flag_th = general[0]["flag"])
  
app.run(host='0.0.0.0', port=81)