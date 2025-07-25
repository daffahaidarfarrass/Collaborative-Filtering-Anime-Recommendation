# -*- coding: utf-8 -*-
"""Collaborative Filtering - Daffa Haidar Farras v.2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QVyISfy0NERbq7MaZ6ImEXjiDdFn4Tza

# Collaborative Filtering: Movie Recommendation
- Nama : Daffa Haidar Farras
- Username : daffa_haidar
- Email :  daffahaidarfarras@gmail.com

## Topik Rekomendasi Film

# Proyek Analisis Data: Rekomendasi Movie

Seiring pertumbuhan eksponensial konten hiburan digital, seperti film dan anime, pengguna semakin kesulitan menemukan tayangan yang relevan dan sesuai minat. Platform seperti Netflix, Crunchyroll, dan MyAnimeList menghadapi tantangan besar dalam mengelola dan merekomendasikan ribuan judul kepada jutaan pengguna. Oleh karena itu, pengembangan sistem rekomendasi cerdas menjadi sangat penting untuk meningkatkan pengalaman pengguna dan efisiensi dalam menjelajahi konten.

Metode Collaborative Filtering (CF) telah menjadi pendekatan utama dalam sistem rekomendasi, yang memanfaatkan kesamaan antar pengguna atau item berdasarkan histori interaksi mereka. Meskipun efektif, CF klasik memiliki kelemahan seperti cold-start problem dan kesulitan menangani data spars. Untuk mengatasi keterbatasan ini, pada projek ini menggunakan pendekatan seperti LightFM, yang melakukan collaborative filtering, serta Neural Collaborative Filtering (NCF), yang menggunakan jaringan saraf untuk memodelkan interaksi pengguna dan item secara lebih kompleks dan non-linear.


Link Dataset : https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

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

### Deskripsi:
Dataset ini berisi informasi tentang 12,294 anime dan preferensi dari 73,515 pengguna yang berbeda. Secara khusus, dataset ini mencakup user Id, movie Id, rating, dan genre

### Kolom/Fitur

### Usability dan Jumlah Baris
- Usability : 8.24
- **anime.csv** :
  - Jumlah Baris : 12,294
  - Jumlah Kolom : 7
- **rating.csv** :
  - Jumlah Baris : 7,813,737
  - Jumlah Kolom : 3

# Import Library
"""

pip install lightfm

import pandas as pd
import kagglehub
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
from sklearn.model_selection import train_test_split
import random

from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.evaluation import precision_at_k, auc_score

import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Flatten, Concatenate, Dense
from tensorflow.keras.models import Model

from sklearn.preprocessing import LabelEncoder

"""# Load Dataset"""

# Download latest version
path = kagglehub.dataset_download("CooperUnion/anime-recommendations-database")

print("Path to dataset files:", path)

# Path disesuaikan dengan path download
data_movie = pd.read_csv("/kaggle/input/anime-recommendations-database/anime.csv")
data_rating = pd.read_csv("/kaggle/input/anime-recommendations-database/rating.csv")

data_movie

data_rating

"""# Data Understanding

Pada tahap ini, akan memahami struktur dataset, termasuk:
- Jumlah baris dan kolom.
- Jenis data (numerik/kategorik).
- Distribusi nilai.
"""

data_rating.info()

"""Insight:

| Kolom | Deskripsi|
|---|---|
|user_id | non identifiable randomly generated user id. |
|anime_id | the anime that this user has rated. |
|rating | rating out of 10 this user has assigned (-1 if the user watched it but didn't assign a rating). |

- Semua Fitur memiliki tipe data `int64`
"""

data_movie.info()

"""Insight:

| Kolom | Deskripsi |
|---|---|
| anime_id | myanimelist.net's unique id identifying an anime. |
|name | full name of anime.|
|genre | comma separated list of genres for this anime.|
|type | movie, TV, OVA, etc.|
|episodes | how many episodes in this show. (1 if movie).|
|rating | average rating out of 10 for this anime.|
|members | number of community members that are in this anime's "group".|

- 3 dari 8 Fitur memiliki tipe data `int64`
- 1 dari 8 fitur memiliki tipe data `float64`
- 4 dari 8 fitur memiliki tipe data `object`
"""

data_movie.describe()

data_movie.shape

"""Insight :

Pada **data_movie** ini memiliki

|Jumlah Baris|Jumlah Kolom|
|---|---|
|12.294|8|
"""

