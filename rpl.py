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
# Ganti bagian multiselect MK yang kaku tadi dengan ini:

st.subheader("2. Portofolio Pengalaman")
st.info("Pilih bidang pengalaman yang Anda miliki. Kami akan membantu memetakan ke kurikulum kami.")

bidang_exp = st.selectbox("Sektor Pengalaman Dominan:", 
                         ["Pilih Sektor", "Perbankan & Keuangan", "Wirausaha/UMKM", "Administrasi Publik", "Analisis Data/Statistik"])

if bidang_exp == "Perbankan & Keuangan":
    st.write("👉 **Kompetensi yang dapat diakui:** Analisis Kredit, Manajemen Risiko, Operasional Bank.")
    st.caption("Potensi Mata Kuliah: Manajemen Perbankan, Ekonomi Moneter, Akuntansi.")
    
elif bidang_exp == "Wirausaha/UMKM":
    st.write("👉 **Kompetensi yang dapat diakui:** Perencanaan Bisnis, Strategi Pemasaran, Kelayakan Investasi.")
    st.caption("Potensi Mata Kuliah: Kewirausahaan, Manajemen Pemasaran, Evaluasi Proyek.")

# Biarkan user mengisi narasi kompetensi, bukan memilih kode MK yang membingungkan
kemampuan = st.multiselect("Kemampuan apa saja yang Anda kuasai secara profesional?", 
                          ["Menyusun Laporan Keuangan", "Melakukan Analisis Pasar", "Mengelola SDM", "Menggunakan Software Statistik", "Perencanaan Anggaran"])

deskripsi_pengalaman = st.text_area("Deskripsikan detail pekerjaan/tugas yang mendukung kemampuan tersebut:", 
                                     placeholder="Ceritakan aktivitas harian Anda yang relevan...")
