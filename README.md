# Laporan Proyek Machine Learning - Daffa Haidar Farras
## Project Overview
Dalam beberapa tahun terakhir, pertumbuhan platform hiburan penyedia film dan anime daring seperti MyAnimeList, Netflix, dan Bsation telah meningkatkan permintaan terhadap sistem rekomendasi yang cerdas dan personal. Sistem ini dirancang untuk membantu pengguna menemukan konten baru berdasarkan preferensi mereka. Salah satu pendekatan populer dalam membangun sistem rekomendasi adalah Collaborative Filtering (CF), yang menggunakan pola interaksi pengguna dengan item (dalam konteks ini, anime) untuk memprediksi preferensi pengguna lain.
## Business Understanding
### Problem Statements
- Bagaimana membangun sistem rekomendasi anime yang akurat dengan pendekatan klasik maupun modern untuk meningkatkan relevansi rekomendasi?
- Bagaimana membandingkan performa antara algoritma CF klasik berbasis LightFM dan Neural Collaborative Filtering (NCF)?
### Goals
- Mengimplementasikan dua model rekomendasi—LightFM Collaborative Filtering dan Neural Collaborative Filtering (NCF)—untuk memahami efisiensi dan efektivitas masing-masing.
- Mengukur performa kedua pendekatan menggunakan metrik evaluasi seperti Precision@K.
### Solution Statement
- Sistem rekomendasi anime akan dibangun dengan dua pendekatan utama yaitu, LightFM (Collaborative Filtering klasik) dan Neural Collaborative Filtering (NCF) berbasis deep learning.
- Evaluasi performa dilakukan dengan metrik Precision@K
## Data Understanding
Kumpulan data ini berisi informasi tentang data preferensi pengguna dari 73,516 pengguna pada 12,294 anime. Dataset ini diambil dari platform [Kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database) Dataset ini memiliki 2 file csv yaitu, anime.csv dan rating.csv
Struktur file nya
- anime.csv

| Kolom | Deskripsi |
|---|---|
| anime_id | myanimelist.net's unique id identifying an anime. |
|name | full name of anime.|
|genre | comma separated list of genres for this anime.|
|type | movie, TV, OVA, etc.|
|episodes | how many episodes in this show. (1 if movie).|
|rating | average rating out of 10 for this anime.|
|members | number of community members that are in this anime's "group".|
- rating.csv

| Kolom | Deskripsi |
|---|---|
|user_id | non identifiable randomly generated user id. |
|anime_id | the anime that this user has rated. |
|rating | rating out of 10 this user has assigned (-1 if the user watched it but didn't assign a rating). |

### Memeriksa duplicate value


Insight :
- Untuk data_movie tidak ditemukan duplikat data
- Tetapi, untuk data_rating terdapat 1 duplikat data

### Memeriksa Missing Value

Insight :
- Untuk data_movie ditemukan beberapa missing data
- Untuk data_rating tidak terdapat missing data
## Deskripsi Statistik dari Data

- Untuk data_rating
  
|	|user_id	|anime_id	|rating	|movieId|
|---|---|---|---|---|
|count	|7.813737e+06	|7.813737e+06	|7.813737e+06	|7.813737e+06|
|mean	|3.672796e+04	|8.909072e+03	|6.144030e+00	|8.909072e+03|
|std	|2.099795e+04	|8.883950e+03	|3.727800e+00	|8.883950e+03|
|min	|1.000000e+00	|1.000000e+00	|-1.000000e+00	|1.000000e+00|
|25%	|1.897400e+04	|1.240000e+03	|6.000000e+00	|1.240000e+03|
|50%	|3.679100e+04	|6.213000e+03	|7.000000e+00	|6.213000e+03|
|75%	|5.475700e+04	|1.409300e+04	|9.000000e+00	|1.409300e+04|
|max	|7.351600e+04	|3.451900e+04	|1.000000e+01	|3.451900e+04|

- Untuk data_movie
  
|	|user_id	|rating	|members	|movieId|
|---|---|---|---|---|
|count	|12294.000000	|12064.000000	|1.229400e+04	|12294.000000|
|mean	|14058.221653	|6.473902	|1.807134e+04	|14058.221653|
|std	|11455.294701	|1.026746	|5.482068e+04	|11455.294701|
|min	|1.000000	|1.670000	|5.000000e+00	|1.000000|
|25%	|3484.250000	|5.880000	|2.250000e+02	|3484.250000|
|50%	|10260.500000	|6.570000	|1.550000e+03	|10260.500000|
|75%	|24794.500000	|7.180000	|9.437000e+03	|24794.500000|
|max	|34527.000000	|10.000000	|1.013917e+06	|34527.000000|


## Univariate Analysis
### Distribusi Rating


Insight:
- Rating 10 mendominasi sebagai nilai paling sering diberikan, diikuti oleh rating 9 dan 8.
- Rating 0 juga sangat tinggi, kemungkinan besar karena mencerminkan anime yang ditambahkan ke daftar namun belum ditonton atau belum diberi rating oleh pengguna (missing rating).
- Distribusi ini tidak simetris dan sangat condong ke arah positif (skewed right), mengindikasikan adanya bias terhadap anime favorit atau populer.

## Multivariate Analysis
### Movie/Anime Populer


Insight:
- "Kimi no Na wa." dan "Ginga Eiyuu Densetsu" menempati posisi teratas dengan rating rata-rata di atas 8

### Genre Terpopuler


Insight:
- Genre "Comedy", "Action", dan "Adventure" merupakan tiga genre paling dominan dalam koleksi dataset.
- Genre seperti "Music", "Mecha", dan "Supernatural" memiliki jumlah yang lebih sedikit

## Data Preparation
### Data Spliting
## Modeling
## Evaluation
## Kesimpulan
## Referensi
