import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    
    style_background_dashboard()
    style_base_layout()
    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type =='register':
        teacher_screen_register()
        
    
def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut='Ctrl+Backspace'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header("Login with email", text_alignment='center')
    st.space()
    st.space()
    
    teacher_username = st.text_input("Enter username", placeholder="abc@gmail.com")
    teacher_pass = st.text_input("Enter Password", type='password', placeholder="Enter your password")

    st.divider()
    
    btnc1, btnc2 = st.columns(2)
    
    with btnc1:
        st.button("Login", icon=':material/passkey:', shortcut='Ctrl+Enter', width='stretch')
    
    with btnc2:
        if st.button("Register Now", type='primary', icon=':material/passkey:', shortcut='Ctrl+Enter', width='stretch'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()
        
    footer_dashboard()
    
    
def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut='Ctrl+Backspace'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header("Register your Teacher Profile")
    st.space()
    st.space()
    
    teacher_username = st.text_input("Enter username", placeholder="abc@gmail.com")
    teacher_name = st.text_input("Enter name", placeholder="Sanam")
    
    teacher_pass = st.text_input("Enter Password", type='password', placeholder="Enter your password")
    Confirm_Password = st.text_input("Confirm Password", type='password', placeholder="Enter password again")

    st.divider()
    
    btnc1, btnc2 = st.columns(2)
    
    with btnc1:
        st.button("Register now", icon=':material/passkey:', shortcut='Ctrl+Enter', width='stretch')
    
    with btnc2:
        if st.button("Login instead", type='primary', icon=':material/passkey:', shortcut='Ctrl+Enter', width='stretch'):
            st.session_state.teacher_login_type = 'login'
            st.rerun()
    
    footer_dashboard()
