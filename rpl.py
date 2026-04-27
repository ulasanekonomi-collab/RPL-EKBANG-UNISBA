import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="RPL Unisba - Yuhkasun", 
    page_icon="🎓", 
    layout="wide"
)

# 2. HEADER & LOGO
col1, col2 = st.columns([1, 5])
with col1:
    # Menggunakan URL logo Unisba
    st.image("https://upload.wikimedia.org/wikipedia/id/8/8c/Logo_Unisba.png", width=100) 
with col2:
    st.title("Portal Rekognisi Pembelajaran Lampau (RPL)")
    st.subheader("Universitas Islam Bandung")

st.divider()

# 3. NAVIGASI TAB
tab1, tab2 = st.tabs(["📋 Informasi & Cek Kelayakan", "📤 Pengajuan E-Portofolio"])

# --- TAB 1: INFORMASI ---
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
        * **Pengakuan Profesional:** Kompetensi lapangan Anda dihargai secara akademis.
        """)

    st.markdown("---")
    st.subheader("🔍 Cek Kelayakan Awal")
    st.write("Cek potensi Anda sebelum melakukan pendaftaran resmi.")
    
    c1, c2 = st.columns(2)
    with c1:
        ijazah = st.selectbox("Ijazah Terakhir", ["Pilih Ijazah", "SMA/SMK/MA Sederajat", "Diploma (D1/D2/D3)", "Pernah Kuliah (Putus Studi)"])
        masa_kerja = st.number_input("Total Masa Kerja (Tahun)", min_value=0, max_value=40, step=1)
    with c2:
        bidang_kerja = st.text_input("Bidang Pekerjaan Dominan", placeholder="Contoh: Perbankan, Administrasi, dll")

    if st.button("Analisis Potensi Saya"):
        if ijazah == "Pilih Ijazah":
            st.error("Silakan pilih ijazah terakhir Anda.")
        elif masa_kerja >= 2:
            st.success(f"🚀 Luar Biasa! Pengalaman Anda di bidang {bidang_kerja} selama {masa_kerja} tahun memiliki potensi tinggi untuk dikonversi menjadi SKS.")
            st.balloons()
        else:
            st.warning("Berdasarkan pedoman, disarankan memiliki masa kerja minimal 2 tahun untuk hasil maksimal.")

# --- TAB 2: FORMULIR E-PORTOFOLIO ---
with tab2:
    st.header("Formulir E-Portofolio RPL")
    st.write("Isi narasi keahlian Anda secara mandiri di bawah ini.")

    with st.form("form_pendaftaran_rpl"):
        # Identitas
        st.subheader("1. Identitas Pelamar")
        nama_lengkap = st.text_input("Nama Lengkap (Sesuai Ijazah)")
        nik_user = st.text_input("Nomor Induk Kependudukan (NIK)", max_chars=16)
        
        st.divider()
        
        # Narasi Keahlian
        st.subheader("2. Deskripsi Pengalaman Profesional")
        st.caption("Ceritakan dunia kerja Anda dengan bahasa sendiri.")
        
        sektor_pekerjaan = st.text_input("Sektor/Bidang Pekerjaan", placeholder="Misal: Keuangan Mikro, Kewirausahaan Kuliner, dll")
        keahlian_list = st.text_area("Sebutkan 3 Keahlian Utama Anda", placeholder="1. Analisis Laporan Keuangan\n2. Manajemen Operasional\n3. Strategi Pemasaran")
        cerita_kerja = st.text_area("Uraikan Pengalaman Kerja Anda secara Detail", height=200, 
                                    placeholder="Jelaskan tugas harian Anda yang menurut Anda setara dengan materi kuliah...")
        
        st.divider()
        
        # Upload Bukti
        st.subheader("3. Unggah Bukti Kompetensi")
        uploaded_docs = st.file_uploader("Unggah SK Kerja, Sertifikat, atau Portofolio (PDF/JPG)", accept_multiple_files=True)
        
        st.warning("PENTING: Pastikan semua data yang Anda masukkan adalah benar dan dokumen yang diunggah adalah asli.")
        pernyataan = st.checkbox("Saya menjamin keaslian dokumen dan data yang saya kirimkan.")
        
        # Submit Button
        submit_final = st.form_submit_button("Kirim Pengajuan RPL")
        
        if submit_final:
            if not pernyataan:
                st.error("Anda harus menyetujui pernyataan keaslian data.")
            elif not nama_lengkap or not cerita_kerja:
                st.error("Nama dan Deskripsi Pengalaman tidak boleh kosong.")
            else:
                st.success(f"Alhamdulillah, data {nama_lengkap} telah berhasil direkam dalam sistem!")
                st.info("Tim Asesor Universitas Islam Bandung akan segera melakukan pemetaan terhadap narasi Anda.")

# 4. FOOTER (Catatan Pengembangan)
st.divider()
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: gray;
        text-align: center;
        font-style: italic;
        padding: 10px;
    }
    </style>
    <div class="footer">
    Dikembangkan oleh Yuhkasun © 2026
    </div>
    """, 
    unsafe_allow_html=True
)