data_rating.describe()

data_rating.shape

"""Insight :

Pada **data_rating** ini memiliki

|Jumlah Baris|Jumlah Kolom|
|---|---|
|7.813.737|4|
"""

print('Banyak data Movie: ', len(data_movie.anime_id.unique()))
print('Banyak data User: ', len(data_rating.user_id.unique()))

"""## Cek Duplikat

Untuk mengecek apakah ada data yang terduplikat
"""

print(data_movie.duplicated().sum())

print(data_rating.duplicated().sum())

"""Insight :
- Untuk data_movie tidak ditemukan duplikat data
- Tetapi, untuk data_rating terdapat 1 duplikat data

## Missing Value

Untuk mengecek apakah ada data yang hilang
"""

print(data_movie.isnull().sum())

print(data_rating.isnull().sum())

"""Insight :
- Untuk data_movie ditemukan beberapa missing data
- Untuk data_rating tidak terdapat missing data

# Exploratory Data Analysis

## Univariate Analysis

### Distribusi Rating
"""

plt.figure(figsize=(8, 5))
sns.histplot(data_rating['rating'], bins=10, kde=False)
plt.title('Distribusi Rating yang Diberikan Pengguna')
plt.xlabel('Rating')
plt.ylabel('Jumlah')
plt.show()

"""Insight:
- Rating 10 mendominasi sebagai nilai paling sering diberikan, diikuti oleh rating 9 dan 8.
- Rating 0 juga sangat tinggi, kemungkinan besar karena mencerminkan anime yang ditambahkan ke daftar namun belum ditonton atau belum diberi rating oleh pengguna (missing rating).
- Distribusi ini tidak simetris dan sangat condong ke arah positif (skewed right), mengindikasikan adanya bias terhadap anime favorit atau populer.

## Multivariate Analysis

### Movie Populer
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Rename agar kolom bisa di-merge
data_movie = data_movie.rename(columns={"anime_id": "anime_id"})

# Gabungkan rating dengan info movie
ratings_with_titles = pd.merge(data_rating, data_movie[['anime_id', 'name']], on='anime_id')

# Grouping berdasarkan anime_id, hitung rata-rata dan jumlah rating
movie_stats = ratings_with_titles.groupby('anime_id').agg(
    rating_mean=('rating', 'mean'),
    rating_count=('rating', 'count')
).reset_index()

# Filter hanya movie dengan setidaknya 100 rating
movie_stats = movie_stats[movie_stats['rating_count'] >= 100]

# Ambil nama movie dari data_movie
movie_stats = pd.merge(movie_stats, data_movie[['anime_id', 'name']], on='anime_id')

# Ambil Top 10 berdasarkan rata-rata rating tertinggi
top_rated = movie_stats.sort_values('rating_mean', ascending=False).head(10)

# Visualisasi
plt.figure(figsize=(10, 6))
sns.barplot(x=top_rated['rating_mean'], y=top_rated['name'], palette="viridis")
plt.title("Top 10 Movie dengan Rating Tertinggi (min 100 rating)")
plt.xlabel("Rata-rata Rating")
plt.ylabel("Movie")
plt.show()

"""Insight:
- "Kimi no Na wa." dan "Ginga Eiyuu Densetsu" menempati posisi teratas dengan rating rata-rata di atas 8

### Genre Terpopuler
"""

# Pisahkan genre
movie_exploded = data_movie.dropna(subset=["genre"]).copy()
movie_exploded["genre"] = movie_exploded["genre"].str.split(", ")
genre_counts = movie_exploded.explode("genre")["genre"].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.values[:15], y=genre_counts.index[:15], palette="magma")
plt.title("15 Genre Movie Terpopuler")
plt.xlabel("Jumlah Movie")
plt.ylabel("Genre")
plt.show()

"""# Data Preparation

Insight:
- Genre "Comedy", "Action", dan "Adventure" merupakan tiga genre paling dominan dalam koleksi dataset.
- Genre seperti "Music", "Mecha", dan "Supernatural" memiliki jumlah yang lebih sedikit

## Data Cleaning

### Menanagani Data Duplikat
"""

print(data_movie.duplicated().sum())

print(data_rating.duplicated().sum())

data_rating = data_rating.drop_duplicates()

"""Insight :
- Untuk data_movie tidak ditemukan duplikat data
- Tetapi, untuk data_rating terdapat 1 duplikat data
- Sehingga, untuk data yang terduplikat yang ada pada data_rating saya menghapus barisnya

