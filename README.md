# AI-Based Pothole Detection System
An AI-based web application designed to detect potholes in road images using a YOLO object detection model. The application provides a simple web interface where users can upload an image and view the model's prediction with detection annotations.

## 📌 Project Overview
Potholes can contribute to road accidents, vehicle damage, and unsafe driving conditions. This project explores how computer vision can assist in identifying potential potholes from road images.
The application uses a trained YOLO model for image prediction and Flask to provide a web interface.

> **Note:** This is an academic prototype. Detection accuracy and real-world reliability must be evaluated using suitable test images before practical deployment.

## ✨ Features
* Upload road images through a web interface.
* Run object detection using a YOLO model.
* Display the prediction result as an annotated image.
* Show the number of detections returned by the model.
* Simple and user-friendly interface.
* Local execution using Flask.

## 🛠️ Technologies Used
* **Python** — application logic
* **Flask** — web framework
* **YOLO / Ultralytics** — object detection
* **OpenCV** — image processing
* **HTML and CSS** — user interface

## 📁 Project Structure
PATHOLE/
│
├── app.py
├── best.pt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── uploads/
│   └── .gitkeep
│
└── outputs/
    └── .gitkeep


**Important:** The trained model file `best.pt` is excluded from this GitHub repository because of the `.gitignore` configuration. You must obtain the model file separately and place it in the project root before running the application.

## ⚙️ Requirements
* Python installed on your computer
* pip package manager
* The project's trained YOLO model file (`best.pt`)
* An internet connection for installing the required packages

## 🚀 Installation and Setup

### 1. Clone the repository
git clone https://github.com/sanketsonkamble35-coder/AI-Based-Pothole-Detection.git


### 2. Open the project directory
cd AI-Based-Pothole-Detection


### 3. Create a virtual environment (recommended)
```bash
python -m venv .venv
```

Activate it on Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, you can install and run packages using the Python interpreter in the virtual environment directly, without changing your system execution policy.

### 4. Install dependencies
```bash
python -m pip install flask ultralytics opencv-python
```

### 5. Add the trained model
Place your `best.pt` file in the project's root directory, alongside `app.py`.
The model file is not included in this repository. Only use a model that you have permission to use and distribute.

### 6. Run the application
```bash
python app.py
```

### 7. Open the web application
Open your browser and visit:
http://127.0.0.1:5000
Upload a road image and click the analysis button to view the prediction result.

## 🔍 How It Works
1. The user uploads a road image.
2. The Flask application receives and saves the image.
3. The YOLO model processes the image and generates predictions.
4. The application saves the annotated prediction image.
5. The web page displays the result and detection count.

## 🧪 Testing
Test the application with different road images, including images with visible potholes and images without potholes.
Evaluate the predictions manually to identify false positives and missed potholes. Do not assume that every prediction is correct.

## ⚠️ Limitations
* Detection performance depends on the quality and training data of the model.
* Lighting, shadows, road surfaces, image quality, and camera angles may affect predictions.
* The model's class labels and accuracy should be verified before relying on its results.
* This prototype has not been established as suitable for real-time road monitoring or safety-critical use.

## 🔮 Future Improvements
* Evaluate and document model accuracy using a labeled test dataset.
* Verify and display meaningful class names.
* Add webcam or video-based detection.
* Improve the interface for mobile devices.
* Add detection history and result downloads.
* Explore real-time road monitoring after appropriate testing.

## 👨‍💻 Author
**Sanket Sonkamble**
* GitHub: [sanketsonkamble35-coder](https://github.com/sanketsonkamble35-coder)

## 📄 License
A license has not yet been specified for this project. Check the license and redistribution terms of the trained model before sharing it. Add an appropriate project license if you intend to permit others to reuse your code.
