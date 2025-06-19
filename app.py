import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Konfigurasi halaman
st.set_page_config(page_title="Deteksi Risiko Dropout Mahasiswa", layout="wide")
st.title("🎓 Sistem Deteksi Risiko Dropout Mahasiswa")

# Load model dan scaler
model = joblib.load("model_dropout.pkl")
scaler = joblib.load("scaler_dropout.pkl")

# --- Input Form ---
st.subheader("📥 Masukkan Data Mahasiswa")
with st.form(key='predict_form'):
    age = st.number_input("Usia saat Masuk", min_value=17, max_value=70, value=18)

    avg_grade = st.slider(
        "Rata-rata Nilai Semester",
        min_value=0.00,
        max_value=18.00,
        value=10.00,
        step=0.01,
        format="%.2f"
    )

    approved_courses = st.number_input(
        "Jumlah Mata Kuliah yang Lulus",
        min_value=0,
        max_value=40,
        value=0
    )

    submit = st.form_submit_button("🔍 Prediksi")

# --- Proses Prediksi ---
if submit:
    # Buat DataFrame dari input
    X_input = pd.DataFrame({
        'avg_semester_grade': [avg_grade],
        'Age_at_enrollment': [age],
        'total_courses_approved': [approved_courses]
    })

    # Normalisasi fitur
    X_scaled = scaler.transform(X_input)

    # Prediksi probabilitas
    proba = model.predict_proba(X_scaled)[0]
    labels = model.classes_
    label_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    pred_index = np.argmax(proba)
    predicted_status = label_map[pred_index]

    # --- Tampilkan Hasil ---
    st.subheader("📊 Probabilitas Prediksi")
    prob_dict = {label_map[i]: round(prob, 2) for i, prob in enumerate(proba)}
    st.json(prob_dict)

    st.subheader("✅ Hasil Prediksi Status Mahasiswa")
    st.success(f"Mahasiswa ini diprediksi: **{predicted_status}**")

    # --- Saran & Intervensi ---
    st.subheader("💡 Rekomendasi Intervensi dan Solusi")

    if predicted_status == "Dropout":
        st.error("⚠️ Mahasiswa ini berisiko tinggi untuk *Dropout*.")
        st.markdown("""
        **Saran untuk Institut:**
        - Jadwalkan sesi konseling akademik dan psikologis secara berkala.
        - Berikan tutor atau mentor sebaya (peer-mentoring).
        - Tawarkan program beasiswa atau bantuan biaya kuliah.
        - Periksa dan bantu penyelesaian masalah administrasi (utang, kehadiran).
        - Lakukan pemantauan berkala terhadap kemajuan studi.
        """)
    elif predicted_status == "Enrolled":
        st.warning("ℹ️ Mahasiswa ini masih *terdaftar* dan bisa berisiko jika tidak dibimbing.")
        st.markdown("""
        **Saran untuk Institut:**
        - Pastikan mahasiswa memiliki rencana studi yang jelas.
        - Evaluasi motivasi dan hambatan belajar.
        - Dorong partisipasi aktif dalam kegiatan akademik dan sosial.
        - Lakukan monitoring perkembangan akademik per semester.
        """)
    elif predicted_status == "Graduate":
        st.success("🎉 Mahasiswa ini diprediksi akan *Lulus*.")
        st.markdown("""
        **Saran untuk Institut:**
        - Berikan dukungan untuk persiapan tugas akhir atau skripsi.
        - Sediakan akses ke pelatihan karir dan job fair.
        - Dokumentasikan praktik baik agar bisa diterapkan pada mahasiswa lain.
        """)

