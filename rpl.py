import streamlit as st

# Setup Page (Supaya tampilannya Wide dan judul Tab-nya bagus)
st.set_page_config(page_title="RPL Unisba", page_icon="🎓", layout="wide")

# --- HEADER SECTION ---
col1, col2 = st.columns([1, 5])
with col1:
    # Pastikan file logo_unisba.png ada di folder yang sama, atau bisa di-comment dulu
    st.image("https://upload.wikimedia.org/wikipedia/id/8/8c/Logo_Unisba.png", width=100) 
with col2:
    st.title("Portal Rekognisi Pembelajaran Lampau (RPL)")
    st.subheader("Universitas Islam Bandung")

st.divider()

# --- MODUL 1: DESKRIPSI & INFORMASI ---
st.markdown("### 👋 Selamat Datang di Jalur RPL Tipe A")

st.info("""
**Apa itu RPL Tipe A?** RPL adalah pengakuan atas Capaian Pembelajaran seseorang yang diperoleh dari **pendidikan nonformal, informal, dan/atau pengalaman kerja** sebagai dasar untuk melanjutkan pendidikan formal. 
""")

with st.expander("📖 Landasan Hukum & Manfaat", expanded=True):
    st.write("""
    Program ini merujuk pada **Keputusan Direktur Jenderal Pendidikan Tinggi No. 112/B/KPT/2025**.
    
    **Manfaat untuk Anda:**
    * **Efisiensi Waktu:** Tidak perlu mengambil mata kuliah yang sudah Anda kuasai di lapangan.
    * **Pengakuan Profesional:** Pengalaman kerja bertahun-tahun dihargai secara akademik.
    * **Biaya Hemat:** SKS yang diakui akan mengurangi total biaya perkuliahan.
    """)

# --- MODUL 1: PRE-SCREENING (CEK KELAYAKAN) ---
st.markdown("---")
st.markdown("### 🔍 Cek Kelayakan Awal")
st.write("Silakan isi data singkat di bawah ini untuk melihat potensi pengakuan SKS Anda.")

c1, c2 = st.columns(2)
with c1:
    ijazah = st.selectbox("Ijazah Terakhir", 
                        ["Pilih Ijazah", "SMA/SMK/MA Sederajat", "Diploma (D1/D2/D3)", "Pernah Kuliah (Putus Studi)"])
    masa_kerja = st.number_input("Total Masa Kerja (Tahun)", min_value=0, max_value=40, step=1)

with c2:
    bidang = st.text_input("Bidang Pekerjaan (Contoh: Perbankan, Guru, Admin)")
    st.caption("Pilih bidang yang paling dominan dalam karir Anda.")

if st.button("Analisis Potensi Saya"):
    if ijazah == "Pilih Ijazah":
        st.error("Mangga pilih ijazah terakhir Akang/Teteh dulu.")
    elif masa_kerja < 2:
        st.warning("⚠️ Berdasarkan pedoman, masa kerja di bawah 2 tahun memiliki potensi pengakuan yang terbatas. Disarankan minimal 2 tahun pengalaman relevan.")
    else:
        st.success(f"🚀 Hasil Analisis: Anda memiliki potensi tinggi untuk program RPL di bidang {bidang}!")
        st.balloons()
# --- REVISI MODUL 2: BAGIAN KLAIM BERBASIS NARASI ---

with tab2:
    st.header("Formulir E-Portofolio RPL")
    
    with st.form("form_rpl_narasi"):
        st.subheader("1. Identitas Pelamar")
        nama = st.text_input("Nama Lengkap")
        nik = st.text_input("NIK", max_chars=16)

        st.divider()

        # Bagian ini yang kita buat jadi Free-Text
        st.subheader("2. Deskripsi Profesional")
        st.info("Tuliskan bidang pekerjaan dan keahlian utama yang Anda kuasai. Penjelasan ini akan membantu kami memetakan pengalaman Anda ke mata kuliah yang relevan.")
        
        sektor_mandiri = st.text_input("Sektor/Bidang Pekerjaan Anda", 
                                      placeholder="Contoh: Perbankan Syariah, Industri Kreatif, Aparatur Desa, dll.")
        
        keahlian_utama = st.text_area("Sebutkan Kemampuan/Keahlian Utama Anda", 
                                      placeholder="Contoh: Penyusunan laporan keuangan, Manajemen stok barang, Analisis risiko kredit, dll.",
                                      help="Sebutkan minimal 3 kemampuan teknis yang Anda kuasai di pekerjaan.")

        narasi_portofolio = st.text_area("Uraikan Pengalaman Kerja Anda (Kontekstual)", 
                                         placeholder="Ceritakan detail tugas harian Anda yang menurut Anda setara dengan materi perkuliahan...",
                                         height=200)

        st.divider()

        st.subheader("3. Bukti Pendukung")
        uploaded_files = st.file_uploader("Unggah Sertifikat, SK, atau Portofolio", accept_multiple_files=True)

        st.warning("Pastikan data asli. Ketidaksesuaian data dapat membatalkan proses RPL.")
        setuju = st.checkbox("Saya menjamin keaslian dokumen ini.")

        btn_kirim = st.form_submit_button("Kirim Pengajuan")

        if btn_kirim:
            if not setuju:
                st.error("Centang dulu pernyataan keasliannya ya, Kang.")
            else:
                st.success("Data berhasil direkam. Tim Asesor akan melakukan pemetaan (mapping) terhadap narasi Anda.")
