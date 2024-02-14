import streamlit as st
from download_data import download_lotto
import numpy as np

def main():

    df = download_lotto()
    date = st.date_input('Wybierz datę losowania', format='YYYY-MM-DD')
    your_numbers = st.multiselect('Twoje liczby', range(1, 99))
    st.write(date)

    df_select = df.loc[df['data'] == date]

    guessed = df_select[df_select['wylosowana_liczba'].isin(your_numbers)]
    st.write('trafiłeś', guessed['wylosowana_liczba'])

    st.dataframe(df_select)


if __name__ == "__main__":
    main()
