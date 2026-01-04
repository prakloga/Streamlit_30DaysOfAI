import streamlit as st

st.title(":material/vpn_key: Day 1: Connect to Snowflake")

# Connect to Snowflake
try:
    #works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()

except:
    #works locally and Streamlit Community Edition
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# Query Snowflake version
version = session.sql("select current_version()").collect()[0][0]

# Display results
st.success(f"Successfully connected! Snowflake version: {version}")