### Menangani Missing Value
"""

print(data_movie.isnull().sum())

print(data_rating.isnull().sum())

data_movie = data_movie.dropna()

"""Insight :
- Untuk data_movie ditemukan beberapa missing data
- Untuk data_rating tidak terdapat missing data
- Sehingga, untuk data yang missing yang ada pada data_movie saya menghapus barisnya

## Filter Data
"""

# Hitung item dan user yang aktif (dengan minimal 100 interaksi)
item_count = data_rating['anime_id'].value_counts()
user_count = data_rating['user_id'].value_counts()

# Ambil item dan user yang memenuhi syarat
active_items = item_count[item_count >= 100].index
active_users = user_count[user_count >= 100].index

# Filter data_rating berdasarkan item dan user yang aktif
filtered_data = data_rating[
    (data_rating['anime_id'].isin(active_items)) &
    (data_rating['user_id'].isin(active_users))
]

"""Insight:
- Hanya menggunakan data dari pengguna dan item yang aktif
- Supaya matriks interaksi menjadi lebih padat
- Fokus pada film yang cukup sering dirating akan memberi insight yang lebih dapat diandalkan.
"""

filtered_data

"""## Splitting Data"""

train_df, test_df = train_test_split(filtered_data, test_size=0.2, random_state=42)

"""Insight:
- Melakukan splitting data untuk data latih dan data uji

### Mapping

Membuat objek `Dataset` dan memetakan `ID user` dan `item`
"""

dataset = Dataset()
dataset.fit(
    train_df['user_id'].unique(),
    train_df['anime_id'].unique()
    )

"""Membuat reverse mapping dari index ke ID asli"""

user_id_map, _, item_id_map, _ = dataset.mapping()

reverse_user_map = {index: userId for userId, index in user_id_map.items()}
reverse_item_map = {index: itemId for itemId, index in item_id_map.items()}

"""Membuat dictionary untuk mengubah `movieId` ke judul `film` (name)"""

movie_id_to_title = dict(zip(data_movie['anime_id'].astype(int), data_movie['name']))

"""## Fit LabelEncoder

Tahapan ini penting yang nantinya akan digunakan untuk membangun model NCF
"""

from sklearn.preprocessing import LabelEncoder

user_enc = LabelEncoder()
item_enc = LabelEncoder()

user_enc.fit(filtered_data['user_id'])
item_enc.fit(filtered_data['anime_id'])

"""# LightFM

## Fit Dataset dan Mapping

### Untuk Train data

Membangun objek `interactions_train` berupa matriks interaksi user-item dari `train_df`.
"""

(interactions_train, _) = dataset.build_interactions(
    ((row['user_id'], row['anime_id'], 1.0 if row['rating'] >= 8 else 0.0)
    for _, row in train_df.iterrows())
    )

"""### Untuk Test data

Untuk memastikan `test_df` hanya berisi user dan item yang sudah pernah muncul di data latih `train_df`
"""

valid_users = set(train_df['user_id'])
valid_items = set(train_df['anime_id'])
test_df = test_df[test_df['user_id'].isin(valid_users) & test_df['anime_id'].isin(valid_items)]

"""Membangun objek `interactions_test` berupa matriks interaksi user-item dari `test_df`."""

(interactions_test, _) = dataset.build_interactions(
    [(row['user_id'], row['anime_id'], 1.0 if row['rating'] >= 7 else 0.0)
    for _, row in test_df.iterrows()]
    )

"""## Training LightFM"""

model_lightFM = LightFM(loss='warp', random_state=42)
model_lightFM.fit(
    interactions_train,
    epochs=10,
    num_threads=4,
    verbose=True
)

"""## Evaluasi model LightFM"""

from lightfm.evaluation import precision_at_k, recall_at_k, auc_score

k = 5
precision = precision_at_k(model_lightFM, interactions_test, k=k).mean()
recall = recall_at_k(model_lightFM, interactions_test, k=k).mean()
auc = auc_score(model_lightFM, interactions_test).mean()

print(f"[LightFM Evaluation]")
print(f"Precision@{k}: {precision:.4f}")
print(f"Recall@{k}: {recall:.4f}")
print(f"AUC Score: {auc:.4f}")

