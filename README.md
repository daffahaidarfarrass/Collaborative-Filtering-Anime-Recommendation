# Laporan Proyek Machine Learning - Daffa Haidar Farras
## Project Overview
  Seiring pertumbuhan eksponensial konten hiburan digital, seperti film dan anime, pengguna semakin kesulitan menemukan tayangan yang relevan dan sesuai minat. Platform seperti Netflix, Crunchyroll, dan MyAnimeList menghadapi tantangan besar dalam mengelola dan merekomendasikan ribuan judul kepada jutaan pengguna [1]. Oleh karena itu, pengembangan sistem rekomendasi cerdas menjadi sangat penting untuk meningkatkan pengalaman pengguna dan efisiensi dalam menjelajahi konten.<br><br>
  Metode Collaborative Filtering (CF) telah menjadi pendekatan utama dalam sistem rekomendasi, yang memanfaatkan kesamaan antar pengguna atau item berdasarkan histori interaksi mereka. Meskipun efektif, CF klasik memiliki kelemahan seperti cold-start problem dan kesulitan menangani data spars [2]. Untuk mengatasi keterbatasan ini, pada projek ini menggunakan pendekatan seperti LightFM, yang melakukan collaborative filtering, serta Neural Collaborative Filtering (NCF), yang menggunakan jaringan saraf untuk memodelkan interaksi pengguna dan item secara lebih kompleks dan non-linear.

## Business Understanding
### Problem Statements
- Bagaimana membangun sistem rekomendasi movie (anime) yang akurat dengan pendekatan klasik maupun modern untuk meningkatkan relevansi rekomendasi?
- Bagaimana membandingkan performa antara algoritma CF klasik berbasis LightFM dan Neural Collaborative Filtering (NCF)?
### Goals
- Mengimplementasikan dua model rekomendasi—LightFM Collaborative Filtering dan Neural Collaborative Filtering (NCF)—untuk memahami efisiensi dan efektivitas masing-masing.
- Mengukur performa kedua pendekatan menggunakan metrik evaluasi seperti Precision@K.
### Solution Statement
- Sistem rekomendasi anime akan dibangun dengan dua pendekatan utama yaitu, LightFM (Collaborative Filtering klasik) dan Neural Collaborative Filtering (NCF) berbasis deep learning.
- Evaluasi performa dilakukan dengan metrik Precision@K dan Recall@K
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

- Pada **anime.csv** ini memiliki

|Jumlah Baris|Jumlah Kolom|
|---|---|
|12.294|8|


- rating.csv

