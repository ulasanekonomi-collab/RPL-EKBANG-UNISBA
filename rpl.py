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
# --- LANJUTAN KODE DI rpl.py ---

st.markdown("---")
# Membuat Tab agar navigasi lebih enak dilihat
tab1, tab2 = st.tabs(["📋 Informasi & Cek Kelayakan", "📤 Pengajuan E-Portofolio"])

with tab1:
    st.write("Silakan gunakan form di atas untuk mengecek kelayakan awal.")
    # (Kode cek kelayakan yang tadi sudah ada di sini otomatis kalau kita pindahkan ke tab)

with tab2:
    st.header("Formulir E-Portofolio RPL")
    st.write("Lengkapi data dan unggah bukti kompetensi Anda di bawah ini.")

    with st.form("form_rpl"):
        # 1. Identitas
        st.subheader("1. Identitas Pelamar")
        nama = st.text_input("Nama Lengkap (Sesuai Ijazah)")
        nik = st.text_input("Nomor Induk Kependudukan (NIK)", max_chars=16)
        
        # 2. Mata Kuliah yang Diklaim
        st.subheader("2. Klaim Mata Kuliah")
        st.info("Pilih mata kuliah yang menurut Anda relevan dengan pengalaman kerja Anda.")
        
        mk_pilihan = st.multiselect("Pilih Mata Kuliah:", 
                                   ["Ekonomi Makro", "Manajemen Keuangan", "Kewirausahaan", "Pemasaran Digital", "Akuntansi Dasar"])
        
        deskripsi_pengalaman = st.text_area("Jelaskan secara singkat mengapa Anda layak mendapatkan pembebasan MK tersebut:", 
                                         placeholder="Contoh: Saya sudah bekerja sebagai Manajer Keuangan selama 5 tahun...")

        # 3. Unggah Berkas Bukti
        st.subheader("3. Unggah Bukti Kompetensi")
        st.caption("Unggah bukti berupa CV, Sertifikat Pelatihan, SK Kerja, atau Portofolio (Format PDF/JPG)")
        uploaded_files = st.file_uploader("Pilih Berkas", accept_multiple_files=True)

        # 4. Pernah Dokumen (Penting menurut Juknis!)
        st.warning("Pastikan seluruh dokumen yang Anda unggah adalah asli dan dapat dipertanggungjawabkan secara hukum.")
        setuju = st.checkbox("Saya menyatakan bahwa data yang saya berikan adalah benar.")

        submit_button = st.form_submit_button("Kirim Pengajuan RPL")

        if submit_button:
            if not setuju:
                st.error("Silakan centang kotak pernyataan keaslian dokumen dulu, Kang.")
            elif not nama or not nik:
                st.error("Nama dan NIK jangan dikosongkan ya.")
            else:
                st.success(f"Alhamdulillah, data atas nama {nama} berhasil dikirim! Tim Asesor akan segera memeriksa dokumen Anda.")
                # Di sini nanti bisa ditambah fungsi untuk simpan ke database atau kirim email
