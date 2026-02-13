import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from flask import Flask, render_template, request
print("import success")

model_rf_MU = pickle.load(open('../flaskapp/ML model/model_rf_MU.pkl', 'rb'))

print("models loaded success")

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        print("страница в разработке")

        sootnoshenie = request.form['sootnoshenie']
        plotnost = request.form['plotnost']
        modul_upr = request.form['modul_upr']
        kol_otverd = request.form['kol_otverd']
        soder_e_g = request.form['soder_e_g']
        temp_vsp = request.form['temp_vsp']
        pover_plotnost = request.form['pover_plotnost']
        potreb_smol = request.form['potreb_smol']
        ugol = request.form['ugol']
        shag = request.form['shag']
        plotnost_nash = request.form['plotnost_nash']

        x = [sootnoshenie, plotnost, modul_upr, kol_otverd, soder_e_g, temp_vsp, pover_plotnost, potreb_smol, ugol, shag, plotnost_nash]
        predict_Y = model_rf_MU.predict([x])

        return render_template('result.html', result=predict_Y)




if __name__=='__main__':
    app.run(debug=True)
