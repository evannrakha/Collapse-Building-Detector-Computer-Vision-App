import streamlit as st
import tempfile
import os
from ultralytics import YOLO
import cv2
from PIL import Image

# Load YOLOv11 model
model = YOLO("best.pt")  # Ganti dengan path modelmu

st.title("🧱 Collapse Detection dengan YOLOv11")
st.write("Upload gambar atau video bangunan, sistem akan mendeteksi keruntuhan.")

option = st.radio("Pilih jenis input:", ["Gambar", "Video"])

if option == "Gambar":
    uploaded_image = st.file_uploader("Upload Gambar", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, caption="Gambar yang diunggah", use_column_width=True)

        with st.spinner("🔍 Mendeteksi..."):
            results = model.predict(image, save=False, conf=0.4)
            result_image = results[0].plot()
            st.image(result_image, caption="🧠 Hasil Deteksi", use_column_width=True)

elif option == "Video":
    uploaded_video = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded_video.read())
        tfile_path = tfile.name

        st.video(tfile_path)

        if st.button("Jalankan Deteksi"):
            st.info("⏳ Sedang memproses video...")

            cap = cv2.VideoCapture(tfile_path)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            # Simpan hasil output ke file output.mp4
            output_path = os.path.join(os.getcwd(), "output.mp4")
            out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            progress = st.progress(0)

            frame_idx = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                results = model.predict(frame, save=False, conf=0.4)
                result_frame = results[0].plot()
                out.write(result_frame)

                frame_idx += 1
                progress.progress(min(frame_idx / frame_count, 1.0))

            cap.release()
            out.release()

            st.success("✅ Deteksi selesai!")

            # Tampilkan tombol download
            with open(output_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Hasil Video Deteksi",
                    data=f,
                    file_name="hasil_deteksi.mp4",
                    mime="video/mp4"
                )
