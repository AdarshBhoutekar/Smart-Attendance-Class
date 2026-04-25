import streamlit as st

from supabase import create_client, Client

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

SUPABASE_SERVICE_ROLE_KEY = st.secrets.get("SUPABASE_SERVICE_ROLE_KEY")
HAS_SUPABASE_SERVICE_ROLE_KEY = bool(SUPABASE_SERVICE_ROLE_KEY)

supabase_admin: Client = create_client(
    st.secrets["SUPABASE_URL"],
    SUPABASE_SERVICE_ROLE_KEY or st.secrets["SUPABASE_KEY"]
)
