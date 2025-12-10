import streamlit as st

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('Pilih aplikasi',['luas persegi','luas segitiga','luas lingkaran'])

if menu == 'luas persegi':
    st.write('ini halam untuk menghitung luas persegi')
    st.image('https://awsimages.detik.net.id/community/media/visual/2022/11/09/keliling-persegi_169.jpeg?w=650&q=90',caption='gambar persegi')
    sisi = st.number_input('silahkan masukan sisi', min_value=0)
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write('ini halam untuk menghitung luas segitiga')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/06/rumus-luas-segitiga-sama-sisi.jpg',caption='gambar segitiga')

elif menu == 'luas lingkaran':
    st.write('ini halam untuk menghitung luas lingkaran')