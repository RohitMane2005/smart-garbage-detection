import os
import sys
import subprocess
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")
IMAGE_FOLDER = os.path.join(BASE_DIR, "..", "output_events", "images")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)


def clear_old_results():
    for f in os.listdir(IMAGE_FOLDER):
        os.remove(os.path.join(IMAGE_FOLDER, f))


@app.route("/", methods=["GET", "POST"])
def upload_video():
    if request.method == "POST":
        clear_old_results()

        file = request.files["video"]
        filename = secure_filename(file.filename)
        video_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(video_path)

        subprocess.run([
            sys.executable,
            os.path.join(BASE_DIR, "..", "src", "main.py"),
            video_path
        ])

        return redirect(url_for("results"))

    return render_template("upload.html")


@app.route("/results")
def results():
    images = os.listdir(IMAGE_FOLDER)
    return render_template("results.html", images=images)


@app.route("/images/<filename>")
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)


if __name__ == "__main__":
    print("[INFO] Flask server started")
    app.run(debug=True)
