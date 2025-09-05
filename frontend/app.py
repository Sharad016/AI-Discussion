import streamlit as st

st.set_page_config(page_title="AI Discussion Tool", page_icon="💬", layout="centered")

st.title("💬 AI Discussion Tool")

# Textbox for user input
discussion_text = st.text_area("Paste a discussion thread here:", height=200)

# Analyze button
if st.button("Analyze"):
    if discussion_text.strip() == "":
        st.warning("⚠️ Please paste some text before analyzing.")
    else:
        # Placeholder outputs (later we hook to backend)
        st.subheader("📌 Results")
        st.markdown("**Summary:** This is a placeholder summary of the discussion.")
        st.markdown("**Toxicity Check:** Safe ✅")
        st.markdown("**Recommendations:** You may also like: Thread A, Thread B, Thread C")
