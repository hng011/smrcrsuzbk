from .__init__ import *
from .Utils import generate_text
from streamlit.components.v1 import html

def text_generation_page():
    st.title("Story Generation Page")
    user_prompt = st.text_area("✍️ Enter your story prompt:", height=100)
    min_par, max_par = 1, 5
    paragraph = st.number_input("📃 Number of paragraph: ", min_value=min_par, max_value=max_par, format='%d')
    system_prompt = f"You are a creative and imaginative story writer. Write vivid, engaging, and coherent stories based on the user prompt. Include a creative title. Write the story in exactly {paragraph} paragraphs. Do not include any explanation or commentary. ONLY USE ENGLISH LANGUAGE"
    
    if paragraph > 0 and paragraph <= max_par:        
        start_t, end_t = None, None
        is_end = False
        
        if st.button("🪄 Generate Story"):
            if not user_prompt.strip():
                st.warning("Please enter a prompt.")
            else:
                with st.spinner("Generating Story... ⭐"):
                    start_t = time.time()
                    generate_text(
                        user_prompt=f"Write a story about: {user_prompt}",
                        system_prompt=system_prompt
                    )
                    
                    res, model, l = generate_text(
                        user_prompt=f"Write a story about: {user_prompt}",
                        system_prompt=system_prompt
                    )
                    
                    token = res.split(" ")
                    
                res_placeholder = st.empty()
                story = ""
                    
                for x in token:
                    story += x + " "
                    res_placeholder.markdown(story)
                    time.sleep(0.02)
                
                end_t = time.time() - start_t
                is_end = True
        
        if is_end: 
            html(f"<script>console.log(\"{l}\");</script>", height=0)
            st.write(f"⏳ Response Time: {end_t:.2f} seconds")
            st.write(f"🤖 Model: {model}")