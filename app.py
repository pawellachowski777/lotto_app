import streamlit as st
from download_data import download_lotto


def main():

    df = download_lotto()
    date = st.date_input('Wybierz datę losowania', format='YYYY-MM-DD')
    st.write(date)
    df_select = df.loc[df['data'] == date]
    st.dataframe(df_select)


if __name__ == "__main__":
    main()
