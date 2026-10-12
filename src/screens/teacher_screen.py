import streamlit as st

from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.footer import footer_dashboard

from src.database.db import create_teacher, check_teacher_exists, teacher_login

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    
    st.header(f"""Welcome, {teacher_data['name']}""")

def login_teacher(username, pwd):
    if not username or not pwd:
        return False
    teacher = teacher_login(username, pwd)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False

def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="login_back_button", shortcut="ctrl+h"):
                st.session_state['login_type'] = None
                st.rerun()

    st.header("Login using password", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input("Enter username: ", key="teacher_username", placeholder="Enter your username", type="default")
    teacher_password = st.text_input("Enter password: ", key="teacher_password", placeholder="Enter your password", type="password")

    st.divider()

    bc1, bc2 = st.columns(2, gap="large")
    with bc1:
        if st.button("Login", icon=':material/passkey:', shortcut="ctrl+enter", width='stretch'):
            if login_teacher(teacher_username, teacher_password):
                st.toast("Welcome Back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Username and Password combination", icon="⚠️")
    with bc2:
        if st.button("Register Instead", icon=':material/passkey:', width='stretch', type='primary'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()

    footer_dashboard()


def register_teacher(username, name, password, password_confirm):
    if not username or not name or not password or not password_confirm:
        return False, "Please fill in all fields."
    if check_teacher_exists(username):
        return False, "Username already exists."
    if password != password_confirm:
        return False, "Password doesn't match"

    try:
        create_teacher(username, password, name)
        return True, "Successfully Created! Login Now"
    except Exception as e:
        return False, "Unexpected Error!"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="login_back_button1", shortcut="ctrl+h"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Register your teacher profile", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input("Enter username: ", key="teacher_username", placeholder="Enter your username", type="default")
    teacher_name = st.text_input("Enter name: ", key="teacher_name", placeholder="Enter your name", type="default")
    teacher_password = st.text_input("Enter password: ", key="teacher_password", placeholder="Enter your password", type="password")
    teacher_password_confirm = st.text_input("Confirm password: ", key="teacher_password_confirm", placeholder="Confirm your password", type="password")

    st.divider()

    bc1, bc2 = st.columns(2, gap="large")
    with bc1:
        if st.button("Register Now", icon=':material/passkey:', shortcut="ctrl+enter", width='stretch'):
            success, message = register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)
    with bc2:
        if st.button("Login Instead", icon=':material/passkey:', width='stretch', type='primary'):
            st.session_state.teacher_login_type = 'login'
            st.rerun()

    footer_dashboard()