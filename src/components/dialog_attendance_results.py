import streamlit as st
from src.database.db import enroll_student_to_subject, create_attendance
from src.database.config import supabase
import time


@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    st.write("Please review attendance before conforming.")
    st.dataframe(df, hide_index=True, width='stretch')
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Discard", width='stretch'):
            st.rerun()
            
    with col2:
        if st.button("Confirm & Save", width='stretch', type='primary'  ):
            try:
                create_attendance(logs)
                st.toast("Attendance Taken!")
                st.session_state.attendance_images = []
                st.rerun()
            except Exception as e:
                st.error("Sync failed!")