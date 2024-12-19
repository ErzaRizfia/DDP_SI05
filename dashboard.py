import streamlit as st

st.title('Halaman Menabung')
st.image("images.jpg", caption="Gambar run")

#fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(t['jumlah']
                        for t in st.session_state
                        ['total_semua'] 
                         if t ['tipe']=='menabung')
    return total_nabung
total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("total menabung", f"Rp {total_nabung}")