import streamlit as st
import random

st.set_page_config(page_title="AI Content Automation", page_icon="🤖")

st.title("🤖 AI Multi-Agent Content Automation System")

# -------- AGENTS -------- #

def content_generation_agent(topic):
    templates = [
        f"{topic} is transforming industries with innovation and efficiency.",
        f"In recent years, {topic} has gained significant attention worldwide.",
        f"{topic} plays a crucial role in shaping the future of technology.",
        f"Many organizations are adopting {topic} to improve productivity.",
        f"{topic} is expected to grow rapidly in the coming years."
    ]
    return " ".join(random.sample(templates, 3))


def compliance_agent(content):
    banned_words = ["fake", "illegal", "scam", "fraud", "hack", "violence"]

    content_lower = content.lower()

    for word in banned_words:
        if word in content_lower:
            return f"Rejected ❌ (Contains restricted word: {word})"

    return "Approved ✅"


def publishing_agent():
    return "Published Successfully 🚀"


# -------- INPUT -------- #

topic = st.text_input("Enter Content Topic")
language = st.selectbox("Select Language", ["English", "Hindi", "Kannada"])
platform = st.selectbox("Select Platform", ["Blog", "Instagram", "LinkedIn"])

# -------- PIPELINE -------- #

if st.button("Run AI Pipeline"):

    if topic == "":
        st.warning("Please enter a topic")

    else:
        # Agent 1
        content = content_generation_agent(topic)

        # Agent 2
        compliance_status = compliance_agent(content)

        # Agent 3
        publishing_status = publishing_agent()

        # -------- OUTPUT -------- #

        st.subheader("📄 Generated Content")
        st.write(content)

        st.subheader("🛡 Compliance Status")
        st.write(compliance_status)

        st.subheader("🌍 Language")
        st.write(language)

        st.subheader("📢 Platform")
        st.write(platform)

        st.subheader("⚙️ Multi-Agent Pipeline Execution")
        st.write("Agent 1: Content Generation ✅")
        st.write("Agent 2: Compliance Check ✅")
        st.write("Agent 3: Publishing ✅")

        st.subheader("📢 Publishing Status")
        st.write(publishing_status)