import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data
data = pd.read_csv('data_1.csv')  # Ganti 'hour.csv' dengan path file Anda

# Judul dashboard
st.title("Dashboard Analisis Data Bike Sharing")

# Tampilkan data
st.subheader("Data Head")
st.write(data.head())

# Statistik deskriptif
st.subheader("Statistik Deskriptif")
st.write(data.describe())

# Visualisasi 1: Hourly Rental Patterns
st.subheader("Pola Sewa per Jam")
hourly_rentals = data.groupby('hr')['cnt'].mean().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(hourly_rentals['hr'], hourly_rentals['cnt'], marker='o', linestyle='-')
plt.title('Rata-rata Sewa Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Sewa')
plt.grid(True)
st.pyplot(plt)

# Visualisasi 2: Correlation between Temperature and Rentals
st.subheader("Korelasi antara Temperatur dan Jumlah Sewa")
plt.figure(figsize=(8, 6))
plt.scatter(data['temp'], data['cnt'], alpha=0.5)
plt.title('Jumlah Sewa vs. Temperatur')
plt.xlabel('Temperatur')
plt.ylabel('Jumlah Sewa')
plt.grid(True)
st.pyplot(plt)

# Visualisasi 3: Heatmap Korelasi
st.subheader("Heatmap Korelasi")
numeric_data = data.select_dtypes(include=['number'])
corr = numeric_data.corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Filter data berdasarkan jam
st.subheader("Analisis Berdasarkan Jam")
hour_filter = st.slider("Pilih Jam", min_value=0, max_value=23, value=12)
filtered_data = data[data['hr'] == hour_filter]
st.write(f"Data untuk Jam {hour_filter}:")
st.write(filtered_data)
