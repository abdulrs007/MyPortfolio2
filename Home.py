import pandas as pd
import streamlit as st


# Page configuration with custom theme
st.set_page_config(
    page_title="Abdulrasheed Shittu - Software Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"  # Changed to show sidebar for navigation
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');

    /* Multiple Sidebar Selectors for Different Streamlit Versions */
    .css-1d391kg, 
    .css-6qob1r,
    .css-1cypcdb,
    section[data-testid="stSidebar"],
    .stSidebar,
    div[data-testid="stSidebar"] > div,
    .sidebar {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab, #667eea, #764ba2) !important;
        background-size: 400% 400% !important;
        animation: gradientShift 15s ease infinite !important;
        position: relative !important;
        overflow: hidden !important;
    }

    /* Pattern Overlay */
    .css-1d391kg::before,
    .css-6qob1r::before,
    .css-1cypcdb::before,
    section[data-testid="stSidebar"]::before,
    .stSidebar::before,
    div[data-testid="stSidebar"] > div::before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="5" cy="15" r="0.5" fill="rgba(255,255,255,0.05)"/><circle cx="15" cy="5" r="0.7" fill="rgba(255,255,255,0.08)"/></pattern></defs><rect width="100" height="100" fill="url(%23dots)"/></svg>') !important;
        opacity: 0.4 !important;
        z-index: 0 !important;
        pointer-events: none !important;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Sidebar Text and Elements */
    .css-1d391kg .css-1v3fvcr,
    .css-6qob1r .css-1v3fvcr,
    .css-1cypcdb .css-1v3fvcr,
    section[data-testid="stSidebar"] *,
    .stSidebar *,
    div[data-testid="stSidebar"] * {
        color: #ffffff !important;
        position: relative !important;
        z-index: 1 !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
    }

    /* Style the collapse/expand control wherever it appears */
    [data-testid="stSidebar"] button[data-testid="collapsedControl"],
    [data-testid="stHeader"] button[data-testid="collapsedControl"] {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d3748 25%, #e53e3e 50%, #3182ce 75%, #38a169 100%) !important;
        color: white !important;
        border: 3px solid #000000 !important;
        border-radius: 50% !important;
        box-shadow: 
            0 0 0 4px #ffffff,
            0 0 0 7px #000000,
            0 8px 25px rgba(0, 0, 0, 0.8),
            inset 0 2px 10px rgba(255, 255, 255, 0.3) !important;
        width: 60px !important;
        height: 60px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 10000 !important;
        transition: all 0.4s ease !important;
        cursor: pointer !important;
        font-size: 20px !important;
        font-weight: bold !important;
        animation: megaPulse 3s ease-in-out infinite !important;
    }

    button[data-testid="collapsedControl"]:hover,
    .css-1rs6os:hover,
    .css-vk3wp9:hover,
    button[kind="header"]:hover,
    button[data-baseweb="button"]:hover {
        background: linear-gradient(135deg, #ff4444 0%, #ff8844 25%, #44ff44 50%, #4488ff 75%, #ff44ff 100%) !important;
        transform: scale(1.2) rotate(360deg) !important;
        box-shadow: 
            0 0 0 6px #ffffff,
            0 0 0 10px #000000,
            0 12px 35px rgba(0, 0, 0, 0.9),
            0 0 30px rgba(255, 68, 68, 0.8) !important;
        border-width: 4px !important;
    }

    /* When sidebar is collapsed - SUPER VISIBLE BUTTON */
    .css-1544g2n button[data-testid="collapsedControl"],
    .css-1oe5cao button[data-testid="collapsedControl"],
    div[data-testid="stSidebar"][aria-expanded="false"] button[data-testid="collapsedControl"] {
        visibility: visible !important;
        opacity: 1 !important;
        display: flex !important;
        background: linear-gradient(45deg, #000000 0%, #ff0000 25%, #00ff00 50%, #0000ff 75%, #ff00ff 100%) !important;
        animation: megaPulse 2s ease-in-out infinite alternate, rotate 4s linear infinite !important;
    }

    @keyframes megaPulse {
        0% { 
            box-shadow: 
                0 0 0 4px #ffffff,
                0 0 0 7px #000000,
                0 8px 25px rgba(0, 0, 0, 0.8),
                0 0 20px rgba(255, 0, 0, 0.6);
            transform: scale(1);
        }
        50% {
            box-shadow: 
                0 0 0 6px #ffffff,
                0 0 0 12px #000000,
                0 12px 40px rgba(0, 0, 0, 0.9),
                0 0 40px rgba(0, 255, 0, 0.8);
            transform: scale(1.1);
        }
        100% { 
            box-shadow: 
                0 0 0 4px #ffffff,
                0 0 0 7px #000000,
                0 8px 25px rgba(0, 0, 0, 0.8),
                0 0 20px rgba(0, 0, 255, 0.6);
            transform: scale(1);
        }
    }

    @keyframes rotate {
        from { background-position: 0% 50%; }
        to { background-position: 100% 50%; }
    }

    /* Enhanced Sidebar content styling with glass morphism */
    .sidebar-content {
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(20px) saturate(180%) !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        z-index: 1 !important;
    }

    .sidebar-content:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15) !important;
    }

    /* Global Styles */
    .main {
        padding: 0 2rem;
    }

    /* Custom Header */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="50" cy="10" r="0.5" fill="rgba(255,255,255,0.05)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
    }

    .hero-content {
        position: relative;
        z-index: 1;
    }

    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .hero-subtitle {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.2rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: 1.5rem;
        font-weight: 400;
    }

    .hero-description {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: rgba(255,255,255,0.85);
        max-width: 800px;
    }

    /* Skills Tags */
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1.5rem;
    }

    .skill-tag {
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
    }

    .skill-tag:hover {
        background: rgba(255,255,255,0.3);
        transform: translateY(-2px);
    }

    /* Project Cards */
    .project-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e1e5e9;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }

    .project-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.8rem;
    }

    .project-description {
        font-family: 'Inter', sans-serif;
        color: #5a6c7d;
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .project-link {
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        text-decoration: none;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        transition: all 0.3s ease;
        margin-top: 1rem;
    }

    .project-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        text-decoration: none;
        color: white;
    }

    /* Section Headers */
    .section-header {
        font-family: 'Inter', sans-serif;
        font-size: 2.2rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 3rem 0 2rem 0;
        text-align: center;
        position: relative;
    }

    .section-header::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }

    /* Contact Section */
    .contact-section {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 3rem;
        text-align: center;
    }

    .contact-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
    }

    .contact-description {
        font-family: 'Inter', sans-serif;
        color: #5a6c7d;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }

    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .hero-subtitle {
            font-size: 1rem;
        }
        .main {
            padding: 0 1rem;
        }
    }

    /* Keep header visible; hide only menu/deploy */
    [data-testid="stHeader"] { visibility: visible !important; }
    #MainMenu, .stDeployButton, footer { display: none !important; }
    
    /* Hide all deploy-related buttons that might interfere */
    button[data-testid="stDeployButton"],
    .css-1rs6os.edgvbvh3,
    .css-vk3wp9.edgvbvh3,
    button[kind="primary"].css-1rs6os,
    button[kind="primary"].css-vk3wp9 {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }

    /* Custom image styling */
    .profile-image {
        border-radius: 50%;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        border: 4px solid white;
    }
