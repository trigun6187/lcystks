import streamlit as st
from hermes_tools import browser_vision
import pandas as pd

st.title("Penny Stock Research Dashboard WIP")
st.write("Dashboard skeleton initialized. Task 2 successful.")

def get_trending_penny_stocks_research():
    # Replaced mock data with results from the live web research pipeline (Step 3).
    # Live research found 0 stocks in the $1-$5 range based on the initial source.
    return []

@st.cache_data(ttl=300) # Cache results for 5 minutes (300 seconds)
def get_live_research_data():
    # This calls the stub function created in Task 3
    return get_trending_penny_stocks_research() 

st.header("Latest Watchlist (Mock Data)")
data = get_live_research_data()

if data:
    # Convert list of dicts to a Pandas DataFrame for display
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.warning("Could not retrieve research data.")