from flask import Flask, render_template, request
import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "video" not in request.files:
        return "No video selected."

    video = request.files["video"]

    if video.filename == "":
        return "No video selected."

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], video.filename)
    video.save(filepath)

    print("Uploaded:", filepath)

    detect_script = os.path.join(BASE_DIR, "detect.py")

    subprocess.run(
        [sys.executable, detect_script, filepath],
        check=True
    )

    # Open the detected video automatically
    output_video = os.path.join(BASE_DIR, "static", "output", "output.mp4")

    if os.path.exists(output_video):
        os.startfile(output_video)

    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)