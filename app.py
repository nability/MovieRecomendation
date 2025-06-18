from flask import Flask, request, render_template
import google.generativeai as genai
import markdown 
# Masukkan API Key Gemini
genai.configure(api_key="AIzaSyAKVznqz9WIWEBpeEW5b3mX02q2QSi0BS0")

app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        Genre = request.form['Genre']
        Umur = request.form['Umur']
        Produksi = request.form['Produksi']

        prompt = (
    f"Berikan 10 rekomendasi film populer yang sesuai dengan kriteria berikut:\n"
    f"- Genre: {Genre}\n"
    f"- Kategori usia penonton: {Umur}\n"
    f"- Asal produksi: {Produksi}\n\n"
    f"Tampilkan hasil dengan format berikut untuk masing-masing film:\n"
    f"1. Judul: [judul film]\n"
    f"   Deskripsi: [deskripsi singkat film, maksimal 2 kalimat]\n"
    f"   Rating IMDb: [nilai rating IMDb aktual atau estimasi jika tidak tersedia]\n\n"
    f"Hanya tampilkan daftar film tanpa penjelasan tambahan."
)


        response = model.generate_content(prompt)
        reply_raw = response.text
        reply = markdown.markdown(reply_raw)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
