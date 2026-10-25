from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)

# Project folders
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the trained AI model
model = YOLO("best.pt")


@app.route("/", methods=["GET", "POST"])
def index():
    result_image = None
    message = None

    if request.method == "POST":
        if "image" not in request.files:
            message = "Please select an image."
            return render_template(
                "index.html",
                result_image=result_image,
                message=message
            )

        file = request.files["image"]

        if file.filename == "":
            message = "Please select an image."
            return render_template(
                "index.html",
                result_image=result_image,
                message=message
            )

        # Accept common image formats
        allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}
        extension = os.path.splitext(file.filename)[1].lower()

        if extension not in allowed_extensions:
            message = "Please upload a JPG, JPEG, PNG, or WEBP image."
            return render_template(
                "index.html",
                result_image=result_image,
                message=message
            )

        # Save the uploaded image with a unique filename
        filename = f"{uuid.uuid4().hex}{extension}"
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(image_path)

        try:
            # Run AI inference
            results = model.predict(
                source=image_path,
                conf=0.25,
                save=False,
                verbose=False
            )

            result = results[0]

            # Save the image with detection boxes
            output_filename = f"detected_{filename.rsplit('.', 1)[0]}.jpg"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)

            result.save(filename=output_path)

            result_image = output_filename

            # Display detection count
            count = len(result.boxes)
            message = f"Analysis complete. Detected objects: {count}"

        except Exception as error:
            message = f"Error processing image: {error}"

    return render_template(
        "index.html",
        result_image=result_image,
        message=message
    )


@app.route("/outputs/<filename>")
def show_output(filename):
    from flask import send_from_directory
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)

