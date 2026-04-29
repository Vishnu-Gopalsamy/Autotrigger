import streamlit as st

st.set_page_config(page_title="CI Pipeline Dashboard", layout="centered")

st.title("🚀 Continuous Integration Dashboard")
st.subheader("Dockerized Application using Jenkins + GitHub")

st.write("### Project Title")
st.write("Automated CI Pipeline for Dockerized Applications using Jenkins and GitHub")



st.write("### Pipeline Status")
st.success("GitHub Webhook Triggered Successfully")
st.success("Docker Image Built Successfully")
st.success("Container Test Passed")
st.success("Docker Image Pushed to Docker Hub")

st.write("### Application Output")
st.code("""Hello World\nChanged now\now""")

st.info("Project completed successfully with Continuous Integration workflow.")
