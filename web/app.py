from flask import Flask, render_template, url_for, redirect, request
import pickle
app = Flask(__name__)

# Load model Algoritma Genetika dari file .pkl
with open('model-pniel.pkl', 'rb') as file:
    model_genetika = pickle.load(file)

# Halaman utama
@app.route("/")
def index():
    return render_template("index.html")

# Halaman hasil
@app.route("/optimasi", methods=['POST'])
def optimasi():
    value = int(request.form['id_asrama'])
    list_asrama = ['Pniel', 'Antiokia', 'Kapernaum', 'Silo', 'Mambre', 'Mahanaim', 'Nazareth', 'Kana']

    # Pastikan model_genetika memiliki fungsi optimasi() untuk melakukan prediksi
    hasil_optimasi = model_genetika.optimasi(value)
    return render_template('result.html', nama_asrama=list_asrama[value])

if __name__ == "__main__":
    app.run(debug=True)
