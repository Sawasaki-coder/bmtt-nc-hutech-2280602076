from flask import Flask, render_template, request
import subprocess
import sys

app = Flask(__name__)

# Trang chủ
@app.route("/")
def home():
    return render_template("index.html")

# --- Mở các ứng dụng GUI Qt từ nút web ---
@app.route("/launch/caesar", methods=["POST"])
def launch_caesar():
    subprocess.Popen([sys.executable, "lab-03/caesar_cipher.py"])
    return render_template("index.html")

@app.route("/launch/playfair", methods=["POST"])
def launch_playfair():
    subprocess.Popen([sys.executable, "lab-03/playfair_cipher.py"])
    return render_template("index.html")

@app.route("/launch/railfence", methods=["POST"])
def launch_railfence():
    subprocess.Popen([sys.executable, "lab-03/railfence_cipher.py"])
    return render_template("index.html")

@app.route("/launch/vigenere", methods=["POST"])
def launch_vigenere():
    subprocess.Popen([sys.executable, "lab-03/vigenere_cipher.py"])
    return render_template("index.html")

# MAIN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
