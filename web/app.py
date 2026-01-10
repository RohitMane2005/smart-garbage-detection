import os
import sys
import subprocess
import shutil
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
    if not os.path.exists(IMAGE_FOLDER):
        return

    for item in os.listdir(IMAGE_FOLDER):
        item_path = os.path.join(IMAGE_FOLDER, item)

        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(f"[WARN] Could not delete {item_path}: {e}")


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
