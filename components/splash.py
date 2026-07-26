import streamlit as st
import streamlit.components.v1 as components
import time


def show_splash():

    if "splash_done" not in st.session_state:

        components.html(
            """
<!DOCTYPE html>
<html>

<head>

<style>

html,body{

margin:0;
padding:0;

width:100%;
height:100%;

background:#020617;

display:flex;

justify-content:center;

align-items:center;

font-family:Arial,sans-serif;

overflow:hidden;

}

.container{

text-align:center;

color:white;

}

.robot{

font-size:90px;

animation:float 2s infinite ease-in-out;

}

.title{

font-size:50px;

font-weight:bold;

margin-top:20px;

}

.subtitle{

margin-top:10px;

font-size:20px;

color:#94a3b8;

}

.loader{

margin:auto;

margin-top:35px;

width:220px;

height:6px;

background:#1e293b;

border-radius:20px;

overflow:hidden;

}

.bar{

height:100%;

width:0%;

background:linear-gradient(90deg,#2563eb,#7c3aed,#06b6d4);

animation:load 2.3s linear forwards;

}

@keyframes load{

0%{width:0%;}

100%{width:100%;}

}

@keyframes float{

0%{transform:translateY(0px);}
50%{transform:translateY(-15px);}
100%{transform:translateY(0px);}

}

</style>

</head>

<body>

<div class="container">

<div class="robot">🤖</div>

<div class="title">

AI SQL Assistant

</div>

<div class="subtitle">

Loading Intelligence...

</div>

<div class="loader">

<div class="bar"></div>

</div>

</div>

</body>

</html>
""",
            height=700,
        )

        time.sleep(2.5)

        st.session_state.splash_done = True

        st.rerun()