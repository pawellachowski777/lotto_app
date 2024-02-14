import requests
from bs4 import BeautifulSoup
import pandas as pd

def download_lotto():
    url = 'https://megalotto.pl/wyniki/multi-multi/'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_list_latest = soup.find('div', class_=['lista_ostatnich_losowan'])
    numbers = []
    df = pd.DataFrame()

    for losowanie in soup_list_latest.find_all('ul'):
        df_day = pd.DataFrame()
        date = losowanie.find(class_='date_in_list').text

        result_first = losowanie. \
            find(class_='pierwszy_wiersz_z_kulkami_w_muliti_multi'). \
            find_all(class_='numbers_in_list')

        df_line = pd.DataFrame()
        numbers = [int(x.text.strip()) for x in result_first]

        result_next = losowanie.find_all(class_='kolejny_wiersz_z_kulkami_w_muliti_multi')
        list_result = []
        for number_list in result_next:
            number_line = number_list.find_all(class_='numbers_in_list')
            for number in number_line:
                list_result.append(number.text.strip())

        numbers = [n for n in list_result]
        df_day['wylosowana_liczba'] = numbers
        df_day['data'] = pd.to_datetime(date, dayfirst=True).date()
        # df_day['data'] = date

        df = pd.concat([df, df_day])

    return df
