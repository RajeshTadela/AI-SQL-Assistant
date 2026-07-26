import streamlit as st

from components.sidebar import render_sidebar
from components.upload_section import render_upload_section
from components.mysql_section import render_mysql_section
from components.chat import render_chat

st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Session State
# -------------------------

if "started" not in st.session_state:
    st.session_state.started = False

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>

.stApp{

background:linear-gradient(135deg,#020617,#0f172a,#111827);

}

/* ===========================
HERO
=========================== */

.hero{

padding:15px 25px;

border-radius:25px;

background:linear-gradient(135deg,#2563eb,#7c3aed,#06b6d4);

background-size:300% 300%;

animation:gradient 8s ease infinite;

text-align:center;

color:white;

box-shadow:0px 15px 40px rgba(0,0,0,.45);

}

.hero h1{

font-size:36px;

margin-bottom:8px;

}

.hero p{

font-size:16px;

margin:5px 0;

}

/* ===========================
FEATURE CARDS
=========================== */

.feature{

background:rgba(255,255,255,.05);

backdrop-filter:blur(18px);

border-radius:20px;

border:1px solid rgba(255,255,255,.08);

height:170px;

display:flex;

flex-direction:column;

justify-content:center;

align-items:center;

transition:.35s;

overflow:hidden;

padding:20px;

}

.feature:hover{

transform:translateY(-8px);

box-shadow:0 0 25px rgba(37,99,235,.35);

border:1px solid #2563eb;

}

.feature h2{

font-size:38px;

margin:0;

padding:0;

line-height:1;

}

.feature h3{

font-size:20px;

margin-top:18px;

margin-bottom:0;

color:white;

font-weight:700;

}
/* ===========================
BUTTON
=========================== */

.stButton > button{

width:100%;

height:72px;

background:#0f172a;

color:white;

border:2px solid #2563eb;

border-radius:18px;

font-size:24px;

font-weight:700;

letter-spacing:1px;

transition:.35s;

}

.stButton > button:hover{

background:#2563eb;

transform:translateY(-4px);

box-shadow:0 0 25px rgba(37,99,235,.6);

}

.stButton > button:active{

background:#7c3aed;

transform:scale(.95);

box-shadow:0 0 30px rgba(124,58,237,.7);

}

/* ===========================
RADIO BUTTONS
=========================== */

div[role="radiogroup"]{

padding:12px;

border-radius:15px;

background:rgba(255,255,255,.04);

}

/* ===========================
CHAT
=========================== */

[data-testid="stChatMessage"]{

border-radius:18px;

padding:15px;

background:rgba(255,255,255,.04);

}

/* ===========================
SCROLLBAR
=========================== */

::-webkit-scrollbar{

width:10px;

}

::-webkit-scrollbar-thumb{

background:#2563eb;

border-radius:20px;

}

/* ===========================
HIDE STREAMLIT
=========================== */

#MainMenu{

visibility:hidden;

}

footer{

visibility:hidden;

}

header{

visibility:hidden;

}

/* ===========================
ANIMATION
=========================== */

@keyframes gradient{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LANDING PAGE
# ==========================================================

if not st.session_state.started:

    st.markdown("""

<div class="hero">

<h1>🤖 AI SQL Assistant</h1>

<p>

Transform Natural Language into SQL<br><br>

Upload CSV • Connect MySQL • Query with AI

</p>

</div>

""", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        if st.button(
            "GET STARTED",
            use_container_width=True,
            key="start_btn"
        ):
            st.session_state.started = True
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4, gap="large")

    # ----------------------------
    # Upload CSV
    # ----------------------------

    with col1:

        st.markdown("""

    <div class="feature">

    <h2>📂</h2>

    <h3>Upload CSV</h3>

    </div>

    """, unsafe_allow_html=True)

    # ----------------------------
    # Connect MySQL
    # ----------------------------

    with col2:

        st.markdown("""

    <div class="feature">

    <h2>🛢</h2>

    <h3>Connect MySQL</h3>

    </div>

    """, unsafe_allow_html=True)

    # ----------------------------
    # AI SQL
    # ----------------------------

    with col3:

        st.markdown("""

    <div class="feature">

    <h2>🤖</h2>

    <h3>AI SQL</h3>

    </div>

    """, unsafe_allow_html=True)

    # ----------------------------
    # Results
    # ----------------------------

    with col4:

        st.markdown("""

    <div class="feature">

    <h2>📑</h2>

    <h3>Results</h3>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# MAIN APPLICATION
# ==========================================================

else:

    render_sidebar()

    st.markdown("""

<div class="hero">

<h1>🤖 AI SQL Assistant</h1>

<p>

Ask questions about your database using Natural Language

</p>

</div>

""",unsafe_allow_html=True)

    st.write("")

    choice=st.radio(

        "📂 Choose Data Source",

        [

            "Upload CSV Files",

            "Connect MySQL Database"

        ],

        horizontal=True

    )

    if choice=="Upload CSV Files":

        render_upload_section()

    else:

        render_mysql_section()

    st.divider()

    render_chat()

    st.markdown("""

<hr>

<center>

<small>

Powered by Streamlit • Gemini AI • MySQL

</small>

</center>

""",unsafe_allow_html=True)