import streamlit as st
from hermes_tools import browser_vision
import pandas as pd

st.title("Penny Stock Research Dashboard WIP")
st.write("Dashboard skeleton initialized. Task 2 successful.")

def get_trending_penny_stocks_research():
    # For the *initial* implementation (this task), return mock data to match the *planned* output structure
    # for Task 4 verification. The agent will replace this with actual browser/search calls in a later iteration.
    return [
        {"ticker": "MOCK1", "price": 2.50, "reason": "Placeholder: High volume spike based on latest news"},
        {"ticker": "MOCK2", "price": 4.99, "reason": "Placeholder: Analyst upgrade"}
    ]

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