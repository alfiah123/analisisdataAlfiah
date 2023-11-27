# -*- coding: utf-8 -*-
"""dashboard.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13t93DLrtqlgjUpFh_DyBjXhOJE4Ypq2D
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = 'https://raw.githubusercontent.com/marceloreis/HTI/master/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv'
dataset = pd.read_csv(url)

# Menambahkan judul
st.title('Dashboard Analisis Data Kualitas Udara')

# Tampilkan beberapa baris data
st.subheader('Data Awal')
st.write(dataset.head())

# Visualisasi 1: Histogram tingkat PM2.5 pada jam tertentu dalam sehari
hourly_avg_PM25 = dataset.groupby('hour')['PM2.5'].mean()
st.subheader('Histogram Rata-rata Tingkat PM2.5 pada Jam Tertentu dalam Sehari')
fig, ax = plt.subplots()
ax.bar(hourly_avg_PM25.index, hourly_avg_PM25.values, color='skyblue', edgecolor='black')
ax.set_xlabel('Jam dalam Sehari')
ax.set_ylabel('Rata-rata Tingkat PM2.5')
st.pyplot(fig)

# Visualisasi 2: Hubungan antara suhu dan tingkat PM2.5
st.subheader('Scatter plot: Hubungan antara Suhu dan Tingkat PM2.5')
fig, ax = plt.subplots()
sns.scatterplot(x='TEMP', y='PM2.5', data=dataset, alpha=0.5, ax=ax)
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Tingkat PM2.5')
st.pyplot(fig)

# Visualisasi 3: Heatmap korelasi antara variabel cuaca dan tingkat PM2.5
correlation_matrix = dataset[['TEMP', 'PRES', 'DEWP', 'RAIN', 'PM2.5']].corr()
st.subheader('Heatmap Korelasi antara Variabel Cuaca dan Tingkat PM2.5')
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)