</style>

<script>
    // Fix for sidebar toggle functionality
    document.addEventListener('DOMContentLoaded', function() {
        // Ensure the sidebar toggle button works properly
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes.length) {
                    // Find and style collapse/expand buttons
                    const buttons = document.querySelectorAll('button[data-testid="collapsedControl"]');
                    buttons.forEach(button => {
                        button.style.cssText += `
                            background: rgba(255, 255, 255, 0.2) !important;
                            border-radius: 8px !important;
                            border: 1px solid rgba(255, 255, 255, 0.3) !important;
                            backdrop-filter: blur(10px) !important;
                            transition: all 0.3s ease !important;
                        `;
                        
                        button.addEventListener('mouseenter', function() {
                            this.style.cssText += `
                                background: rgba(255, 255, 255, 0.3) !important;
                                transform: scale(1.05) !important;
                            `;
                        });
                        
                        button.addEventListener('mouseleave', function() {
                            this.style.cssText += `
                                background: rgba(255, 255, 255, 0.2) !important;
                                transform: scale(1) !important;
                            `;
                        });
                    });
                }
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
</script>
""", unsafe_allow_html=True)

# Navigation in sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0; border-bottom: 2px solid rgba(255,255,255,0.4); margin-bottom: 2rem; position: relative;">
        <h2 style="color: #ffffff; font-family: 'Inter', sans-serif; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.5), 0 2px 4px rgba(0,0,0,0.3); font-size: 1.4rem; font-weight: 600; animation: glow 2s ease-in-out infinite alternate;">🧭 Navigation</h2>
    </div>
    <style>
        @keyframes glow {
            from { text-shadow: 0 0 10px rgba(255,255,255,0.3), 0 2px 4px rgba(0,0,0,0.3); }
            to { text-shadow: 0 0 20px rgba(255,255,255,0.6), 0 0 30px rgba(255,255,255,0.4), 0 2px 4px rgba(0,0,0,0.3); }
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-content">
        <div style="color: #ecf0f1; font-family: 'Inter', sans-serif; line-height: 1.6;">
            <p style="margin: 0.8rem 0;"><strong>📍 Current Page:</strong> <span style="color: #f39c12;">Home Portfolio</span></p>
            <p style="margin: 0.8rem 0;"><strong>💬 Need to reach me?</strong><br>Use the <span style="color: #3498db;">Contact Me</span> page!</p>
            <p style="margin: 0.8rem 0;"><strong>🔍 Navigation:</strong><br>Use the sidebar menu above to switch between pages</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">Abdulrasheed Shittu</div>
        <div class="hero-subtitle">< Software Developer /></div>
        <div class="hero-description">
            Hi, I'm Abdulrasheed, a passionate Software Developer with a B.Eng in Electrical and Computer
            Engineering. I specialize in backend development using Python and Django, and I've successfully led and
            contributed to impactful projects across e-libraries, VAT audit systems, AI agents, and eCommerce platforms.
            With hands-on experience in cloud platforms, APIs, data pipelines, and full-stack development, I bring 
            a blend of technical expertise and problem-solving skills. My work emphasizes performance, security, 
            and real-world usability—whether it's building AI-powered platforms or creating scalable systems for organizations.
        </div>
        <div class="skills-container">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Django</span>
            <span class="skill-tag">css</span>
            <span class="skill-tag">Bootstrap</span>
            <span class="skill-tag">Javascript</span>
            <span class="skill-tag">Backend Development</span>
            <span class="skill-tag">Cloud Platforms</span>
            <span class="skill-tag">APIs</span>
            <span class="skill-tag">AI/ML</span>
            <span class="skill-tag">Full-Stack</span>
            <span class="skill-tag">Data Pipelines</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Projects Section Header
st.markdown('<div class="section-header">Featured Projects</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; font-family: 'Inter', sans-serif; color: #5a6c7d; font-size: 1.1rem; margin-bottom: 3rem;">
    Below you will find some of the applications I have built. Each project represents my commitment to creating impactful, scalable solutions.
</div>
""", unsafe_allow_html=True)