"""Insight :
- `Precision@5`:
  - Artinya, rata-rata 17.21% dari 5 rekomendasi teratas yang diberikan kepada pengguna benar-benar relevan (dalam konteks: rating tinggi atau disukai user).
- `AUC Score`:
  - Area Under Curve (AUC) menunjukkan seberapa baik model membedakan item yang disukai dan tidak disukai user. Nilai mendekati 1.0 (maksimal) berarti:
    - Model sangat baik dalam ranking item yang benar di atas item yang salah.
    - Nilai 0.91 ini sangat bagus, artinya model punya kemampuan prediksi yang sangat baik.
- `Recall@5`:
  - Rata-rata hanya 2.3% dari total item relevan yang berhasil ditemukan di top-5.

## Prediksi
"""

user_id = random.choice(train_df['user_id'].unique())
user_internal_id = dataset.mapping()[0].get(user_id)
n_users, n_items = interactions_train.shape

scores = model_lightFM.predict(
    user_ids=np.full(n_items, user_internal_id),
    item_ids=np.arange(n_items)
)

top_items = np.argsort(-scores)[:10]
data_movie['anime_id'] = data_movie['anime_id'].astype(int)

liked_movies = filtered_data[(filtered_data['user_id'] == user_id) & (filtered_data['rating'] >= 7)]
liked_titles = data_movie[data_movie['anime_id'].isin(liked_movies['anime_id'])]['name'].head(5).tolist()

print(f"\n User {user_id} menyukai film berikut (rating >= 7):")
for i, title in enumerate(liked_titles, start=1):
    print(f"{i}. {title}")


print(f"\nTop 10 Rekomendasi untuk User {user_id}:\n")

# Pastikan movie_df['anime_id'] bertipe int agar cocok dengan reverse map
data_movie['anime_id'] = data_movie['anime_id'].astype(int)

for rank, item_index in enumerate(top_items, start=1):
    # Ambil anime_id dari reverse map
    movie_id = reverse_item_map.get(item_index)

    # Ambil judul film dari data_movie
    title_row = data_movie[data_movie['anime_id'] == movie_id]['name'].values
    title_str = title_row[0] if len(title_row) > 0 else f"Movie ID {movie_id}"

    print(f"{rank}. {title_str}")

"""# Training Neural Collaborative Filtering (NCF)"""

data_rating[['user_id', 'anime_id', 'rating']]

"""menggunakan `LabelEncoder` dari sklearn untuk mengubah `ID user` dan `item` menjadi indeks numerik"""

train_df['user_id_enc'] = user_enc.transform(train_df['user_id'])
train_df['item_enc'] = item_enc.transform(train_df['anime_id'])

test_df['user_id_enc'] = user_enc.transform(test_df['user_id'])
test_df['item_enc'] = item_enc.transform(test_df['anime_id'])

num_users = len(user_enc.classes_)
num_items = len(item_enc.classes_)

"""## Bangun model NCF"""

# Input layers
user_input = Input(shape=(1,), name='user_input')
item_input = Input(shape=(1,), name='item_input')

# Embedding layers
user_embedding = Embedding(input_dim=num_users, output_dim=32, name='user_embedding')(user_input)
item_embedding = Embedding(input_dim=num_items, output_dim=32, name='item_embedding')(item_input)

# Flatten
user_vec = Flatten()(user_embedding)
item_vec = Flatten()(item_embedding)

# Concatenate
concat = Concatenate()([user_vec, item_vec])

# Fully connected layers
fc = Dense(128, activation='relu')(concat)
fc = Dense(64, activation='relu')(fc)
output = Dense(1)(fc)

# Build model
model_NCF = Model(inputs=[user_input, item_input], outputs=output)
model_NCF.compile(optimizer='adam', loss='mse', metrics=['mae'])

model_NCF.summary()

"""Mengubah user dan movie ID menjadi angka"""

# Training data
X_train_user = train_df['user_id_enc'].values
X_train_item = train_df['item_enc'].values
y_train = train_df['rating'].values

# Testing data
X_test_user = test_df['user_id_enc'].values
X_test_item = test_df['item_enc'].values
y_test = test_df['rating'].values

"""## Training NCF"""

# Train
model_NCF.fit(
    x=[X_train_user, X_train_item],
    y=y_train,
    epochs=10,
    batch_size=1024,
    validation_data=([X_test_user, X_test_item], y_test)
)

