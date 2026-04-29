from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Continuous Integration Dashboard</h1>
    <h2>Dockerized Application using Jenkins + GitHub</h2>

    <h3>Project Title</h3>
    <p>Automated CI Pipeline for Dockerized Applications using Jenkins and GitHub</p>

    <h3>Pipeline Status</h3>
    <p>✔ GitHub Webhook Triggered Successfully</p>
    <p>✔ Docker Image Built Successfully</p>
    <p>✔ Container Test Passed</p>
    <p>✔ Docker Image Pushed to Docker Hub</p>

    <h3>Application Output</h3>
    <pre>Hello World
Changed now
test</pre>

    <p><b>Project completed successfully with Continuous Integration workflow.</b></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
