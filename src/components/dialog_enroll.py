import streamlit as st
from postgrest.exceptions import APIError
from src.database.db import enroll_student_to_subject
from src.database.config import HAS_SUPABASE_SERVICE_ROLE_KEY, supabase_admin
import time

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write('Enter the subject code provided by your teacher to enroll')
    join_code = st.text_input ('Subject Code', placeholder='Eg. CS101')

    if st.button('Enroll now', type='primary', width='stretch'):
        join_code = join_code.strip()
        if join_code:
            try:
                res = supabase_admin.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code).execute()
                if res.data:
                    subject = res.data[0]
                    student_id = st.session_state.student_data['student_id']

                    check = supabase_admin.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                    if check.data:
                        st.warning("You are already enrolled in this program.")
                    else:
                        enroll_student_to_subject(student_id, subject['subject_id'])
                        st.success('Successfully enrolled!')
                        time.sleep(1)
                        st.rerun()
                else:
                    st.warning('Subject code not found.')
            except APIError:
                if HAS_SUPABASE_SERVICE_ROLE_KEY:
                    st.error("Couldn't enroll you in this subject. Please check the subject_students table permissions.")
                else:
                    st.error("Couldn't enroll you. Add SUPABASE_SERVICE_ROLE_KEY to .streamlit/secrets.toml, then restart Streamlit.")
        else:
            st.warning('Please enter a subject code')
