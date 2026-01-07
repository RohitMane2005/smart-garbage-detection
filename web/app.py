import os
import sys
import subprocess
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory


UPLOAD_FOLDER = "../uploads"
IMAGE_FOLDER = "../output_events/images"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def upload_video():
    if request.method == "POST":
        file = request.files["video"]
        filename = secure_filename(file.filename)

        video_path = os.path.abspath(
            os.path.join(app.config["UPLOAD_FOLDER"], filename)
        )
        file.save(video_path)

        subprocess.run([
            sys.executable,
            "../src/main.py",
            video_path
        ])

        return redirect(url_for("results"))

    return render_template("upload.html")


import os

@app.route("/results")
def results():
    if not os.path.exists(IMAGE_FOLDER):
        images = []
    else:
        images = [
            img for img in os.listdir(IMAGE_FOLDER)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

    return render_template("results.html", images=images)

@app.route("/images/<filename>")
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

# 🔴 THIS IS REQUIRED
if __name__ == "__main__":
    print("[INFO] Starting Flask server...")
    app.run(debug=True)
