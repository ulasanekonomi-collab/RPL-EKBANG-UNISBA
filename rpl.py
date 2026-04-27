import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="RPL Unisba", page_icon="🎓", layout="wide")

# 2. Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/id/8/8c/Logo_Unisba.png", width=100) 
with col2:
    st.title("Portal Rekognisi Pembelajaran Lampau (RPL)")
    st.subheader("Universitas Islam Bandung")

st.divider()

# 3. Membuat Tab (Agar rapi dan tidak error)
tab1, tab2 = st.tabs(["📋 Informasi & Cek Kelayakan", "📤 Pengajuan E-Portofolio"])

with tab1:
    st.markdown("### 👋 Selamat Datang di Jalur RPL Tipe A")
    st.info("RPL adalah pengakuan atas pengalaman kerja Anda menjadi SKS akademik.")
    
    with st.expander("📖 Lihat Manfaat & Landasan Hukum"):
        st.write("Berdasarkan Keputusan Dirjen Dikti No. 112/B/KPT/2025.")
        st.bullet_point("Efisiensi Waktu Kuliah")
        st.bullet_point("Biaya Lebih Hemat")

    st.markdown("---")
    st.subheader("🔍 Cek Kelayakan Awal")
    c1, c2 = st.columns(2)
    with c1:
        ijazah = st.selectbox("Ijazah Terakhir", ["Pilih", "SMA/SMK/MA", "Diploma", "Putus Kuliah"])
        masa_kerja = st.number_input("Masa Kerja (Tahun)", min_value=0)
    with c2:
        bidang_kerja = st.text_input("Bidang Pekerjaan", placeholder="Contoh: Perbankan")

    if st.button("Analisis Potensi"):
        if masa_kerja >= 2:
            st.success(f"Potensi Tinggi! Pengalaman di {bidang_kerja} sangat mendukung.")
            st.balloons()
        else:
            st.warning("Masa kerja minimal disarankan 2 tahun.")

with tab2:
    st.header("Formulir E-Portofolio")
    st.write("Ceritakan keahlian Anda di sini.")

    # Bagian Form (Penting: semua di bawah ini harus menjorok ke dalam)
    with st.form("form_utama"):
        nama = st.text_input("Nama Lengkap")
        nik = st.text_input("NIK", max_chars=16)
        
        st.divider()
        
        st.subheader("Deskripsi Pengalaman & Keahlian")
        sektor = st.text_input("Sektor Pekerjaan", placeholder="Misal: Administrasi Desa")
        keahlian = st.text_area("Sebutkan Keahlian Utama", placeholder="1. Kelola Keuangan\n2. Arsip Data")
        narasi = st.text_area("Ceritakan Pengalaman Kerja Anda", height=150)
        
        st.divider()
        
        st.subheader("Bukti Dokumen")
        files = st.file_uploader("Unggah Bukti (SK/Sertifikat)", accept_multiple_files=True)
        
        setuju = st.checkbox("Saya menjamin keaslian data ini.")
        
        submit = st.form_submit_button("Kirim Pengajuan")
        
        if submit:
            if setuju and nama:
                st.success(f"Data {nama} berhasil direkam!")
            else:
                st.error("Mohon isi nama dan centang pernyataan setuju.")