| Kolom | Deskripsi |
|---|---|
|user_id | non identifiable randomly generated user id. |
|anime_id | the anime that this user has rated. |
|rating | rating out of 10 this user has assigned (-1 if the user watched it but didn't assign a rating). |

 - Pada **rating.csv** ini memiliki

|Jumlah Baris|Jumlah Kolom|
|---|---|
|7.813.737|4|

### Data Unique untuk `anime_id` dan `user_id`
- Terdapat 12,294 data unik di kolom `anime_id`
- Terdapat 73,515 data unik di kolom `user_id`



### Memeriksa duplicate value

![Cek Duplikat](https://github.com/user-attachments/assets/8bcfd72a-87ed-4fdd-9f75-50c42ea39526)



Insight :
- Untuk data_movie tidak ditemukan duplikat data
- Tetapi, untuk data_rating terdapat 1 duplikat data

### Memeriksa Missing Value

![Missing Value](https://github.com/user-attachments/assets/7340a1ff-f86a-46f5-b803-4a37e761b521)


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

![Distribusi Rating](https://github.com/user-attachments/assets/9c36fb34-85f8-4dc0-be95-b4f5e4ae4492)


Insight:
- Rating 10 mendominasi sebagai nilai paling sering diberikan, diikuti oleh rating 9 dan 8.
- Rating 0 juga sangat tinggi, kemungkinan besar karena mencerminkan anime yang ditambahkan ke daftar namun belum ditonton atau belum diberi rating oleh pengguna (missing rating).
- Distribusi ini tidak simetris dan sangat condong ke arah positif (skewed right), mengindikasikan adanya bias terhadap anime favorit atau populer.

## Multivariate Analysis
### Movie/Anime Populer

![Movie Populer](https://github.com/user-attachments/assets/4146a054-7074-4dce-b660-31a64e156074)



Insight:
- "Kimi no Na wa." dan "Ginga Eiyuu Densetsu" menempati posisi teratas dengan rating rata-rata di atas 8

### Genre Terpopuler

![Genre Terpopuler](https://github.com/user-attachments/assets/b73cd8ab-40ac-41a6-b790-a68e789fe007)



Insight:
- Genre "Comedy", "Action", dan "Adventure" merupakan tiga genre paling dominan dalam koleksi dataset.
- Genre seperti "Music", "Mecha", dan "Supernatural" memiliki jumlah yang lebih sedikit

## Data Preparation
### Menangani Duplicat value

![Menangani Duplikat](https://github.com/user-attachments/assets/ae96066d-95be-4999-82cd-161b9a759c05)


Insight :
- Untuk data_movie tidak ditemukan duplikat data
- Tetapi, untuk data_rating terdapat 1 duplikat data
- Sehingga, untuk data yang terduplikat yang ada pada data_rating saya menghapus barisnya

### Menangani Missing Value

![Menangani missing](https://github.com/user-attachments/assets/4f720760-e578-4630-89ae-0ccede6c1e36)

Insight :
- Untuk data_movie ditemukan beberapa missing data
- Untuk data_rating tidak terdapat missing data
- Sehingga, untuk data yang missing yang ada pada data_movie saya menghapus barisnya

### Filter Data

![Filter Data](https://github.com/user-attachments/assets/1936edbb-e3ac-449d-8d54-380b17f19e1e)


Insight:
- Hanya menggunakan data dari pengguna dan item yang aktif (diatas 100)
- Supaya matriks interaksi menjadi lebih padat
- Fokus pada film yang cukup sering dirating akan memberi insight yang lebih dapat diandalkan.

### Data Spliting


![Splitting Data](https://github.com/user-attachments/assets/85965d85-195f-4637-8ec8-151a61ce718d)


Insight:
- Melakukan splitting data untuk data latih dan data uji

### Mapping dan Encoding

![mapping](https://github.com/user-attachments/assets/97fc4978-dc7a-4bbc-b872-34757e0d91fc)

- Membuat objek `Dataset` dan memetakan `ID user` dan `item` yang akan digunakan untuk melatih model LightFM
- Membuat reverse mapping dari index ke ID asli
- Membuat dictionary untuk mengubah `movieId` ke judul `film` (name)
#### Encoding ID menjadi angka

![Encoding ID](https://github.com/user-attachments/assets/5b996b6a-f6a2-482f-99bf-90bf30d83a23)

- Tahapan ini penting yang nantinya akan digunakan untuk membangun model NCF

## Modeling dan Result
Ada 2 algoritma yang digunakan untuk membuat model, yaitu sebagai berikut.
### LIGHTFM
#### Apa itu?
LightFM adalah algoritma sistem rekomendasi yang menggabungkan dua pendekatan:
- Collaborative Filtering (CF): mempelajari interaksi user-item.
- Content-Based Filtering: dapat menggabungkan fitur dari user dan item.
LightFM efektif digunakan untuk masalah implicit feedback (misalnya klik, like) maupun explicit feedback (seperti rating).
#### Cara Kerja
- Interaksi user-item dibuat dalam bentuk matriks sparse.
- User dan item dipetakan ke dalam embedding/vektor laten.
- Model menghitung skor relevansi antara user dan item menggunakan fungsi loss tertentu.
- Embedding diperbarui untuk meminimalkan loss (seperti BPR atau WARP).
#### Tahapan
- Preprocessing khusus:
  - Melakukan filter hanya interaksi dengan rating >= 8 dianggap positif (untuk train).
  - dan untuk test rating >= 7
- LightFM bekerja dengan matriks user-item sparse. build_interactions mengubah data rating menjadi matrix format yang efisien untuk pelatihan (CSR matrix). Proses ini dilakukan terpisah untuk training dan testing.
- Hanya user dan item yang sudah ada di training yang digunakan di testing, untuk menghindari cold-start saat evaluasi.
- Membangunan Model
- Lalu, training
#### Parameter yang Digunakan
- `loss='warp'`: Menggunakan Weighted Approximate-Rank Pairwise, cocok untuk implicit feedback.
- `random_state=42`: Untuk reprodusibilitas hasil.
- `epochs=10`: Jumlah iterasi pelatihan.
- `num_threads=4`: Jumlah thread paralel untuk mempercepat pelatihan.
#### Output Top-N Rekomendasi

![Contoh Hasil Prediksi LightFM](https://github.com/user-attachments/assets/265249d8-4e90-478b-bf42-ffb38f65da25)


### Neural Collaborative Filtering (NCF)
#### Apa itu?
NCF adalah pendekatan sistem rekomendasi berbasis deep learning yang menggantikan perkalian dot product (seperti dalam matrix factorization) dengan arsitektur neural network, untuk menangkap hubungan non-linear antara user dan item.
#### Cara Kerja
- User dan item diubah menjadi ID numerik.
- Masing-masing ID diubah menjadi vektor laten berdimensi tetap.
- Vektor user dan item digabung.
- Masuk ke fully-connected layers (dense).
- Output berupa prediksi rating user terhadap item.
#### Tahapan
- Karena embedding layer hanya menerima input integer, `user_id` dan `movieId` harus dikonversi ke angka. Encoding ini memastikan setiap user/item memiliki ID unik numerik dari 0 hingga N-1.
- Menambahkan kolom hasil encoding ke data yang nantinya digunakan sebagai input ke model NCF.
- Membangun arsitektur model
- Lalu, training model
#### Parameter yang Digunakan
- `Embedding dim=32`: Ukuran vektor representasi user/item.
- `Dense(128, 64)`: Layer dense untuk mempelajari hubungan kompleks.
- `activation='relu'`: Fungsi aktivasi untuk non-linearitas.
- `loss='mse'`: Menggunakan Mean Squared Error karena ini kasus explicit feedback (rating).
- `optimizer='adam'`: Optimizer yang adaptif dan umum digunakan.
- `batch_size=1024`, `epochs=10`: Untuk proses training.
#### Output Top-N Rekomendasi

![Contoh Hasil Prediksi NCF](https://github.com/user-attachments/assets/487dba5b-4752-4f6a-a56f-00c60c20a9c0)


## Evaluation
### Precision@k
Precision@k mengukur proporsi item yang direkomendasikan (Top-k) yang benar-benar relevan untuk user.
- Jika 3 dari 5 item yang direkomendasikan disukai user, maka Precision@5 = 3/5 = 0.6
- Nilainya antara 0–1, makin tinggi makin bagus.

![Precision@k](https://github.com/user-attachments/assets/5eadeff7-9b19-4141-b851-355ba75f5b55)



### Recall@k
Recall@k mengukur seberapa banyak item relevan yang berhasil ditemukan dari semua item relevan yang sebenarnya ada untuk user.
- Jika user menyukai 10 item, dan 3 dari 10 muncul di Top-5, maka Recall@5 = 3/10 = 0.3
- Mengukur kelengkapan rekomendasi.

![Recall@k](https://github.com/user-attachments/assets/3a320bdd-0634-422e-b21d-179d58bd3dfd)



### AUC Score
AUC mengukur seberapa baik model membedakan antara item relevan (positif) dan tidak relevan (negatif).
- Dengan menghitung kemungkinan item relevan mendapatkan skor lebih tinggi daripada item tidak relevan.
- dan mencocokan untuk evaluasi ranking global, terutama untuk data implicit feedback.


![AUC Score](https://github.com/user-attachments/assets/44418560-2583-4771-a8bd-86bc26999154)



### MSE
MSE mengukur seberapa jauh rata-rata kuadrat perbedaan antara prediksi rating dan rating aktual.
- Memberikan Penalti lebih besar untuk prediksi yang sangat jauh dari nilai sebenarnya.
- Lalu, digunakan untuk model regresi, seperti NCF.

![Mean Squared Error](https://github.com/user-attachments/assets/cdb7553a-2495-4157-b423-420137c36fac)



### MAE
MAE menghitung rata-rata kesalahan absolut antara rating prediksi dan aktual.
- Menilai Rata-rata kesalahan prediksi
- Tidak memberi penalti besar pada outlier seperti MSE.

![Mean Absolute Error](https://github.com/user-attachments/assets/6faf2209-3b0f-4935-bc40-b48f4affb4c7)

## Hasil Evaluasi
### LightFM

![LightFM Evaluation](https://github.com/user-attachments/assets/350968c8-7136-4a65-8ef4-b37c05bc3c6e)


Insight :
- `Precision@5`:
  - Artinya, rata-rata 17.02% dari 5 rekomendasi teratas yang diberikan kepada pengguna benar-benar relevan (dalam konteks: rating tinggi atau disukai user).
- `AUC Score`:
  - Area Under Curve (AUC) menunjukkan seberapa baik model membedakan item yang disukai dan tidak disukai user. Nilai mendekati 1.0 (maksimal) berarti:
    - Model sangat baik dalam ranking item yang benar di atas item yang salah.
    - Nilai 0.91 ini sangat bagus, artinya model punya kemampuan prediksi yang sangat baik.
- `Recall@5`:
  - Rata-rata hanya 2.28% dari total item relevan yang berhasil ditemukan di top-5.


### Neural Collaborative Filtering (NCF)


![NCF Evaluation](https://github.com/user-attachments/assets/5e41e80d-5f2a-415a-a80b-b61e738c17c4)


Insight :
Insight :
- `Precision@5`:
  - Artinya, rata-rata 79.98% dari 5 rekomendasi teratas yang diberikan kepada pengguna benar-benar relevan (dalam konteks: rating tinggi atau disukai user).
- `Recall@5`:
  - Rata-rata hanya 23.6% dari total item relevan yang berhasil ditemukan di top-5.
- `MSE` :
  - 3.8266 ini menunjukan bahwa model tidak menghasilkan kesalahan besar pada sebagian besar data
- `MAE` :
  - 1.1885 ini menunjukan model sudah cukup baik, tetapi model masih bisa ditingkatkan untuk bisa mendapatkan presisi yang lebih baik


## Kesimpulan
1. Berdasarkan kedua pendekatan yang sudah dilakukan yaitu dengan menggunakan model LightFM dan Neural Collaborative Filtering (NCF) menunjukan bahwa Neural Collaborative Filtering (NCF) dapat memberikan rekomendasi yang lebih relevan dibandingkan dengan model LightFM. Hal ini ditunjukan oleh hasil evaluasi yang menunjukan Precision@5 NCF yang tinggi (0.7998) jika dibandingkan dengan LightFM yang hanya memiliki Presicion@5 sebesar 0.1702.
2. Perbandingan antara ke-2 model ini menghasilkan model Neural Collaborative Filtering (NCF) yang unggul signifikan pada metriks top-k (Precision dan Recall). Meskipun model LightFM menunjukan nilai AUC yang tinggi (0.9120) yang membuktikan bahwa model dapat membedakan interaksi tetapi, performanya dalam menghasilkan rekomendasi Top-K sangat rendah (Precision@5 hanya 0.1702).

## Referensi
1. Mardhiyah, I., & Mukti, K. T. (2022). Sistem Rekomendasi Pembelian Lisensi Film Menggunakan Pendekatan Hybrid Filtering. Jurnal Riset Sistem Informasi dan Teknologi Informasi. https://jursistekni.nusaputra.ac.id/article/view/116
2. Faisal, M., & Roziqiin, N. M. (2024). Sistem rekomendasi pemilihan anime menggunakan user-based collaborative filtering. JIPI. https://www.jurnal.stkippgritulungagung.ac.id/index.php/jipi/article/view/4222
