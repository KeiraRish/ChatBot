import streamlit as st

st.set_page_config(page_title="Interview Companion", page_icon="💼", layout="wide")

st.markdown(
    """
    <style>
    :root {
        --bg: #ffffff;
        --panel: #fff7fa;
        --accent: #f06292;
        --accent-dark: #d94672;
        --text: #1f1f1f;
        --muted: #6b7280;
    }
    .stApp {
        background: linear-gradient(135deg, #ffffff 0%, #fff7fa 100%);
    }
    [data-testid="stHeader"] {
        background: rgba(255,255,255,0);
    }
    .hero-card {
        background: linear-gradient(135deg, #ffffff 0%, #fff7fa 100%);
        border: 1px solid #ffdce9;
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(240, 98, 146, 0.08);
    }
    .pill {
        display: inline-block;
        background: #ffe4ee;
        color: var(--accent-dark);
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 0.9rem;
        margin: 4px 6px 4px 0;
        font-weight: 600;
    }
    .chat-bubble {
        background: #fff;
        border: 1px solid #ffdce9;
        border-radius: 14px;
        padding: 12px 14px;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <h1 style="margin-bottom: 0.2em; color:#1f1f1f;">Keira Rish</h1>
        <p style="font-size: 1.1rem; color:#f06292; font-weight: 700; margin-top: 0;">Product-minded software engineer • thoughtful builder • calm under pressure</p>
        <p style="color:#4b5563; line-height: 1.6;">This experience is designed for interviewers who want a polished, conversational way to learn about my background, strengths, and working style.</p>
        <div>
            <span class="pill">Leadership</span>
            <span class="pill">Product thinking</span>
            <span class="pill">AI & automation</span>
            <span class="pill">Collaboration</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

left, right = st.columns([1.45, 1])

with left:
    st.subheader("Why I’m a strong fit")
    st.markdown(
        """
        - I bring a calm, thoughtful approach to ambiguous problems.
        - I enjoy turning complex ideas into clear, practical execution.
        - I care deeply about building experiences that feel polished, useful, and human.
        - I thrive in collaborative settings where curiosity and ownership matter.
        """
    )

    st.subheader("What I value")
    st.markdown(
        """
        - Clear communication and genuine curiosity.
        - Strong execution paired with empathy.
        - Continuous learning and thoughtful growth.
        - Building with intention, not just speed.
        """
    )

with right:
    st.subheader("Quick conversation starters")
    starter_questions = [
        "Tell me about yourself",
        "What is your biggest strength?",
        "How do you work with a team?",
        "What motivates you in your work?",
        "Describe a challenge you handled well",
    ]

    for question in starter_questions:
        if st.button(question, use_container_width=True):
            st.session_state.pending_question = question

    st.subheader("Interview style")
    st.info("I like conversations that explore impact, ownership, growth, and how someone thinks—not just what they’ve done.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I’m Keira. Ask me anything you’d want to know about my background, values, or working style.",
        }
    ]

if "pending_question" in st.session_state and st.session_state.pending_question:
    prompt = st.session_state.pending_question
    st.session_state.pending_question = None
else:
    prompt = st.chat_input("Ask a question to learn more about me")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    question = prompt.lower()

    if any(word in question for word in ["tell me about yourself", "about yourself", "who are you"]):
        answer = "I’m a product-minded software engineer who enjoys creating thoughtful digital experiences, solving ambiguous problems, and helping teams move with clarity. I care about building work that is useful, polished, and meaningful."
    elif any(word in question for word in ["strength", "strongest", "best"]):
        answer = "One of my biggest strengths is turning ambiguity into momentum. I’m good at asking the right questions, connecting ideas quickly, and helping teams make progress even when the path isn’t fully clear."
    elif any(word in question for word in ["team", "collaborate", "work with"]):
        answer = "I work best in collaborative environments where people are curious and honest. I like sharing context, listening closely, and making sure everyone feels aligned on the goal and the next step."
    elif any(word in question for word in ["motivat", "drive", "passion"]):
        answer = "I’m motivated by work that has real impact and by the chance to learn while building something meaningful. I’m especially energized by projects that improve people’s experience or simplify complexity."
    elif any(word in question for word in ["challenge", "hard", "difficult", "failure"]):
        answer = "I’ve learned that the best way through a challenge is to stay calm, clarify what matters most, and focus on steady progress rather than perfection. I try to be clear, accountable, and adaptable when things shift."
    else:
        answer = "That’s a great question. I’d answer it by focusing on how I think, how I work with others, and the kind of impact I’m trying to create through my work."

    st.session_state.messages.append({"role": "assistant", "content": answer})

for message in st.session_state.messages:
    with st.container():
        if message["role"] == "assistant":
            st.markdown(f"<div class='chat-bubble'><strong>Me:</strong> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble' style='background:#fff7fa;'><strong>Interviewer:</strong> {message['content']}</div>", unsafe_allow_html=True)
