from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok
import joblib

app = Flask(__name__)
model = joblib.load("model_ipm.model")

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/aplikasi')
def aplikasi():
    return render_template('aplikasi.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    Harapan_Lama_Sekolah = float(request.form['Harapan_Lama_Sekolah'])
    Pengeluaran_Perkapita = float(request.form['Pengeluaran_Perkapita'])
    Rerata_Lama_Sekolah = float(request.form['Rerata_Lama_Sekolah'])
    Usia_Harapan_Hidup = float(request.form['Usia_Harapan_Hidup'])

    prediction = model.predict([[Harapan_Lama_Sekolah, Pengeluaran_Perkapita, Rerata_Lama_Sekolah, Usia_Harapan_Hidup]])

    output = round(prediction[0], 2)

    if output >= 0.8:
        category = "Selamat, IPM berstatus very-high"
    elif output >= 0.7:
        category = "Selamat, IPM berstatus high"
    elif output >= 0.6:
        category = "Selamat dan tingkatkan, IPM berstatus normal"
    else:
        category = "Yah, status IPM low"

    if category == "Yah, status IPM low":
        img_url = "static/images/low.PNG"
        prediction_category = 0
    elif category == "Selamat dan tingkatkan, IPM berstatus normal":
        img_url = "static/images/normal.PNG"
        prediction_category = 1
    elif category == "Selamat, IPM berstatus high":
        img_url = "static/images/high.PNG"
        prediction_category = 2
    else:
        img_url = "static/images/very.PNG"
        prediction_category = 3

    prediction_text = f"{category}"
    return render_template('aplikasi.html', prediction_text=prediction_text,img_url=img_url)

if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()
