# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Latar BelakangJaya Jaya Institut mengalami permasalahan jumlah dropout mahasiswa yang cukup tinggi. Hal ini berdampak pada reputasi lembaga, efisiensi anggaran, dan kualitas lulusan.

### Permasalahan Bisnis

Fitur apa yang paling mempengaruhi risiko dropout?

Siapa mahasiswa yang harus diprioritaskan intervensinya?

Bagaimana estimasi risiko dropout per mahasiswa?

### Cakupan Proyek

Membuat model prediksi untuk mendeteksi mahasiswa yang berisiko dropout agar intervensi akademik bisa dilakukan lebih awal.

### Persiapan

Sumber data: "postgresql://postgres.sstitmkpsttbamcrrvvc:root123@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

Setup environment:
```
1. Buka terminal atau PowerShell.

2. Jalankan perintah berikut.

conda create --name students_performance python=3.11

3. Aktifkan virtual environment dengan menjalankan perintah berikut.

conda activate students_performance

4. Instal semua library yang dibutuhkan menggunakan perintah berikut.

pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn==1.2.2 joblib==1.3.1

5.Buka jupyter-notebook dengan menjalankan perintah berikut.

jupyter-notebook .
```

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Latar BelakangJaya Jaya Institut mengalami permasalahan jumlah dropout mahasiswa yang cukup tinggi. Hal ini berdampak pada reputasi lembaga, efisiensi anggaran, dan kualitas lulusan.

### Permasalahan Bisnis

Fitur apa yang paling mempengaruhi risiko dropout?

Siapa mahasiswa yang harus diprioritaskan intervensinya?

Bagaimana estimasi risiko dropout per mahasiswa?

### Cakupan Proyek

Membuat model prediksi untuk mendeteksi mahasiswa yang berisiko dropout agar intervensi akademik bisa dilakukan lebih awal.


## Menjalankan Sistem Machine Learning
Berikut langkah-langkah untuk menjalankan prototipe sistem deteksi risiko dropout mahasiswa yang telah dikembangkan:

```
1. Siapkan Lingkungan Virtual
Pastikan semua dependensi tersedia. Jalankan perintah:
pip install -r requirements.txt

2. Jalankan Aplikasi Streamlit
Gunakan perintah:
streamlit run app.py

3. Antarmuka Pengguna
Setelah dijalankan, sistem dapat diakses melalui browser pada alamat: http://localhost:8501
Link prototipe online :

4. Proses Prediksi

Masukkan informasi dasar mahasiswa (usia, nilai rata-rata, mata kuliah lulus).

Klik tombol “🔍 Prediksi”.

Sistem akan menampilkan prediksi status mahasiswa serta saran intervensi berdasarkan hasil prediksi.

Link prototipe online : https://billyelridho-students-performance.streamlit.app/
```

## Conclusion

Proyek ini berhasil membangun sistem deteksi risiko dropout mahasiswa menggunakan algoritma machine learning berbasis CatBoost Classifier dengan akurasi prediksi sekitar 70–75%.

Model memanfaatkan kombinasi fitur akademik (seperti rata-rata nilai semester dan jumlah mata kuliah yang disetujui) serta karakteristik pribadi (seperti usia saat masuk kuliah). Sistem ini memberikan:

- Prediksi status mahasiswa: Dropout / Enrolled / Graduate
- Probabilitas untuk masing-masing label
- Rekomendasi intervensi untuk institusi

Faktor-Faktor yang Berpengaruh terhadap Dropout:

- Average Grade: Mahasiswa dengan nilai rata-rata rendah memiliki risiko dropout yang jauh lebih tinggi. Ini adalah indikator kinerja akademik utama.

- Curricular Units Failed: Semakin banyak mata kuliah yang gagal, semakin besar kemungkinan mahasiswa tersebut akan dropout.

- Age at Enrollment: Mahasiswa yang masuk kuliah di usia lebih tua dari rata-rata juga lebih berisiko.

Karakteristik Mahasiswa yang Rentan Dropout:
- Memiliki rata-rata nilai semester rendah (< 12).
- Telah gagal di beberapa mata kuliah (lebih dari 2).
- Memiliki status debitur aktif.
- Masuk kuliah pada usia di atas 22 tahun.

Manfaat Sistem:
- Identifikasi Dini: Sistem ini mampu mengklasifikasikan mahasiswa berdasarkan probabilitas dropout dengan cukup akurat.

- Intervensi yang Tepat: Memberikan informasi bagi pihak akademik untuk memprioritaskan perhatian kepada mahasiswa yang memiliki risiko tinggi.

- Rekomendasi Personalisasi: Institusi dapat menyesuaikan strategi intervensi berdasarkan faktor dominan penyebab dropout per mahasiswa.

Dengan demikian, dashboard dan model yang dibangun dapat menjadi alat bantu yang efektif untuk menekan angka dropout, meningkatkan retensi mahasiswa, dan pada akhirnya menjaga reputasi serta efisiensi operasional institusi.

### Rekomendasi Action Items

1. Mahasiswa yang yang Hasil Prediksinya Dropout
    - Jadwalkan sesi konseling akademik dan psikologis secara berkala.
    - Berikan tutor atau mentor sebaya (peer-mentoring).
    - Tawarkan program beasiswa atau bantuan biaya kuliah.
    - Periksa dan bantu penyelesaian masalah administrasi (utang, kehadiran).
    - Lakukan pemantauan berkala terhadap kemajuan studi.

2. Mahasiswa yang yang Hasil Prediksinya Enrolled
    - Pastikan mahasiswa memiliki rencana studi yang jelas.
    - Evaluasi motivasi dan hambatan belajar.
    - Dorong partisipasi aktif dalam kegiatan akademik dan sosial.
    - Lakukan monitoring perkembangan akademik per semester.

3. Mahasiswa yang yang Hasil Prediksinya Graduate

    - Berikan dukungan untuk persiapan tugas akhir atau skripsi.
    - Sediakan akses ke pelatihan karir dan job fair.
    - Dokumentasikan praktik baik agar bisa diterapkan pada mahasiswa lain.