from dotenv import load_dotenv
load_dotenv()   # MUST be first

import streamlit as st
from crew import WorkflowCrew

st.set_page_config(page_title="AI Workflow Optimizer", page_icon="🚀")
st.title("🤖 AI Workflow Optimizer")
st.write("Turn your chaotic day into a high-performance schedule.")

user_data = st.text_area(
    "Paste your day's tasks (e.g., 9am-11am: Emails, 11am-1pm: Meeting...)",
    height=200
)

if st.button("Optimize My Data"):
    if user_data:
        with st.spinner("Analyzing your day..."):
            try:
                crew_instance = WorkflowCrew(user_data)

                result = crew_instance.build().kickoff()

                st.success("Optimization Complete!")
                st.markdown("### 📋 Your Optimized Plan")
                st.write(result)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some tasks first!")
