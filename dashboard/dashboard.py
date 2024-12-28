import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

#  Load dataset (pastikan Anda mengganti 'salaries.csv' dengan path file Anda)
def load_data():
    return pd.read_csv("all_data.csv")

# Load data
salaries_dataset_df = load_data()

# Sidebar content
with st.sidebar:
    st.write("""
        # Proyek Analyst Data: Data Science Salaries Dataset :sparkles:
        - **Nama:** Eva Theresia Pardede
        - **Email:** evatheresiapardede@gmail.com
        - **Linkedin:**  https://www.linkedin.com/in/eva-theresia-pardede-2157b0246/
    """)
    # selected_filter = st.selectbox(
    # label="Pilih Filter Berdasarkan:",
    # options=(
    # 'Tahun Kerja', 
    # 'Tingkat Pengalaman', 
    # 'Jenis Pekerjaan', 
    # 'Jabatan', 
    # 'Gaji', 
    # 'Mata Uang Gaji', 
    # 'Gaji dalam USD', 
    # 'Domisili Karyawan', 
    # 'Rasio Kerja Remote', 
    # 'Lokasi Perusahaan', 
    # 'Ukuran Perusahaan'))

# Header Content
# st.header("Data Science Salaries :sparkles:")

import streamlit as st

# Menambahkan CSS untuk center align
st.markdown(
    """
    <style>
    .centered-header {
        text-align: center;
        color: #b1d274; 
        font-size: 40;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Menampilkan header dengan center alignment
st.markdown('<h1 class="centered-header">Data Science Salaries</h1>', unsafe_allow_html=True)


# Pertanyaan No 1
st.write("1. Apa 5 pekerjaan(job title) dengan jumlah karyawan terbanyak dari tahun 2020 hingga 2024?")
# Visualisasi
top_titles = salaries_dataset_df['job_title'].value_counts().head(5).reset_index()
fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_titles, x='count', y='job_title', palette=['#2c5e51'])
plt.title('Top 5 Job Titles dengan Jumlah Karyawan Terbanyak (2020–2024)', fontsize=14)
plt.xlabel('Jumlah Karyawan', fontsize=12)
plt.ylabel('Job Title', fontsize=12)
st.pyplot(fig1)
#Insight
st.write("Insight: Berdasarkan analisis data yang dilakukan untuk periode 2020 hingga 2024, lima pekerjaan (job title) dengan jumlah karyawan terbanyak adalah Data Engineer, Data Scientist, Data Analyst, Machine Learning Engineer, dan Analytics Engineer")
st.write("")


# Pertanyaan No 2
st.write("")
st.write("2. Bagaimana tren rata-rata kenaikan gaji(salary in usd) untuk 5 pekerjaan(job title) dengan jumlah karyawan terbanyak dari tahun 2020 hingga 2024?")
# Visualisasi 
top_titles_tren = salaries_dataset_df['job_title'].value_counts().head(5).index
top_titles_data = salaries_dataset_df[salaries_dataset_df['job_title'].isin(top_titles_tren)]
salary_trend = top_titles_data.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()
colors = ['#2c5e51' ,'#5d996a', '#b1d274' ,'#d7c14f' ,'#ffa841']
fig2, ax = plt.subplots(figsize=(10, 6))
for idx, job_title in enumerate(top_titles_tren):
    job_data = salary_trend[salary_trend['job_title'] == job_title]
    plt.plot(job_data['work_year'], job_data['salary_in_usd'], marker='o', label=job_title, color=colors[idx])
plt.title('Tren Rata-rata Kenaikan Gaji (USD) untuk 5 Pekerjaan Terpopuler (2020–2024)', fontsize=14)
plt.xlabel('Tahun',fontsize=12)
plt.ylabel('Rata-rata Gaji (USD)',fontsize=12)
plt.legend(title='Job Title')
plt.grid(True)
st.pyplot(fig2)
#Insight
st.write("Insight: Berdasarkan analisis data yang dilakukan untuk periode 2020 hingga 2024, lima pekerjaan (job title) dengan jumlah karyawan terbanyak adalah Data Engineer, Data Scientist, Data Analyst, Machine Learning Engineer, dan Analytics Engineer. Pada tahun 2021, terlihat adanya penurunan yang cukup tajam dalam rata-rata gaji, yang mungkin dipengaruhi oleh faktor eksternal seperti pandemi. Namun, setelah 2021, terjadi pemulihan yang konsisten, diikuti dengan peningkatan yang stabil hingga tahun 2024. Hal ini menunjukkan bahwa permintaan untuk pekerjaan di bidang teknologi dan data semakin meningkat.")
st.write("")


# Pertanyaan No 3
st.write("")
st.write("3. Bagaimana 5 distribusi gaji(salary in usd) tertinggi untuk setiap pekerjaan(job title) karyawan?")
# Visualisasi
top_salaries_by_job = salaries_dataset_df.groupby('job_title')['salary_in_usd'].max().head(5).reset_index()
fig3, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_salaries_by_job, x='job_title', y='salary_in_usd', palette=['#ffa841'])
plt.title('Distribusi 5 Gaji Tertinggi (USD) untuk Setiap Job Title Karyawan', fontsize=14)
plt.xlabel('Job Title', fontsize=12)
plt.ylabel('Gaji (USD)', fontsize=12)
st.pyplot(fig3)
#Insight
st.write("Insight: Berdasarkan hasil analisis distribusi gaji untuk setiap pekerjaan (job title) karyawan, lima pekerjaan dengan gaji tertinggi adalah AI Architect, AI Developer, AI Engineer, AI Product Manager, dan AI Programmer. Dari kelima pekerjaan tersebut, AI Architect memiliki gaji tertinggi, dengan angka mencapai 800.000 USD.")
st.write("")


# Pertanyaan No 4
st.write("")
st.write("4. Berapa persentase karyawan yang tempat(employee residence) tinggalnya berada di kota yang sama dengan lokasi perusahaan(company location) tempat mereka bekerja?")
# Visualisasi 
salaries_dataset_df['same_location']=salaries_dataset_df['employee_residence'] == salaries_dataset_df['company_location']
same_location_count = salaries_dataset_df['same_location'].value_counts()
labels = ['Lokasi Sama', 'Lokasi Berbeda']
sizes = same_location_count.values
colors = ['#2c5e51', '#ffa841']
explode = (0.1, 0)
fig4, ax = plt.subplots(figsize=(8, 8))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode
)
plt.title('Persentase Karyawan yang Tinggal di Kota yang Sama dengan Lokasi Perusahaan', fontsize=14)
st.pyplot(fig4)
#Insight
st.write("Insight: Berdasarkan hasil analisis, persentase karyawan yang tinggal di kota yang sama dengan lokasi perusahaan tempat mereka bekerja sangat tinggi, yaitu mencapai 98,6%. Sementara itu, hanya 1,4% karyawan yang tinggal di kota berbeda dengan lokasi perusahaan mereka. Hal ini menunjukkan bahwa mayoritas pekerja cenderung bekerja di lokasi yang sama dengan tempat tinggal mereka, yang mungkin dipengaruhi oleh faktor-faktor salah satunya yaitu kemudahan akses.")
st.write("")


# Pertanyaan No 5
st.write("")
st.write("5. Bagaimana persentase antara ukuran perusahaan(company size) dan lokasi perusahaan(company location) dengan jumlah karyawan terbanyak?")
# Visualisasi
company_size_location = salaries_dataset_df.groupby(['company_location', 'company_size']).size().reset_index(name='count')
top_company_size_location = company_size_location.sort_values(by='count', ascending=False).head(5)
locations = top_company_size_location['company_location'] + " (" + top_company_size_location['company_size'] + ")"
counts = top_company_size_location['count']
labels = locations
sizes = counts
explode = (0.1, 0,0,0,0)
fig5, ax = plt.subplots(figsize=(8, 8))
plt.pie(sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=['#2c5e51' ,'#5d996a', '#b1d274' ,'#d7c14f' ,'#ffa841'],
        explode=explode)
plt.title('Persentase 5 Jumlah Perusahaan Berdasarkan Ukuran dan Lokasi Perusahaan', fontsize=14)
st.pyplot(fig5)
#Insight
st.write("Insight: Berdasarkan hasil analisis, lokasi perusahaan dengan jumlah karyawan terbanyak terdapat di US, diikuti oleh CA dan GB. Selain itu, ukuran perusahaan yang memiliki jumlah karyawan terbanyak di US adalah perusahaan dengan ukuran menengah (M).")
st.write("")


# Pertanyaan No 6
st.write("")
st.write("6. Bagaimana persebaran data antara gaji(salary in usd), tingkat pengalaman(experience level), dan ukuran perusahaan(company size)?")
# Visualisasi 
fig6, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data= salaries_dataset_df,
    x='experience_level',
    y='salary_in_usd',
    hue='company_size',
    palette=['#2c5e51' ,'#b1d274', '#ffa841'],
    s=100
)
plt.title('Persebaran Data Gaji (USD), Tingkat Pengalaman, dan Ukuran Perusahaan', fontsize=14)
plt.xlabel('Tingkat Pengalaman', fontsize=12)
plt.ylabel('Gaji(USD)', fontsize=12)
plt.legend(title='Ukuran Perusahaan')
plt.grid(True)
st.pyplot(fig6)
df = salaries_dataset_df
#Insight
st.write("Insight: Berdasarkan analisis, dapat dilihat bahwa persebaran data gaji (salary in USD) untuk perusahaan dengan ukuran menengah (M) tersebar merata di keempat tingkat pengalaman. Hal ini kemungkinan terjadi karena jumlah perusahaan dengan ukuran menengah (M) lebih banyak dibandingkan dengan perusahaan besar (L) atau kecil (S), sehingga persebaran data gaji pada perusahaan ukuran M lebih luas.")
st.write("")


# Pertanyaan No 7
st.write("")
st.write("7. Bagaimana demografi antara gaji(salary in usd), jenis pekerjaan(employment type), dan rasio pekerjaan jarak jauh(remote ratio)?")
# Visualisasi 
aggregated_data = salaries_dataset_df.groupby(['employment_type', 'remote_ratio'], as_index=False)['salary_in_usd'].mean()
fig7, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=aggregated_data,
    x='employment_type',
    y='salary_in_usd',
    hue='remote_ratio',
    palette=['#2c5e51' ,'#b1d274', '#ffa841']
)
plt.title('Demografi Gaji (USD), Jenis Pekerjaan, dan remote ratio', fontsize=14)
plt.xlabel('Jenis Pekerjaan', fontsize=12)
plt.ylabel('Rata-rata Gaji (USD)', fontsize=12)
plt.legend(title='remote ratio', fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig7)
#Insight
st.write("Insight: Berdasarkan analisis, dapat dilihat bahwa jenis pekerjaan full time memiliki rasio pekerjaan remote ratio yang bervariasi. Hal ini dilihat dari persentase karyawan yang tinggal di kota yang sama dengan lokasi perusahaan. Faktor ini berkontribusi pada tingginya persentase jenis pekerjaan full time, yang cenderung memiliki opsi pekerjaan remote ratio yang lebih fleksibel. Keberagaman rasio pekerjaan remote ratio pada jenis pekerjaan full time dapat dijelaskan dengan banyaknya karyawan yang berada di lokasi yang sama, memudahkan perusahaan untuk menawarkan berbagai model pekerjaan, baik yang jarak dekat maupun yang bekerja dari remote ratio.")
st.write("")

