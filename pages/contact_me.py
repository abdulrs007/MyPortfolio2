import streamlit as st
from send_email import send_email

# Page configuration
st.set_page_config(
    page_title="Contact - Abdulrasheed Shittu",
    page_icon="📧",
    layout="wide"
)

# Custom CSS for professional contact form styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    .main {
        padding: 0 2rem;
    }

    /* Header Section */
    .contact-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 3rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }

    .contact-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="1" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
    }

    .contact-title {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }

    .contact-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: 0;
        position: relative;
        z-index: 1;
    }

    /* Form Container */
    .form-container {
        max-width: 800px;
        margin: 0 auto;
        background: white;
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.1);
        border: 1px solid #e1e5e9;
        position: relative;
    }

    .form-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 6px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 20px 20px 0 0;
    }

    /* Form Fields Styling */
    .stTextInput > div > div > input {
        border: 2px solid #e1e5e9;
        border-radius: 10px;
        padding: 1rem;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: #fafbfc;
    }

    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        background: white;
    }

    .stTextArea > div > div > textarea {
        border: 2px solid #e1e5e9;
        border-radius: 10px;
        padding: 1rem;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: #fafbfc;
        min-height: 150px;
    }

    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        background: white;
    }

    /* Labels */
    .stTextInput > label, .stTextArea > label {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }

    /* Submit Button */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 1rem 2rem;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }

    /* Success/Info Messages */
    .stAlert {
        border-radius: 10px;
        border-left: 4px solid #667eea;
        font-family: 'Inter', sans-serif;
    }

    /* Contact Info Cards */
    .contact-info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }

    .contact-info-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        border: 1px solid #e1e5e9;
        transition: all 0.3s ease;
    }

    .contact-info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    }

    .contact-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .contact-info-title {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }

    .contact-info-text {
        font-family: 'Inter', sans-serif;
        color: #5a6c7d;
        font-size: 1rem;
    }

    /* Form Instructions */
    .form-instructions {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: center;
    }

    .instructions-title {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }

    .instructions-text {
        font-family: 'Inter', sans-serif;
        color: #5a6c7d;
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}

    /* Responsive Design */
    @media (max-width: 768px) {
        .contact-title {
            font-size: 2.2rem;
        }
        .form-container {
            padding: 2rem 1.5rem;
        }
        .contact-info-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="contact-header">
    <div class="contact-title">📧 Get In Touch</div>
    <div class="contact-subtitle">
        Let's discuss your next project or collaboration opportunity
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Information Cards
st.markdown("""
<div class="contact-info-grid">
    <div class="contact-info-card">
        <div class="contact-icon">⚡</div>
        <div class="contact-info-title">Quick Response</div>
        <div class="contact-info-text">I typically respond within 24 hours</div>
    </div>
    <div class="contact-info-card">
        <div class="contact-icon">🌍</div>
        <div class="contact-info-title">Remote Ready</div>
        <div class="contact-info-text">Available for remote collaboration worldwide</div>
    </div>
    <div class="contact-info-card">
        <div class="contact-icon">💼</div>
        <div class="contact-info-title">Professional</div>
        <div class="contact-info-text">Serious inquiries and project discussions</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Form Instructions
st.markdown("""
<div class="form-instructions">
    <div class="instructions-title">📝 How to Reach Me</div>
    <div class="instructions-text">
        Fill out the form below with your details and message. Whether you're looking to collaborate on a project, 
        discuss a job opportunity, or just want to connect, I'd love to hear from you!
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Form in a styled container
st.markdown('<div class="form-container">', unsafe_allow_html=True)

with st.form(key="email_form", clear_on_submit=True):
    st.markdown("### 📬 Send Me a Message")

    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])

    with col1:
        user_email = st.text_input(
            "✉️ Your Email Address",
            placeholder="your.email@example.com",
            help="I'll use this to get back to you"
        )

    with col2:
        subject_type = st.selectbox(
            "📋 Message Type",
            ["💼 Job Opportunity", "🤝 Collaboration", "❓ General Inquiry", "🛠️ Technical Discussion", "👋 Just Saying Hi"]
        )

    raw_message = st.text_area(
        "💬 Your Message",
        placeholder="Tell me about your project, opportunity, or what's on your mind...",
        help="Be as detailed as you'd like - I love hearing about interesting projects!",
        height=150
    )

    # Form validation and submission
    if st.form_submit_button("🚀 Send Message"):
        if user_email and raw_message:
            # Clean the subject type to remove emojis for email compatibility
            clean_subject = subject_type.split(' ', 1)[1] if ' ' in subject_type else subject_type

            # Create formatted message without emojis for email compatibility
            message = f"""\
Subject: New Portfolio Contact - {clean_subject}

From: {user_email}
Type: {clean_subject}

Message:
{raw_message}

---
Sent via Portfolio Contact Form
"""

            try:
                # Ensure the message is properly encoded
                clean_message = message.encode('ascii', 'ignore').decode('ascii')
                send_email(clean_message)
                st.success("🎉 Your message was sent successfully! I'll get back to you soon.")
                st.balloons()
            except Exception as e:
                st.error(
                    f"❌ Sorry, there was an issue sending your message. Please try again or reach out directly via email.")
                st.write("Debug info:", str(e))
        else:
            st.warning("⚠️ Please fill in both your email and message before sending.")

st.markdown('</div>', unsafe_allow_html=True)

# Additional Contact Methods
st.markdown("""
<div style="margin-top: 3rem; text-align: center; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px;">
    <h3 style="font-family: 'Inter', sans-serif; color: #2c3e50; margin-bottom: 1rem;">🔗 Other Ways to Connect</h3>
    <p style="font-family: 'Inter', sans-serif; color: #5a6c7d; font-size: 1.1rem;">
        Prefer a different communication method? Feel free to reach out through your preferred platform!
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #5a6c7d; font-family: 'Inter', sans-serif; margin-top: 3rem;">
    <p>💡 <strong>Pro Tip:</strong> The more details you share about your project or opportunity, the better I can help you!</p>
    <hr style="border: none; height: 1px; background: linear-gradient(90deg, transparent, #667eea, transparent); margin: 2rem 0;">
    <p>© 2024 Abdulrasheed Shittu | Looking forward to hearing from you! 🚀</p>
</div>
""", unsafe_allow_html=True)