# ⛑️ Helmet Detection System using YOLOv8

![Project Architecture](https://raw.githubusercontent.com/hdyzute/Helmet-Detection/refs/heads/main/demo.png)

This project implements a helmet detection system using the **YOLOv8** object detection framework.  
The system can detect and classify two categories:
- **With Helmet**
- **Without Helmet**

It is designed for safety monitoring in environments such as construction sites, factories, traffic systems, and more.

---

## 🌟 Key Features

- **Fast & Lightweight Model:** Built with the YOLOv8 Nano (v8n) architecture for real-time inference.
- **Balanced Dataset:** Handles data imbalance using augmentation techniques.
- **High Accuracy:** Achieves **88.8% mAP@50** on validation data.
- **Interactive Web App:** A simple and intuitive **Streamlit** interface for image-based testing.

---

## 📂 Project Structure
```text
Project_Folder/
│
├── best.pt                 # Your trained YOLOv8 model (place it here)
├── app.py                  # Streamlit web application
├── requirements.txt        # Required Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 How to Run the Application

Follow the steps below to run the helmet detection web application.

### ✅ Step 1: Clone the Project (Optional)

If you are using Git:
```bash
git clone https://github.com/hdyzute/Helmet-Detection.git
cd helmet-detection
```

### ✅ Step 2: Install Python Dependencies

Make sure you have Python 3.8+ installed.
Then, open a terminal (or CMD) inside the project folder and run:
```bash
pip install -r requirements.txt
```

This will install:
- ultralytics (YOLOv8)
- streamlit
- opencv-python
- pillow
- numpy
- and other required packages.

### ✅ Step 3: Add the Model File

Place your trained YOLOv8 model file:
```bash
best.pt
```

directly into the project folder root (same directory as app.py).

**Note:** If this file is missing, the application will not run.

### ✅ Step 4: Launch the Web App

Run this command:
```bash
streamlit run app.py
```

After a few seconds, Streamlit will open the web app in your browser automatically (usually at):
```
http://localhost:8501
```

### ✅ Step 5: Use the Application

Inside the web interface:
1. Upload an image (JPEG/PNG).
2. The system will run YOLOv8 inference.
3. The output image will display bounding boxes with labels:
   - With Helmet
   - Without Helmet
4. You can test multiple images without restarting the app.

---

## 📌 Notes

- Make sure `best.pt` is placed in the correct directory.
- The model can be replaced with any YOLOv8 model trained on a similar dataset.
- If you encounter GPU issues, YOLO will fall back to CPU mode automatically.

---

## 🛠️ Training the Model (Optional)

If you want to retrain the model using YOLOv8:
```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

---

## 📜 License

This project is intended for educational and research purposes.
Feel free to modify or extend it for your own applications.
