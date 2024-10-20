import streamlit as st
from demo_03 import generate_pet_name_with_parser

title_visible = st.session_state.get('title_visible', True)

if title_visible:
    st.title("给你的宠物起个可爱名字")
animal_type = "小猫"

def click_on_btn():
    global is_show_title
    print(animal_type)
    resp = generate_pet_name_with_parser(animal_type)
    print(resp)
    st.session_state.title_visible = False
    st.markdown(f"# 给你的{animal_type}起个可爱名字\n{resp}")
    # st.markdown(resp)

with st.sidebar:
    st.image("<image_path>")
    animal_type = st.selectbox("选择宠物的类型?",("小猫","小狗"))

    gen_btn = st.button("起名吧",on_click=click_on_btn)