# Load and display projects
try:
    df = pd.read_csv("datax.csv", sep=",", encoding="windows-1252")
    df.columns = df.columns.str.strip()

    # Create two columns for projects
    col1, col2 = st.columns(2, gap="large")

    # Split projects between columns
    mid_point = len(df) // 2

    with col1:
        for index, row in df[:mid_point].iterrows():
            st.markdown(f"""
            <div class="project-card fade-in-up">
                <div class="project-title">{row["Title"]}</div>
                <div class="project-description">{row["Description"]}</div>
            """, unsafe_allow_html=True)

            # Display image if exists
            try:
                st.image("images/" + row["image"], use_container_width=True)
            except:
                st.info("📷 Project image not found")

            st.markdown(f"""
                <a href="{row['URL']}" target="_blank" class="project-link">
                    🔗 View Project
                </a>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        for index, row in df[mid_point:].iterrows():
            st.markdown(f"""
            <div class="project-card fade-in-up">
                <div class="project-title">{row["Title"]}</div>
                <div class="project-description">{row["Description"]}</div>
            """, unsafe_allow_html=True)

            # Display image if exists
            try:
                st.image("images/" + row["image"], use_container_width=True)
            except:
                st.info("📷 Project image not found")

            st.markdown(f"""
                <a href="{row['URL']}" target="_blank" class="project-link">
                    🔗 View Project
                </a>
            </div>
            """, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("📁 datax.csv file not found. Please ensure the file exists in your project directory.")
except Exception as e:
    st.error(f"❌ Error loading projects: {str(e)}")

# Typing animation for the footer
st.markdown('<div class="section-header">Let\'s Connect</div>', unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="contact-section">
    <div class="contact-title">Ready to Build Something Amazing Together?</div>
    <div class="contact-description">
        I'm always open to discussing new opportunities, innovative projects, and ways to create impactful solutions.
        Let's connect and explore how we can work together!
    </div>
</div>
""", unsafe_allow_html=True)

# Add some interactive elements
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📧 Contact Me", key="contact"):
        st.balloons()
        st.success("Visit the 'Contact Me' page in the sidebar to send me a message!")

with col2:
    if st.button("📄 Request Resume", key="resume"):
        st.info("Drop me an message using the contact page to get my resume")

with col3:
    if st.button("🤝 Let's Connect", key="connect"):
        st.success("Use the Contact Me page to reach out - I'd love to hear from you!")

# Footer with social links placeholder
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #5a6c7d; font-family: 'Inter', sans-serif;">
    <p>© 2025 Abdulrasheed Shittu | Software Developer | Building the Future, One Line of Code at a Time</p>
</div>
""", unsafe_allow_html=True)