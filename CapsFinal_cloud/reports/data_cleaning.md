# Data Cleaning

# Overview

Tahap Data Cleaning dilakukan untuk memastikan bahwa seluruh video yang digunakan pada proses pelatihan model memiliki kualitas yang sesuai dengan kebutuhan penelitian.

Proses cleaning dilakukan setelah tahap Data Assessment dan sebelum proses ekstraksi landmark menggunakan MediaPipe.

---

# Cleaning Criteria

Video akan dipertahankan apabila memenuhi seluruh kriteria berikut:

* File dapat dibuka menggunakan OpenCV.
* File tidak kosong (0 byte).
* FPS valid (> 0).
* Jumlah frame valid (> 0).
* Durasi video berada pada rentang yang ditentukan.

Video yang tidak memenuhi kriteria tersebut akan dihapus dari dataset pelatihan.

---

# Cleaning Result

| Metric        | Value |
| ------------- | ----- |
| Total Files   | 5094  |
| Valid Files   | 3378  |
| Removed Files | 1716  |

Persentase data yang dipertahankan:

66.31%

Persentase data yang dihapus:

33.69%

---

# Removed Data Analysis

Data yang dihapus terdiri dari video yang tidak memenuhi standar kualitas dataset.

Alasan penghapusan meliputi:

* Empty File
* Cannot Open
* Invalid FPS
* Invalid Frame Count
* Duration Too Short
* Duration Too Long

Distribusi detail alasan penghapusan dapat dilihat pada file:

removed_files.csv

---

# Clean Dataset

Dataset hasil cleaning disimpan pada:

```text
dataset_clean/
```

Struktur folder dipertahankan sama dengan dataset awal untuk memudahkan proses ekstraksi landmark dan pelatihan model.

---

# Conclusion

Tahap Data Cleaning berhasil menghilangkan video yang tidak memenuhi standar kualitas sehingga dataset menjadi lebih konsisten dan siap digunakan pada tahap Dataset Validation dan Landmark Extraction.

Dataset hasil cleaning terdiri dari 3378 video valid yang siap digunakan untuk proses pengolahan lebih lanjut.
