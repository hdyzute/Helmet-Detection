import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

# --- Cấu hình trang ---
st.set_page_config(
    page_title="Helmet Detection App",
    page_icon="⛑️",
    layout="wide"
)

# --- Tải Model ---
# Đường dẫn chính xác đến model 'best.pt' của bạn
MODEL_PATH = 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\Helmet_yolo\\best.pt'

# Tải model (với cache để chạy nhanh hơn)
@st.cache_resource
def load_model(model_path):
    try:
        model = YOLO(model_path)
        return model
    except Exception as e:
        st.error(f"LỖI: Không thể tải model. Đảm bảo file 'best.pt' ở đúng đường dẫn: {model_path}")
        st.error(e)
        return None

model = load_model(MODEL_PATH)

# --- Giao diện Web ---
st.title("⛑️ Ứng dụng Nhận diện Mũ bảo hiểm")
st.write("Tải lên một ảnh để model YOLOv8 của bạn dự đoán.")

# --- Luồng xử lý ---
if model is not None:
    uploaded_file = st.file_uploader("Chọn một file ảnh", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # 1. Đọc file tải lên
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption='Ảnh gốc', use_column_width=True)

        # 2. Chạy dự đoán
        results = model(image)
        
        # 3. Lấy ảnh kết quả (đã vẽ bounding box)
        # results[0].plot() trả về một ảnh numpy (BGR)
        result_image_bgr = results[0].plot()
        
        # 4. Chuyển sang RGB (PIL cần RGB)
        result_image_rgb = Image.fromarray(result_image_bgr[...,::-1])
        
        with col2:
            st.image(result_image_rgb, caption='Ảnh kết quả', use_column_width=True)
        
        # 5. (Tùy chọn) Hiển thị thông tin chi tiết
        st.write("---")
st.subheader("Chi tiết dự đoán:")

# Lấy boxes từ kết quả
boxes = results[0].boxes

if boxes:
    # Tạo list chứa thông tin để hiển thị
    detections = []
    for box in boxes:
        # Lấy thông tin từng box
        class_id = int(box.cls[0])
        class_name = results[0].names[class_id]
        confidence = float(box.conf[0])
        
        detections.append({
            "Loại": class_name,
            "Độ tin cậy": f"{confidence:.2%}"
        })
    
    # Hiển thị dưới dạng bảng
    st.table(detections)
else:
    st.info("Không phát hiện đối tượng nào.")
