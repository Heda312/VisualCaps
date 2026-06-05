# Problem Statement

## Latar Belakang

Nasabah Tuli masih menghadapi berbagai hambatan komunikasi ketika mengakses layanan perbankan. Keterbatasan kemampuan komunikasi antara nasabah Tuli dan petugas bank dapat menyebabkan kesulitan dalam menyampaikan kebutuhan layanan, memahami informasi keuangan, serta meningkatkan risiko terjadinya miskomunikasi.

Perkembangan teknologi Artificial Intelligence dan Computer Vision memungkinkan pengembangan sistem penerjemah bahasa isyarat secara otomatis. Oleh karena itu, SignBank AI dikembangkan sebagai sistem yang mampu mengenali dan menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time untuk mendukung komunikasi yang lebih inklusif.

## Problem Statement

Bagaimana mengembangkan sistem penerjemah bahasa isyarat perbankan berbasis Artificial Intelligence yang mampu mengenali gesture secara akurat dan mendukung komunikasi antara nasabah Tuli dan petugas bank secara real-time?

## Business Questions

### 1. Seberapa akurat SignBank AI dalam menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time?

Pertanyaan ini digunakan untuk mengukur kemampuan model dalam mengenali dan mengklasifikasikan gesture bahasa isyarat perbankan dengan benar.

Indikator yang digunakan:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

### 2. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Pertanyaan ini digunakan untuk mengevaluasi sejauh mana hasil prediksi model dapat digunakan sebagai media pendukung komunikasi pada konteks layanan perbankan.

Indikator yang digunakan:

* Tingkat keberhasilan klasifikasi gesture
* Konsistensi hasil prediksi
* Analisis kesalahan klasifikasi
* Confusion Matrix

---

### 3. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Pertanyaan ini digunakan untuk menganalisis hasil implementasi model terhadap kebutuhan komunikasi dalam skenario layanan perbankan serta mengidentifikasi keterbatasan yang masih perlu ditingkatkan.

Indikator yang digunakan:

* Accuracy
* Precision
* Recall
* F1-Score
* Analisis kelas yang sering salah diprediksi
* Analisis hasil evaluasi model

## Analytical Goals

Untuk menjawab pertanyaan bisnis yang telah ditentukan, analisis dilakukan dengan tujuan:

1. Mengukur tingkat akurasi model dalam menerjemahkan bahasa isyarat perbankan menjadi teks.
2. Mengevaluasi performa model menggunakan berbagai metrik klasifikasi.
3. Mengidentifikasi gesture yang mudah dan sulit dikenali oleh model.
4. Menganalisis kesalahan prediksi yang terjadi selama proses pengujian.
5. Memberikan rekomendasi perbaikan model dan dataset untuk meningkatkan performa sistem.

## Success Metrics

Keberhasilan proyek diukur menggunakan indikator berikut:

* Accuracy ≥ 90%
* Precision ≥ 90%
* Recall ≥ 90%
* F1-Score ≥ 90%
* Sistem mampu melakukan prediksi secara real-time
* Seluruh kelas gesture dapat dikenali oleh model dengan performa yang konsisten
