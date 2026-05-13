import streamlit as st
from html import escape


def subject_card(name, code, section, stats=None, footer_callback=None):
    safe_name = escape(str(name))
    safe_code = escape(str(code))
    safe_section = escape(str(section))

    html = (
        '<div style="background:white; border-left: 8px solid #EB459E; padding:25px; '
        'border-radius: 20px; border: 1px solid black; margin-bottom:20px;">'
        f'<h3 style="margin:0; color: #1e293b; font-size: 1.5rem ">{safe_name}</h3>'
        '<p style="color:#1f2937; margin: 10px 0;">'
        f'Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius: 5px;">{safe_code} | Section : {safe_section}</span>'
        '</p>'
    )
    if stats:
        html += '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            safe_icon = escape(str(icon)).strip()
            safe_label = escape(str(label))
            safe_value = escape(str(value))
            icon_html = f'{safe_icon} ' if safe_icon else ''
            html += (
                '<div style="background:#FCE7F3; color:#111827; padding:5px 12px; '
                'border-radius:12px; font-size:0.9rem; border:1px solid #FBCFE8;">'
                f'{icon_html}<b style="color:#111827;">{safe_value}</b> <span style="color:#111827;">{safe_label}</span></div>'
            )

        html += "</div>"
    
    html += "</div>"
    
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
