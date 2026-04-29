import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="CI Pipeline Dashboard", layout="wide")

st.title("🚀 Jenkins Real-Time Build History Dashboard")

st.subheader("Continuous Integration for Dockerized Application")

# Jenkins API URL
JENKINS_URL = "http://3.87.82.153:8080/job/docker-ci-project/api/json"

try:
    response = requests.get(JENKINS_URL)

    if response.status_code == 200:
        data = response.json()

        builds = []

        for build in data["builds"][:10]:
            builds.append({
                "Build Number": build["number"],
                "Build URL": build["url"]
            })

        df = pd.DataFrame(builds)

        st.success("✔ Real-time Jenkins build data fetched successfully")
        st.table(df)

    else:
        st.error("Failed to fetch Jenkins data")

except Exception as e:
    st.error(f"Connection Error: {e}")

st.write("### Tools Used")
st.write("- GitHub")
st.write("- Jenkins")
st.write("- Docker")
st.write("- Docker Hub")

st.info("This dashboard shows real-time Jenkins build updates for the CI pipeline project.")
