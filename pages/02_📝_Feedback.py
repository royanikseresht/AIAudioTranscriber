"""
Contact Page using formsubmit.co API
"""
import streamlit as st
from streamlit_lottie import st_lottie
from utils import *

st.set_page_config(
        page_title="AI Audio Transciber",
        page_icon="./assets/favicon.png",
        layout= "wide",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/royanikseresht/AIAudioTranscriber.git',
        'Report a bug': "https://github.com/royanikseresht/AIAudioTranscriber.git",
        'About': "## A minimalistic application to generate transcriptions for audio built using Python"
        } )



st.title(":mailbox: Get In Touch With Me!")
hide_footer()

# Load Stylesheet(s) for relevant components
css_local("assets/styles/contact.css")
# Load and display animation
anim = lottie_local("assets/animations/contact.json")
st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium", # low; medium ; high
            # renderer="svg", # canvas
            height=400,
            width=400,
            key=None,
            )
# HTML code for formsubmit contactform template
contact_form ="""
            <form name="form1" action="https://formcarry.com/s/2pFePjMnLAK" method="POST" accept-charset="UTF-8">
            <input id="name" type="text" name="name" placeholder="Your Name" required/>
            <input id="email" type="email" name="email" placeholder="Email Address" required/>                  
            <textarea id="textArea" name="message" placeholder="Type your Message" required></textarea>
            
            <button type="submit" style="background-color: #739c92; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
                  Send
            </button>
            </form>
            """

st.markdown(contact_form,unsafe_allow_html=True)

