# Conclusion

## Ringkasan Proyek

SignBank AI dikembangkan sebagai solusi untuk membantu komunikasi antara nasabah Tuli dan petugas bank melalui penerjemahan bahasa isyarat perbankan menjadi teks secara otomatis. Tahap Data Science pada proyek ini berfokus pada pengumpulan, validasi, transformasi, dan persiapan dataset agar siap digunakan dalam proses pelatihan model machine learning.

Dataset yang digunakan merupakan dataset primer yang dikumpulkan secara mandiri oleh enam kontributor dengan variasi latar belakang, pencahayaan, dan sudut pengambilan video untuk meningkatkan keragaman data.

---

## Hasil Data Gathering

Proses pengumpulan data menghasilkan:

| Komponen     | Nilai     |
| ------------ | --------- |
| Total Kelas  | 49        |
| Total Video  | 5094      |
| Kontributor  | 6 Orang   |
| Format Video | MP4       |
| Resolusi     | 512 × 512 |
| FPS          | 30        |
| Durasi Video | 2–5 Detik |

Dataset mencakup gesture alfabet, angka, istilah perbankan, dan istilah keuangan yang relevan dengan kebutuhan komunikasi dalam layanan perbankan.

---

## Hasil Data Cleaning dan Validation

Tahap Data Cleaning berhasil mengidentifikasi dan menghapus data yang tidak memenuhi standar kualitas.

Selanjutnya, proses Dataset Validation menunjukkan bahwa dataset memiliki kualitas yang baik dan layak digunakan untuk proses pelatihan model.

Hasil validasi menunjukkan:

| Metrik                   | Nilai |
| ------------------------ | ----- |
| Total Labels             | 49    |
| Total Videos             | 5094  |
| Minimum Sampel per Kelas | 100   |
| Maximum Sampel per Kelas | 154   |
| Imbalance Ratio          | 1.54  |
| Dataset Status           | VALID |

Distribusi data yang relatif seimbang menunjukkan bahwa dataset tidak mengalami class imbalance yang signifikan.

---

## Hasil Feature Engineering

Feature engineering dilakukan menggunakan MediaPipe Hands untuk mengekstraksi landmark tangan dari setiap video.

Fitur yang digunakan terdiri dari:

| Jenis Fitur          | Jumlah |
| -------------------- | ------ |
| Landmark Coordinates | 126    |
| Angle Features       | 15     |
| Total Features       | 141    |

Setiap video kemudian dinormalisasi menjadi sequence sepanjang 40 frame sehingga seluruh sampel memiliki ukuran input yang seragam.

Representasi akhir setiap video adalah:

```text
(40, 141)
```

Tahap ekstraksi berhasil memproses seluruh video tanpa kegagalan.

| Metrik               | Nilai |
| -------------------- | ----- |
| Total Video Diproses | 5094  |
| Success Files        | 5094  |
| Failed Files         | 0     |
| Success Rate         | 100%  |

---

## Jawaban Pertanyaan Bisnis

### 1. Seberapa akurat SignBank AI dalam menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time?

Pertanyaan ini belum dapat dijawab pada tahap Data Science karena proses pelatihan dan evaluasi model belum dilakukan.

Namun, seluruh dataset telah berhasil dipersiapkan dalam bentuk representasi numerik yang siap digunakan untuk pelatihan model klasifikasi gesture. Evaluasi terhadap akurasi sistem akan dilakukan pada tahap pemodelan menggunakan metrik Accuracy, Precision, Recall, F1-Score, dan Confusion Matrix.

---

### 2. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Pertanyaan ini juga belum dapat dijawab secara kuantitatif karena model belum melalui proses pelatihan dan pengujian.

Meskipun demikian, hasil Data Wrangling, Dataset Validation, dan Feature Engineering menunjukkan bahwa dataset yang digunakan memiliki kualitas yang baik, distribusi yang relatif seimbang, serta representasi fitur yang informatif untuk mendukung proses pengenalan gesture bahasa isyarat perbankan.

---

## Kesimpulan Akhir

Seluruh tahapan Data Science sebelum pemodelan telah berhasil diselesaikan, meliputi Business Understanding, Data Gathering, Data Assessment, Data Cleaning, Dataset Validation, Landmark Extraction, Feature Engineering, dan Dataset Preparation.

Hasil akhir berupa dataset siap latih dengan total 5094 sampel, 49 kelas gesture, dan representasi fitur berukuran (40, 141). Dataset ini telah memenuhi kebutuhan untuk tahap pelatihan model Long Short-Term Memory (LSTM) yang akan digunakan untuk mengenali dan menerjemahkan bahasa isyarat perbankan secara otomatis.

Tahap berikutnya adalah proses pelatihan, evaluasi, dan pengujian model untuk mengukur tingkat akurasi sistem serta kemampuan SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank.

### Catatan Jumlah Kelas ###

Pada tahap perencanaan awal, dataset dirancang terdiri dari 50 kelas gesture yang mencakup alfabet, angka, istilah perbankan, dan istilah keuangan.

Hasil validasi menunjukkan bahwa dataset akhir terdiri dari 49 kelas. Setelah dilakukan pemeriksaan terhadap label yang tersedia, ditemukan bahwa gesture huruf "F" tidak terdapat pada dataset akhir sehingga tidak ikut diproses pada tahap ekstraksi fitur dan persiapan dataset.

Akibatnya, jumlah kelas yang digunakan dalam penelitian menjadi 49 kelas. Meskipun demikian, seluruh kelas yang tersedia memiliki jumlah sampel yang memadai dengan minimum 100 sampel per kelas dan distribusi yang relatif seimbang, sehingga dataset tetap layak digunakan untuk proses pelatihan model.