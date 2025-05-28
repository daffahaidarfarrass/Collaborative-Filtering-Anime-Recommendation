# Laporan Proyek Machine Learning - Daffa Haidar Farras
## Project Overview
Dalam beberapa tahun terakhir, pertumbuhan platform hiburan penyedia film dan anime daring seperti MyAnimeList, Netflix, dan Bsation telah meningkatkan permintaan terhadap sistem rekomendasi yang cerdas dan personal. Sistem ini dirancang untuk membantu pengguna menemukan konten baru berdasarkan preferensi mereka. Salah satu pendekatan populer dalam membangun sistem rekomendasi adalah Collaborative Filtering (CF), yang menggunakan pola interaksi pengguna dengan item (dalam konteks ini, anime) untuk memprediksi preferensi pengguna lain.
## Business Understanding
### Problem Statements
- Bagaimana membangun sistem rekomendasi anime yang akurat dengan pendekatan klasik maupun modern untuk meningkatkan relevansi rekomendasi?
- Bagaimana membandingkan performa antara algoritma CF klasik berbasis KNN dan pendekatan Matrix Factorization (RecommenderNet)?
- Bagaimana model berbasis embedding dapat mengatasi masalah sparsity yang umum pada data rating pengguna?
### Goals
- Mengimplementasikan dua model rekomendasi—KNN Collaborative Filtering dan RecommenderNet TensorFlow—untuk memahami efisiensi dan efektivitas masing-masing.
- Mengukur performa kedua pendekatan menggunakan metrik evaluasi seperti RMSE, Precision@K, dan Recall.
- Menggunakan arsitektur embedding dalam RecommenderNet untuk menguji kemampuannya dalam menangani kasus data jarang dan item/ user baru.
### Solution Statement
- Menggunakan algoritma K-Nearest Neighbors berbasis kemiripan antar pengguna atau antar item. Algoritma ini sederhana namun efektif dalam konteks data yang cukup padat.
- Menggunakan embedding layer untuk merepresentasikan pengguna dan anime, serta dot product untuk mengukur kesamaan. Diterapkan dalam TensorFlow dengan BinaryCrossentropy sebagai fungsi loss.
- Melakukan evaluasi performa kedua model menggunakan metrik evaluasi standar dan melakukan hyperparameter tuning untuk meningkatkan akurasi model deep learning.
## Data Understanding
### Memeriksa duplicate value
### Memeriksa Missing Value
## Deskripsi Statistik dari Data
## Univariate Analysis
## Multivariate Analysis
## Data Preparation
### Data Spliting
## Modeling
## Evaluation
## Kesimpulan
## Referensi
