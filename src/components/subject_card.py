import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
    <div style="background: white; border-left: 8px solid #EB459E; padding: 25px; border-radius: 20px; border: 1px solid black; margin-bottom: 20px; height: 206px; box-sizing: border-box; display: flex; flex-direction: column;">
    <div><h3 style="margin: 0; color: #1e293b; font-size: 1.5rem; line-height:1.5rem; min-height: 60px; overflow-wrap: anywhere;">{name}</h3></div>
    <p style="color: #64748b; margin: 10px 0;">Code: <span style="background: #E0E5FF; color: #5865F2; padding: 2px 8px; border-radius: 5px;">{code}</span> | Section: {section}</p>
    """

    if stats:
        html += """<div style="display:flex; gap:8px; flex-wrap:wrap;">"""
        # html += f"""
        # <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        # """

        for icon, label, value in stats:
            html += f"""<div style="background: #EB459910; padding: 5px 12px; border-radius: 12px; font-size: 0.9rem;">{icon} <b>{value}</b> {label}</div>"""

        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()



# import streamlit as st


# def subject_card(name, code, section, stats=None, footer_callback=None):
#     """Render a subject card with a consistent height and aligned content."""
#     html = f"""
#     <div style="
#         box-sizing: border-box;
#         width: 100%;
#         min-height: 216px;
#         height: 100%;
#         display: flex;
#         flex-direction: column;
#         background: #ffffff;
#         padding: 25px;
#         border: 1px solid #222222;
#         border-left: 8px solid #EB459E;
#         border-radius: 20px;
#         margin-bottom: 20px;
#     ">
#         <h3 style="
#             margin: 0;
#             color: #1e293b;
#             font-size: 1.5rem;
#             line-height: 1.25;
#             min-height: 60px;
#             overflow-wrap: anywhere;
#         ">{name}</h3>

#         <p style="color: #64748b; margin: 10px 0;">
#             Code: <span style="background: #E0E5FF; color: #5865F2; padding: 2px 8px; border-radius: 5px;">{code}</span>
#             | Section: {section}
#         </p>
#     """

#     if stats:
#         html += '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: auto; padding-top: 4px;">'
#         for icon, label, value in stats:
#             html += f"""
#                 <div style="
#                     background: #EB459910;
#                     padding: 5px 12px;
#                     border-radius: 12px;
#                     font-size: 0.9rem;
#                     white-space: nowrap;
#                 ">{icon} <b>{value}</b> {label}</div>
#             """
#         html += "</div>"

#     html += "</div>"
#     st.markdown(html, unsafe_allow_html=True)

#     if footer_callback:
#         footer_callback()
