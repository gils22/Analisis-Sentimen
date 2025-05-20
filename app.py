import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Judul aplikasi
st.title('Analisis Sentimen Timnas Sepakbola Indonesia di Era STY')

# Membaca data langsung dari file CSV lokal
data = pd.read_csv("Analisis_sentimen_timnas_sepakbola_indonesia_di_era_STY.csv")  # Sesuaikan dengan path file Anda

# Proses data sesuai kebutuhan Anda (misalnya data cleaning, analisis, dll)
data = data.dropna()  # Menghapus data yang hilang

# Menampilkan data yang sudah diproses
st.write("Data yang telah diolah:")
st.dataframe(data)

# Insight 1: Statistik Ringkasan
st.markdown("### 📊 Ringkasan Statistik Data")
total_komentar = data.shape[0]
kategori_terbanyak = data['label'].mode()[0]  # Sentimen yang paling banyak
rata_rata_panjang_komentar = data['komentar'].str.len().mean()  # Rata-rata panjang komentar

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Komentar", value=total_komentar)
with col2:
    st.metric(label="Kategori Sentimen Terbanyak", value=kategori_terbanyak)
with col3:
    st.metric(label="Panjang Rata-rata Komentar", value=f"{rata_rata_panjang_komentar:.2f} karakter")

# Insight 2: Distribusi Sentimen
label_counts = data['label'].value_counts()
st.write("### 📉 Distribusi Sentimen Komentar:")
fig, ax = plt.subplots()
label_counts.plot(kind='bar', color=['#FF6347', '#32CD32'], ax=ax)
ax.set_title('Distribusi Sentimen Komentar')
ax.set_xlabel('Sentimen')
ax.set_ylabel('Jumlah Komentar')
st.pyplot(fig)

# Insight 3: Wordcloud untuk Sentimen Positif
st.subheader("☁️ Wordcloud untuk Sentimen Positif")
positive_comments = data[data['label'] == 'positif']['komentar'].str.cat(sep=' ')
wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_comments)
st.image(wordcloud_positive.to_array(), use_container_width=True)

# Insight 4: Wordcloud untuk Sentimen Negatif
st.subheader("☁️ Wordcloud untuk Sentimen Negatif")
negative_comments = data[data['label'] == 'negatif']['komentar'].str.cat(sep=' ')
wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(negative_comments)
st.image(wordcloud_negative.to_array(), use_container_width=True)

# Insight 5: Distribusi Panjang Komentar
st.markdown("### 📏 Distribusi Panjang Komentar:")
fig, ax = plt.subplots()
ax.hist(data['komentar'].str.len(), bins=20, color='lightblue', edgecolor='black')
ax.set_title('Distribusi Panjang Komentar')
ax.set_xlabel('Panjang Komentar (Karakter)')
ax.set_ylabel('Jumlah Komentar')
st.pyplot(fig)

# Insight 6: Distribusi Komentar Berdasarkan Waktu
st.markdown("### 🕒 Distribusi Komentar Berdasarkan Waktu (Jam):")
data['Hour'] = data['komentar'].apply(lambda x: x.lower().count(' '))  # Dummy logic untuk jam
hour_count = data['Hour'].value_counts().sort_index()
st.bar_chart(hour_count)

# Insight 7: Frekuensi Sentimen Berdasarkan Label
st.markdown("### 🌟 Frekuensi Sentimen Berdasarkan Label")
sentiment_counts = data['label'].value_counts()

# Menampilkan distribusi sentimen berdasarkan label
st.bar_chart(sentiment_counts)

# Menampilkan DataFrame untuk referensi lebih lanjut
st.write("Distribusi sentimen berdasarkan label:")
st.dataframe(sentiment_counts)

# Input Komentar Baru
st.markdown("### 📝 Masukkan Komentar Baru untuk Analisis Sentimen")
new_comment = st.text_area("Komentar Baru", "")

if new_comment:
    # Prediksi Sentimen Sederhana
    if "bagus" in new_comment.lower() or "menang" in new_comment.lower():
        prediksi_sentimen = "positif"
    else:
        prediksi_sentimen = "negatif"
    
    # Menampilkan hasil analisis sentimen untuk komentar baru
    st.write(f"### Analisis Sentimen untuk Komentar Baru: **{prediksi_sentimen.capitalize()}**")
