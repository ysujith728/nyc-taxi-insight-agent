import streamlit as st
import requests
import time

st.set_page_config(
    page_title="NYC Taxi Insight Agent",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700&family=DM+Sans:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: #0a0a0a;
        color: #f5f5f5;
    }

    .stApp {
        background-color: #0a0a0a;
    }

    /* Hide default streamlit stuff */
    #MainMenu, footer, header { visibility: hidden; }

    /* Hero banner */
    .hero {
        background-color: #f7c948;
        padding: 28px 36px;
        border-radius: 0px;
        margin: -1rem -1rem 2rem -1rem;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .hero-title {
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 48px;
        font-weight: 700;
        color: #0a0a0a;
        letter-spacing: -1px;
        line-height: 1;
        margin: 0;
    }
    .hero-sub {
        font-size: 14px;
        color: #1a1a1a;
        margin: 4px 0 0 0;
        opacity: 0.7;
    }
    .hero-badge {
        background: #0a0a0a;
        color: #f7c948;
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 2px;
        padding: 6px 14px;
        border-radius: 4px;
        text-transform: uppercase;
        margin-top: 10px;
        display: inline-block;
    }

    /* Input box */
    .stTextInput > div > div > input {
        background-color: #141414 !important;
        color: #f5f5f5 !important;
        border: 1.5px solid #f7c948 !important;
        border-radius: 6px !important;
        font-size: 15px !important;
        padding: 12px 16px !important;
        font-family: 'DM Sans', sans-serif !important;
    }
    .stTextInput > div > div > input:focus {
        box-shadow: 0 0 0 2px rgba(247,201,72,0.3) !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #555 !important;
    }

    /* Primary button */
    .stButton > button {
        background-color: #f7c948 !important;
        color: #0a0a0a !important;
        font-family: 'Barlow Condensed', sans-serif !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        letter-spacing: 1px !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 10px 24px !important;
        width: 100% !important;
        text-transform: uppercase !important;
        transition: background 0.2s !important;
    }
    .stButton > button:hover {
        background-color: #e6b800 !important;
    }

    /* Chat bubbles */
    .bubble-user {
        background: #141414;
        border-left: 3px solid #f7c948;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        margin: 12px 0 4px 0;
        font-size: 14px;
        color: #f7c948;
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 17px;
        letter-spacing: 0.3px;
    }
    .bubble-agent {
        background: #111;
        border-left: 3px solid #00d4aa;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        margin: 4px 0 16px 0;
        font-size: 14px;
        color: #e0e0e0;
        line-height: 1.6;
    }
    .bubble-label-user {
        font-size: 11px;
        color: #f7c948;
        letter-spacing: 2px;
        font-family: 'Barlow Condensed', sans-serif;
        text-transform: uppercase;
        margin-bottom: 2px;
    }
    .bubble-label-agent {
        font-size: 11px;
        color: #00d4aa;
        letter-spacing: 2px;
        font-family: 'Barlow Condensed', sans-serif;
        text-transform: uppercase;
        margin-bottom: 2px;
    }

    /* Metric cards */
    .metric-box {
        background: #141414;
        border: 1px solid #222;
        border-top: 3px solid #f7c948;
        border-radius: 6px;
        padding: 16px;
        text-align: center;
    }
    .metric-val {
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 36px;
        font-weight: 700;
        color: #f7c948;
        line-height: 1;
    }
    .metric-lbl {
        font-size: 11px;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 4px;
    }

    /* Sample question buttons */
    .sample-btn > button {
        background: #141414 !important;
        color: #ccc !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 6px !important;
        font-size: 13px !important;
        font-family: 'DM Sans', sans-serif !important;
        text-align: left !important;
        font-weight: 400 !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        padding: 8px 12px !important;
    }
    .sample-btn > button:hover {
        border-color: #f7c948 !important;
        color: #f7c948 !important;
        background: #1a1a1a !important;
    }

    /* Section headers */
    .section-label {
        font-family: 'Barlow Condensed', sans-serif;
        font-size: 13px;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #555;
        margin-bottom: 12px;
        margin-top: 24px;
    }

    /* Divider */
    hr {
        border: none;
        border-top: 1px solid #1e1e1e;
        margin: 20px 0;
    }

    /* Scrollable chat area */
    .chat-area {
        max-height: 520px;
        overflow-y: auto;
        padding-right: 4px;
    }

    /* Latency tag */
    .latency-tag {
        font-size: 11px;
        color: #444;
        text-align: right;
        margin-top: -10px;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Banner
# -----------------------------

st.markdown("""
<div class="hero">
    <div style="font-size:48px;">🚕</div>
    <div>
        <p class="hero-title">NYC TAXI INSIGHT AGENT</p>
        <p class="hero-sub">Multi-tool AI reasoning over 10M+ real NYC taxi trips</p>
        <span class="hero-badge">● Live</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Session State
# -----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "total_latency" not in st.session_state:
    st.session_state.total_latency = 0.0

# -----------------------------
# Layout
# -----------------------------

left, right = st.columns([3, 1], gap="large")

# -----------------------------
# LEFT — Chat
# -----------------------------

with left:

    st.markdown('<p class="section-label">Chat Interface</p>', unsafe_allow_html=True)

    # Input row
    col_input, col_btn = st.columns([5, 1])

    with col_input:
        question = st.text_input(
            "question",
            placeholder="Ask anything about NYC taxi data...",
            label_visibility="collapsed",
            key="question_input"
        )

    with col_btn:
        ask = st.button("Ask →")

    def send_question(q):
        with st.spinner("Agent reasoning..."):
            try:
                start = time.time()
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"question": q},
                    timeout=120
                )
                latency = round(time.time() - start, 2)
                data = response.json()
                answer = data.get("answer", "No answer returned.")
                st.session_state.chat_history.append({
                    "question": q,
                    "answer": answer,
                    "latency": latency
                })
                st.session_state.total_questions += 1
                st.session_state.total_latency += latency
                st.rerun()
            except Exception as e:
                st.error(f"Connection error: {str(e)}")

    if ask and question:
        send_question(question)

    # Chat history
    if st.session_state.chat_history:
        st.markdown('<div class="chat-area">', unsafe_allow_html=True)
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f'<p class="bubble-label-user">You</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="bubble-user">{chat["question"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<p class="bubble-label-agent">Agent</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="bubble-agent">{chat["answer"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<p class="latency-tag">⏱ {chat["latency"]}s</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.session_state.total_questions = 0
            st.session_state.total_latency = 0.0
            st.rerun()
    else:
        st.markdown("""
        <div style="text-align:center; padding: 60px 20px; color: #333;">
            <div style="font-size: 48px; margin-bottom: 12px;">🚖</div>
            <p style="font-family: 'Barlow Condensed', sans-serif; font-size: 20px; letter-spacing: 1px; color: #444;">
                Ask your first question to get started
            </p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# RIGHT — Stats + Samples
# -----------------------------

with right:

    # Metrics
    st.markdown('<p class="section-label">Session Stats</p>', unsafe_allow_html=True)

    avg_lat = round(
        st.session_state.total_latency / st.session_state.total_questions, 1
    ) if st.session_state.total_questions > 0 else 0

    col_m1, col_m2 = st.columns(2)

    with col_m1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-val">{st.session_state.total_questions}</div>
            <div class="metric-lbl">Questions</div>
        </div>
        """, unsafe_allow_html=True)

    with col_m2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-val">{avg_lat}s</div>
            <div class="metric-lbl">Avg Speed</div>
        </div>
        """, unsafe_allow_html=True)

    # Sample Questions
    st.markdown('<p class="section-label">Try These</p>', unsafe_allow_html=True)

    samples = [
        "What is the average fare amount?",
        "Which payment type has the highest fare?",
        "Find LocationID for JFK Airport",
        "What does RateCodeID mean?",
        "How many total trips are there?",
        "Are there trips with negative fares?",
        "Top 5 pickup zones by total revenue?",
        "Compare JFK vs LaGuardia average fares",
        "What is the average tip percentage?",
    ]

    for q in samples:
        st.markdown('<div class="sample-btn">', unsafe_allow_html=True)
        if st.button(q, key=f"sample_{q}"):
            send_question(q)
        st.markdown('</div>', unsafe_allow_html=True)

    # Status
    st.markdown('<p class="section-label">System</p>', unsafe_allow_html=True)
    try:
        r = requests.get("http://127.0.0.1:8000/health", timeout=3)
        if r.status_code == 200:
            st.markdown("""
            <div style="background:#0d1f0d; border:1px solid #1a3d1a; border-radius:6px; 
                        padding:10px 14px; font-size:13px; color:#4caf50;">
                ● API Connected
            </div>
            """, unsafe_allow_html=True)
        else:
            raise Exception()
    except:
        st.markdown("""
        <div style="background:#1f0d0d; border:1px solid #3d1a1a; border-radius:6px; 
                    padding:10px 14px; font-size:13px; color:#f44336;">
            ● API Offline — run uvicorn first
        </div>
        """, unsafe_allow_html=True)