"""## Evaluasi Neural Collaborative Filtering (NCF)"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Prediksi rating NCF
y_pred = model_NCF.predict([X_test_user, X_test_item]).flatten()

# Hitung MSE dan MAE (regression evaluation)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"\n[NCF Regression Evaluation]")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")

# Buat DataFrame untuk evaluasi ranking
pred_df = pd.DataFrame({
    'user': X_test_user,
    'item': X_test_item,
    'true_rating': y_test,
    'pred_rating': y_pred
})

# Hitung Precision@K dan Recall@K untuk NCF
def precision_recall_at_k(df, k=5, threshold=8.0):
    precision_list = []
    recall_list = []

    for user_id in df['user'].unique():
        user_data = df[df['user'] == user_id]

        # Top-K prediksi tertinggi
        top_k_items = user_data.sort_values('pred_rating', ascending=False).head(k)
        relevant_items = user_data[user_data['true_rating'] >= threshold]

        n_relevant = len(relevant_items)
        if n_relevant == 0:
            continue  # skip user tanpa item relevan

        hit = top_k_items[top_k_items['true_rating'] >= threshold]

        precision = len(hit) / k
        recall = len(hit) / n_relevant

        precision_list.append(precision)
        recall_list.append(recall)

    return np.mean(precision_list), np.mean(recall_list)

# Evaluasi NCF Top-K (K = 5)
k = 5
precision_ncf, recall_ncf = precision_recall_at_k(pred_df, k=k, threshold=8.0)

print(f"\n[NCF Top-K Evaluation]")
print(f"Precision@{k}: {precision_ncf:.4f}")
print(f"Recall@{k}: {recall_ncf:.4f}")

"""Insight :
- `Precision@5`:
  - Artinya, rata-rata 79.83% dari 5 rekomendasi teratas yang diberikan kepada pengguna benar-benar relevan (dalam konteks: rating tinggi atau disukai user).
- `Recall@5`:
  - Rata-rata hanya 23.5% dari total item relevan yang berhasil ditemukan di top-5.
- `MSE` :
  - 3.8368 ini menunjukan bahwa model tidak menghasilkan kesalahan besar pada sebagian besar data
- `MAE` :
 - 1.2 ini menunjukan model sudah cukup baik, tetapi model masih bisa ditingkatkan untuk bisa mendapatkan presisi yang lebih baik

## Prediksi
"""

def recommend_top_n(user_id, n=10):
    # Encode user_id ke indeks internal
    encoded_user = user_enc.transform([user_id])[0]

    # Buat array item_id untuk semua item
    item_ids = np.arange(num_items)
    user_array = np.full_like(item_ids, encoded_user)

    # Prediksi rating untuk semua item dari user ini
    predictions = model_NCF.predict([user_array, item_ids], verbose=0).flatten()

    # Urutkan prediksi dan ambil top N
    top_n_indices = predictions.argsort()[-n:][::-1]

    # Decode item indices ke anime_id asli
    recommended_movie_ids = item_enc.inverse_transform(top_n_indices)

    # Ambil judul dari data_movie
    recommended_titles = data_movie[data_movie['anime_id'].isin(recommended_movie_ids)][['anime_id', 'name']]

    # Urutkan sesuai urutan prediksi
    ordered_titles = [recommended_titles[recommended_titles['anime_id'] == mid]['name'].values[0]
                      if not recommended_titles[recommended_titles['anime_id'] == mid].empty
                      else f"Movie ID {mid}"
                      for mid in recommended_movie_ids]
    top_items = np.argsort(-scores)[:10]
    data_movie['anime_id'] = data_movie['anime_id'].astype(int)

    liked_movies = filtered_data[(filtered_data['user_id'] == user_id) & (filtered_data['rating'] >= 7)]
    liked_titles = data_movie[data_movie['anime_id'].isin(liked_movies['anime_id'])]['name'].head(5).tolist()

    print(f"\n User {user_id} menyukai film berikut (rating >= 7):")
    for i, title in enumerate(liked_titles, start=1):
        print(f"{i}. {title}")


    print(f"\nTop {n} Rekomendasi untuk User {user_id} (NCF):")
    for i, title in enumerate(ordered_titles, 1):
        print(f"{i}. {title}")

    return recommended_movie_ids

# Misalnya kamu mau rekomendasi untuk user dengan ID 5
recommend_top_n(user_id=(random.choice(train_df['user_id'].unique())), n=10)

