import streamlit as st
from html import escape

def style_background_home():
    st.markdown(
        """
        <style>
            .stApp{
                background: #5856F2 !important; /* home */
            }
            
            .stApp div[data-testid="stColumn"]{
                background-color : #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp{
                background: #E0E3FF !important; /* dashboard */
            }
            
            
            /* Text input + password input box */
            .stTextInput input {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ddd !important;
                # border-radius: 12px !important;
            }

            /* Placeholder text */
            .stTextInput input::placeholder {
                color: #777 !important;
            }

            /* Focus effect */
            .stTextInput input:focus {
                border: 2px solid #5865F2 !important;
                box-shadow: 0 0 0 2px rgba(88,101,242,0.15) !important;
            }

            /* Password eye icon area */
            [data-testid="stTextInput"] {
                background: transparent !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap');
        
        
            # /*Hide top bar of streamlit */
            # #mainMenu , footer, header{
            #     visibility: hidden;
            # }
            
            # .block-container{
            #     padding-top: 1.5rem !important;
            # }
            
            h1{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
                # color: #000 !important;
            }
            h2{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
                color: #000 !important;
                letter-spacing: 2px !important;
            }

            .head h2{
                color:#5865F2 !important;
            }
            
            
            h3, h4, p{
                font-family: 'Noto Serif', serif !important;
                # font-optical-sizing: auto !important;
                # font-weight: 400 !important;
                # font-style: normal !important;
                color: #000 !important;
            }
        
            .stButton > button{
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            .stButton > button * {
                color: white !important;
            }

            .stButton > button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            .stButton > button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            
            .stButton > button:hover{
                transform:scale(1.05)
            }

            /* Keep Streamlit dialogs readable in both light and dark themes. */
            div[data-testid="stDialog"] div[role="dialog"]{
                background: #FFFFFF !important;
                color: #111827 !important;
            }

            div[data-testid="stDialog"] h1,
            div[data-testid="stDialog"] h2,
            div[data-testid="stDialog"] h3,
            div[data-testid="stDialog"] h4,
            div[data-testid="stDialog"] p,
            div[data-testid="stDialog"] label,
            div[data-testid="stDialog"] span,
            div[data-testid="stDialog"] li,
            div[data-testid="stDialog"] div{
                color: #111827;
            }

            div[data-testid="stDialog"] .stTextInput input,
            div[data-testid="stDialog"] .stTextArea textarea,
            div[data-testid="stDialog"] .stSelectbox input,
            div[data-testid="stDialog"] .stMultiSelect input{
                background-color: #FFFFFF !important;
                color: #111827 !important;
                border: 1px solid #D1D5DB !important;
            }

            div[data-testid="stDialog"] [data-testid="stCodeBlock"],
            div[data-testid="stDialog"] [data-testid="stCode"],
            div[data-testid="stDialog"] pre,
            div[data-testid="stDialog"] pre code{
                background: #1F2430 !important;
                color: #FFFFFF !important;
            }

            div[data-testid="stDialog"] pre,
            div[data-testid="stDialog"] code,
            div[data-testid="stDialog"] [data-testid="stCodeBlock"] *,
            div[data-testid="stDialog"] [data-testid="stCode"] *,
            div[data-testid="stDialog"] pre *,
            div[data-testid="stDialog"] code *{
                color: #FFFFFF !important;
                fill: #FFFFFF !important;
                opacity: 1 !important;
            }

            div[data-testid="stDialog"] button[aria-label="Close"]{
                color: #111827 !important;
            }

            /* Keep Streamlit dataframes readable on the custom dashboard background. */
            div[data-testid="stDataFrame"]{
                background: #FFFFFF !important;
                border-radius: 16px !important;
                overflow: hidden !important;
                border: 1px solid #C7D2FE !important;
            }

            div[data-testid="stDataFrame"] *{
                color: #111827 !important;
            }

            div[data-testid="stDataFrame"] [role="grid"],
            div[data-testid="stDataFrame"] [role="row"],
            div[data-testid="stDataFrame"] [role="columnheader"],
            div[data-testid="stDataFrame"] [role="gridcell"]{
                background: #FFFFFF !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_attendance_table(display_df):
    rows_html = []

    for _, row in display_df.iterrows():
        rows_html.append(
            "<tr>"
            f"<td>{escape(str(row['Time']))}</td>"
            f"<td>{escape(str(row['Subject']))}</td>"
            f"<td>{escape(str(row['Subject Code']))}</td>"
            f"<td>{escape(str(row['Attendance Stats']))}</td>"
            "</tr>"
        )

    st.markdown(
        f"""
        <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:18px; overflow:hidden; margin-top:0.75rem;">
            <table style="width:100%; border-collapse:collapse; color:#111827; font-family:'Noto Serif', serif;">
                <thead>
                    <tr style="background:#FFFFFF;">
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; border-right:1px solid #E5E7EB; font-weight:600;">Time</th>
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; border-right:1px solid #E5E7EB; font-weight:600;">Subject</th>
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; border-right:1px solid #E5E7EB; font-weight:600;">Subject Code</th>
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; font-weight:600;">Attendance Stats</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(rows_html)}
                </tbody>
            </table>
        </div>
        <style>
            table td {{
                background:#FFFFFF;
                padding:14px 16px;
                border-bottom:1px solid #E5E7EB;
                border-right:1px solid #E5E7EB;
                color:#111827;
            }}

            table tbody tr:last-child td {{
                border-bottom:none;
            }}

            table td:last-child,
            table th:last-child {{
                border-right:none !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
