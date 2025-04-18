import streamlit as st
from streamlit_option_menu import option_menu

from modules.Pages import text_generation_page 


def main():
    menus = {
        "Text Generation":text_generation_page, 
        # new menu here
    }
    
    with st.sidebar:
        try:
            selected = option_menu(menu_title="APP MENU",
                options=list(menus.keys()),
                default_index=0
            )
        except Exception as e:
            st.write(f"ERROR: {e}")
            
    if selected in menus.keys():
        menus[selected]()
    
    
if __name__ == "__main__":
    main()