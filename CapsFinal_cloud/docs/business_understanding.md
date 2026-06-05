# Business Understanding

## Latar Belakang

Akses terhadap layanan perbankan merupakan hak setiap individu, termasuk penyandang disabilitas Tuli. Namun, dalam praktiknya masih terdapat hambatan komunikasi antara nasabah Tuli dan petugas bank, terutama saat membahas produk dan layanan keuangan yang menggunakan istilah khusus.

Keterbatasan komunikasi tersebut dapat menyebabkan kesalahpahaman informasi, menurunkan kualitas layanan, serta menghambat inklusi keuangan bagi komunitas Tuli. Oleh karena itu, diperlukan solusi teknologi yang mampu menjembatani komunikasi secara efektif dan mudah digunakan.

SignBank AI dikembangkan sebagai sistem penerjemah bahasa isyarat berbasis Artificial Intelligence yang mampu mengenali gesture bahasa isyarat terkait layanan perbankan secara real-time dan menerjemahkannya menjadi teks yang dapat dipahami oleh petugas bank maupun nasabah.

## Permasalahan Bisnis

1. Nasabah Tuli mengalami kesulitan menyampaikan kebutuhan layanan perbankan kepada petugas bank.
2. Tidak semua petugas bank memahami Bahasa Isyarat Indonesia (BISINDO).
3. Komunikasi yang tidak efektif dapat meningkatkan risiko miskomunikasi terkait informasi keuangan.
4. Belum tersedia solusi penerjemah bahasa isyarat khusus untuk konteks layanan perbankan.

## Tujuan Proyek

Mengembangkan sistem pengenalan gesture bahasa isyarat berbasis Computer Vision yang mampu menerjemahkan istilah perbankan secara real-time sehingga dapat meningkatkan aksesibilitas dan kualitas komunikasi dalam layanan perbankan.

## Target Pengguna

* Nasabah Tuli
* Petugas layanan bank
* Institusi perbankan yang ingin meningkatkan layanan inklusif

## Solusi yang Diusulkan

Sistem SignBank AI menggunakan kamera untuk menangkap gerakan tangan pengguna. Gesture yang terdeteksi akan diproses menggunakan MediaPipe dan model Machine Learning untuk menghasilkan teks terjemahan yang sesuai dengan istilah perbankan.

## Success Metrics

Keberhasilan proyek diukur menggunakan beberapa indikator berikut:

* Akurasi klasifikasi gesture ≥ 90%
* Precision ≥ 90%
* Recall ≥ 90%
* F1-Score ≥ 90%
* Latensi prediksi realtime < 1 detik
* Seluruh kelas gesture perbankan dapat dikenali oleh sistem

## Ruang Lingkup

Proyek hanya berfokus pada:

* Pengenalan gesture tangan menggunakan kamera.
* Penerjemahan gesture menjadi teks.
* Istilah perbankan yang telah ditentukan dalam dataset.

Proyek tidak mencakup:

* Eksekusi transaksi perbankan.
* Integrasi langsung dengan core banking system.
* Deteksi ekspresi wajah.
* Pemrosesan kalimat kompleks.
* Aplikasi mobile native.
