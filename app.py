import streamlit as st 

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
      "Menu utama" : [dashboard],
      "Transaksi" :[nabung],

    }
)
if 'total_semua' not in st.session_state:
    st.session_state['total_semua']=[]
pg.run()