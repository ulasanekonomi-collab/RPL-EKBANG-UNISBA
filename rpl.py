import streamlit as st
import pandas as pd
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="RPL Unisba - Yuhkasun", 
    page_icon="🎓", 
    layout="wide"
)

# 2. HEADER TUNGGAL (Hanya satu di sini, Kang!)
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/id/8/8c/Logo_Unisba.png", width=100) 
with col2:
    st.title("Portal Rekognisi Pembelajaran Lampau (RPL)")
    st.subheader("Universitas Islam Bandung")

st.divider()

# 3. NAVIGASI TAB
tab1, tab2, tab3 = st.tabs([
    "📋 Informasi & Cek Kelayakan", 
    "📤 Pengajuan E-Portofolio", 
    "📊 Panel Asesor"
])

# --- TAB 1: INFORMASI & CEK KELAYAKAN ---
with tab1:
    st.markdown("### 👋 Selamat Datang di Jalur RPL Tipe A")
    st.info("""
    **Apa itu RPL Tipe A?** RPL adalah pengakuan atas Capaian Pembelajaran seseorang yang diperoleh dari 
    **pendidikan nonformal, informal, dan/atau pengalaman kerja** sebagai dasar untuk melanjutkan pendidikan formal.
    """)
    
    with st.expander("📖 Lihat Manfaat & Landasan Hukum"):
        st.write("""
        Program ini merujuk pada **Keputusan Direktur Jenderal Pendidikan Tinggi No. 112/B/KPT/2025**.
        
        **Manfaat Utama:**
        * **Efisiensi Waktu:** Pengalaman kerja dikonversi menjadi SKS.
        * **Biaya Hemat:** Mengurangi jumlah mata kuliah yang harus diambil.
        """)

    st.markdown("---")
    st.subheader("🔍 Cek Kelayakan Awal")
    c1, c2 = st.columns(2)
    with c1:
        ijazah = st.selectbox("Ijazah Terakhir", ["Pilih Ijazah", "SMA/SMK/MA Sederajat", "Diploma", "Putus Studi"])
        masa_kerja = st.number_input("Total Masa Kerja (Tahun)", min_value=0, max_value=40, step=1)
    with c2:
        bidang_kerja = st.text_input("Bidang Pekerjaan Dominan", placeholder="Contoh: Perbankan, Administrasi")

    if st.button("Analisis Potensi Saya"):
        if masa_kerja >= 2:
            st.success(f"🚀 Potensi Tinggi! Pengalaman di {bidang_kerja} sangat mendukung.")
            st.balloons()
        else:
            st.warning("Disarankan minimal 2 tahun masa kerja sesuai pedoman.")

# --- TAB 2: FORMULIR E-PORTOFOLIO ---
with tab2:
    st.header("Formulir E-Portofolio RPL")
    
    with st.form("form_rpl_utama"):
        st.subheader("1. Identitas & Deskripsi")
        nama_lengkap = st.text_input("Nama Lengkap")
        nik_user = st.text_input("NIK", max_chars=16)
        
        st.divider()
        sektor_pekerjaan = st.text_input("Sektor Pekerjaan")
        keahlian_list = st.text_area("Sebutkan Keahlian Utama (List)")
        cerita_kerja = st.text_area("Uraikan Pengalaman Kerja secara Detail", height=200)
        
        st.divider()
        st.subheader("2. Bukti Dokumen")
        uploaded_docs = st.file_uploader("Unggah Bukti (PDF/JPG)", accept_multiple_files=True)
        
        pernyataan = st.checkbox("Saya menjamin keaslian dokumen.")
        submit_final = st.form_submit_button("Kirim Pengajuan RPL")
        
        if submit_final:
            if pernyataan and nama_lengkap:
                # Logika Simpan ke CSV
                nama_file = "data_pendaftar_rpl.csv"
                data_baru = {
                    "Nama": [nama_lengkap],
                    "NIK": [nik_user],
                    "Sektor": [sektor_pekerjaan],
                    "Keahlian": [keahlian_list],
                    "Narasi_Pengalaman": [cerita_kerja]
                }
                df_baru = pd.DataFrame(data_baru)
                
                if not os.path.isfile(nama_file):
                    df_baru.to_csv(nama_file, index=False)
                else:
                    df_baru.to_csv(nama_file, mode='a', index=False, header=False)
                
                st.success(f"Data {nama_lengkap} berhasil disimpan!")
            else:
                st.error("Mohon lengkapi data dan centang pernyataan keaslian.")

# --- TAB 3: PANEL ASESOR ---
with tab3:
    st.header("Halaman Khusus Asesor")
    nama_file = "data_pendaftar_rpl.csv"

    if os.path.exists(nama_file):
        df_admin = pd.read_csv(nama_file)
        st.write(f"Total Pengajuan: **{len(df_admin)}**")
        st.dataframe(df_admin, use_container_width=True)
        
        st.divider()
        st.subheader("Aksi Penilaian")
        pilih_nama = st.selectbox("Pilih Pendaftar:", df_admin["Nama"].tolist())
        
        if pilih_nama:
            user_data = df_admin[df_admin["Nama"] == pilih_nama].iloc[0]
            st.info(f"**Narasi {pilih_nama}:**\n\n{user_data['Narasi_Pengalaman']}")
            
            c_a, c_b = st.columns(2)
            with c_a:
                sks = st.number_input("SKS Diakui", 0, 24)
            with c_b:
                status = st.selectbox("Status", ["Menunggu", "Disetujui", "Ditolak"])
            
            if st.button("Simpan Penilaian"):
                st.success("Penilaian berhasil dicatat!")
    else:
        st.info("Belum ada data pendaftar.")

# 4. FOOTER
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-style: italic;'>Dikembangkan oleh Yuhkasun © 2026</p>", unsafe_allow_html=True)
