import os
import sys
import base64
import streamlit as st
from PIL import Image

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

from app.services.langchain_agent_service import agent

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def main():
    image_path = "web/ai-research-assistant.png"
    
    if not os.path.exists(image_path):
        st.error("Image not found! Please check the path.")
        return
    
    encoded_image = encode_image(image_path)
    ai_icon = Image.open(image_path)
    
    st.set_page_config(
        page_title="AI Research Assistant",
        page_icon="ai_icon",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'About': "AI Research Assistant build by Kishore Gottumukkala"
        }
    )
    
    # Custom CSS for Styling
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
        color: #ffffff;  /* White text */
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    #MainMenu, footer {visibility: hidden;}

    .container, .custom-alert, .stSpinner, .stDownloadButton {
        max-width: 850px;
        margin: 20px auto;
        text-align: center;
    }

    .custom-text {
        max-width: 850px;
        margin: 20px auto;
        text-align: left;
    }

    /* Header Section */
    .header img {
        width: 280px;
        height: auto;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-radius: 14px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    .header img:hover {
        transform: scale(1.1);
        box-shadow: 0 14px 40px rgba(0, 0, 0, 0.4);
    }

    .header h1 {
        font-size: 3.8rem;
        margin: 20px 0;
        font-weight: 700;
        color:  #55B2FF;  /* Lighter Blue */
    }

    .header h4 {
        font-size: 1.5rem;
        color: #55B2FF;  /* Lighter Blue */
        margin-bottom: 30px;
    }

    /* Content Box */
    .content {
        margin-top: 10px;
        padding: 10px;
        background: #55B2FF;  /* Lighter Blue */
        border-radius: 8px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25);
    }

    .content h4 {
        margin-bottom: 25px;
        color: #00325B;  /* Dark Blue Text for Contrast */
        font-size: 2rem;
    }

    .content p {
        margin-bottom: 25px;
        color: #ffffff;  /* White text */
        font-size: 1.1rem;
        font-style: italic;
    }

    /* Input and Button Styling */
    .stTextInput, .stButton, .stDownload_Button {
        width: 65% !important;
        margin: 20px auto;
    }

    .stTextInput {
        color: #00325B;  /* Dark Blue Text */
        font-size: 1.1rem;
        font-weight: 500;
        font-style: italic;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #FF8C02;  /* Bright Orange Border */
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
    }

    .stButton>button {
        width: 50%;
        background: linear-gradient(135deg, #FF8C02, #FFB347); /* Orange Gradient */
        color: white;
        font-size: 3.1rem;
        font-weight: 800;
        padding: 14px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #E67700, #FF8C02); /* Darker Hover */
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.2);
        transform: translateY(-4px);
    }

    .stDownloadButton>button {
        width: 50%;
        background: linear-gradient(135deg, #FF8C02, #FFB347); /* Orange Gradient */
        color: white;
        font-size: 3.1rem;
        font-weight: 800;
        padding: 14px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }

    .stDownloadButton>button:hover {
        background: linear-gradient(135deg, #E67700, #FF8C02); /* Darker Hover */
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.2);
        transform: translateY(-4px);
    }

    /* Custom Alert Box */
    .custom-alert {
        width: 80% !important;
        background: linear-gradient(145deg, #FFD580, #FFB347); 
        color: #00325B;
        border-radius: 10px;
        padding: 14px;
        font-size: 1.3rem;
        margin-top: 5px;
        box-shadow: 0 8px 28px rgba(0, 0, 0, 0.2);
    }

    /* Custom Text Display */
    .custom-text {
        margin-top: 30px;
        color: #FFD580;  /* Warm Yellow */
        font-size: 1.3rem;
    }

    /* Spinner (Loading Animation) */
    .stSpinner {
        border: 6px solid #FF8C02;
        border-top: 6px solid #ffffff;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 1.2s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Render Header and Content
    st.markdown(f"""
        <div class="container">
            <div class="header">
               <img src="data:image/png;base64,{encoded_image}" alt="AI Research Assistant Tool" 
                style="
                    width: 160px; height: auto;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                " 
                onmouseover="this.style.boxShadow='0 10px 25px rgba(0, 0, 0, 0.5)'" 
                onmouseout="this.style.boxShadow='0 4px 10px rgba(0, 0, 0, 0.2)'">
                <h1>AI Research Assistant</h1>
                <h4>Explore the world of AI-driven research with ease and precision.</h4>
            </div>
            <div class="content">
                <h4>Start your Research Journey</h4>
                <p>Input your query below and let AI guide you to the best results.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Custom Input and Button
    user_input = st.text_input("Enter your research topic here", "")
    
    if st.button("Research Now", key="custom-button"):
        with st.spinner("Processing..."):
            result = agent(user_input)
            st.markdown('<div class="custom-alert">Research Completed! See the results below.</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">{result["output"]}</div>', unsafe_allow_html=True)
            st.download_button("Download Results", result['output'], file_name="research_summary.txt")

if __name__ == '__main__':
    main()