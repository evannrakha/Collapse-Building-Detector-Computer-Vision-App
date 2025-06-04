# Collapse Building Detector Computer Vision App
App with interface about Computer Vision Project in Machine learning Detecting a Collapse Building with 3 Classes
 **pengecekan instalasi environment** sangat penting agar semuanya berjalan lancar. Berikut daftar pengecekan dan cara melakukannya:

---

## ✅ 1. **Cek Python Terinstall**

**Perintah (di terminal atau command prompt):**

```bash
python --version
```

atau jika di beberapa sistem:

```bash
python3 --version
```

✅ **Output yang diharapkan:**

```
Python 3.x.x
```

Jika belum terinstall, kamu bisa unduh Python dari: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## ✅ 2. **Cek pip Terinstall (Package Manager Python)**

**Perintah:**

```bash
pip --version
```

✅ **Output yang diharapkan:**

```
pip x.x.x from ... (python x.x)
```

Jika belum ada, biasanya pip terinstal bersama Python. Jika tidak, kamu bisa install dengan:

```bash
python -m ensurepip
```

---

## ✅ 3. **Cek Streamlit Terinstall**

**Perintah:**

```bash
streamlit --version
```

✅ **Output yang diharapkan:**

```
Streamlit x.x.x
```

❌ **Jika belum terinstall:**

```bash
pip install streamlit
```

---

## ✅ 4. **Cek Ultralytics Terinstall (YOLOv8/11)**

**Perintah:**

```bash
pip show ultralytics
```

✅ Jika muncul detail paket seperti:

```
Name: ultralytics
Version: 8.x.x
```

❌ Jika belum:

```bash
pip install ultralytics
```

---

## ✅ 5. **Cek OpenCV Terinstall**

**Perintah:**

```bash
python -c "import cv2; print(cv2.__version__)"
```

✅ Jika berhasil menampilkan versi OpenCV, berarti sudah siap.

❌ Jika belum:

```bash
pip install opencv-python
```

---

## 💡 Rangkuman Instalasi Minimal

Jika kamu ragu semua sudah terinstall, jalankan ini saja:

```bash
pip install streamlit ultralytics opencv-python
```

---

## 🚀 Setelah Semua Terpasang

Coba jalankan ini untuk memastikan environment siap:

```bash
streamlit hello
```

Jika Streamlit terbuka di browser, maka semuanya siap untuk lanjut ke pembuatan interface deteksi keruntuhan bangunan.

---

```bash
streamlit run app.py
```
