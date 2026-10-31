
import streamlit as st


@st.dialog("Attendance Details")
def show_attendance_dialog(subject_name, logs):
    st.subheader(subject_name)

    if not logs:
        st.info("No attendance records found.")
        return

    attended = sum(1 for log in logs if log.get("is_present"))
    total = len(logs)

    for i, log in enumerate(logs, start=1):
        if log.get("is_present"):
            st.success(f"Class {i} — Attended")
        else:
            st.error(f"Class {i} — Missed")

    st.divider()
    st.metric("Classes Attended / Total Classes", f"{attended}/{total}")
    st.progress(attended / total)
