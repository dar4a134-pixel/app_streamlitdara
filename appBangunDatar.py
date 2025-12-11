import streamlit as st
# Fungsi untuk menghitung luas bangun datar
def persegi(sisi):
    return sisi * sisi

def segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def lingkaran(jari2):
    return 3.14 * jari2 * jari2

def persegi_panjang(panjang, lebar):
    return panjang * lebar

# Halaman Utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.title('Buatan anak SI')

# Sidebar navigasi
menu = st.sidebar.selectbox('Menu', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran', 'luas persegi panjang'])

if menu == 'Luas Persegi':
    st.subheader('Hitung Luas Persegi')
    
    st.image(
        "https://www.doyanblog.com/wp-content/uploads/2021/12/rumus-persegi.jpg.webp",
        caption="Ilustrasi Persegi",
        width=300,
    )
    input_sisi = st.number_input('silahkan Masukkan Sisi', min_value=0)
    if st.button('Hitung Luas Persegi'):
        if input_sisi > 0:
            luas = persegi(input_sisi)
            st.write(f"Luas persegi adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai sisi yang lebih besar dari 0!')

elif menu == 'Luas Segitiga':
    st.subheader('Hitung Luas Segitiga')

    st.image(
        "https://fti.ars.ac.id/img-blog/cara-mengitung-luas-segitiga-dengan-bahasa-pemograman-c",
        caption="Ilustrasi Segitiga",
        width=300,
    )
    input_alas = st.number_input('Masukkan Alas', min_value=0)
    input_tinggi = st.number_input('Masukkan Tinggi', min_value=0)

    if st.button('Hitung Luas Segitiga'):
        if input_alas > 0 and input_tinggi > 0:
            luas = segitiga(input_alas, input_tinggi)
            st.write(f"Luas segitiga adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai alas dan tinggi yang lebih besar dari 0!')

elif menu == 'Luas Lingkaran':
    st.subheader('Hitung Luas Lingkaran')

    st.image(
        "https://i.pinimg.com/736x/e3/ec/fc/e3ecfc747bbfe1186aa4992e19ea8596.jpg",
        caption="Ilustrasi Lingkaran",
        width=300,
    )
    input_jari2 = st.number_input('Masukkan Jari-Jari', min_value=0)

    if st.button('Hitung Luas Lingkaran'):
        if input_jari2 > 0:
            luas = lingkaran(input_jari2)
            st.write(f"Luas lingkaran adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai jari-jari yang lebih besar dari 0!')

elif menu == 'luas persegi panjang':
    st.subheader('hitung luas persegi panjang')

    st.image(
        "https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi-panjang.jpg.webp",
        caption="Ilustrasi Lingkaran",
        width=300,
    )
    input_panjang = st.number_input ('masukkan panjang', min_value= 0)
    input_lebar = st.number_input ('masukkan lebar', min_value= 0)
    if st.button('hitung luas persegi panjang'):
        if input_panjang > 0 and input_lebar > 0:
            luas = persegi_panjang (input_panjang, input_lebar)
            st.write (f'luas persegi panjang adalah : {luas: 2f}')
    