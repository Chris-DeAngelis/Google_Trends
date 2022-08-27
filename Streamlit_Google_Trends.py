# Testing streamlit with FRED
import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
#import numpy as np

# streamlit specs
st.set_page_config(layout="wide")
#st.sidebar.title("Control Panel")
#st.sidebar.subheader("Prior belief about the click rate")

st.title('Google Trends')

# Pytrend connection and settings
con_trends = TrendReq(hl='es-US', tz=360)
# for proxy skirting
#pytrends = TrendReq(hl='en-US', tz=360, timeout=(3,12), proxies=['https://192.128.156.13:80',], retries=1, backoff_factor=0.1, requests_args={'verify':False})
'''
The timeout attribute is from the Requests Library of Python. The first argument is for “connecting”, the second one is for “read”. If a connection try lasts more than 3 seconds and a reading of the request lasts more than 12 seconds, it will give a timeout error.
Proxies attribute is for stating the proxies which will be used for the request, the port number is obligatory.
“Retries” is the number of retrying chances after the first failed request.
Requests_args parameter is to comply with the nature of the request, false means ignore SSL.
Backoff_factor is the time period between retries.
'''

# Read in search terms and organize for Google Trends API queries
search_data = pd.read_csv('https://raw.githubusercontent.com/topherdea/Google_Trends/main/Google%20Trends%20Template.csv')

def google_trend(kw_list, cat=0, timeframe='today 5-y', geo='us', gprop=''):
    '''Download Google Trends data'''
    #con_trends.get_historical_interest(kw, year_start=2020, month_start=7, day_start=15, hour_start=0, year_end=2020, month_end=7, day_end=17, hour_end=23, cat=0, geo='US', gprop='', sleep=0)
    #con_trends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
    #con_trends.related_topics().values()
    #con_trends.related_queries()
    #con_trends.suggestions()
    con_trends.build_payload(kw_list, cat=cat, timeframe=timeframe, geo=geo, gprop=gprop)
    return(con_trends.interest_over_time())

# Collect data
@st.experimental_memo(ttl=600)
def run_query():
    temp_kw = ['Donald Trump', 'Football']
    data = google_trend(temp_kw, 
                        timeframe = 'today 3-m', 
                        geo='US')
    df = pd.DataFrame(data)
    return df

all_rows = run_query()
#df.columns = field_names
st.table(all_rows.tail())

# Output data
#print(data.head())
st.subheader('More features coming soon...')
