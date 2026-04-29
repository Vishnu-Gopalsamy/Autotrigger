from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>CI Pipeline Dashboard</title>
    </head>
    <body>

        <center>
            <h1>🚀 Continuous Integration Dashboard</h1>
            <h2>Dockerized Application using Jenkins + GitHub</h2>
        </center>

        <hr>

        <h3>📌 Project Title</h3>
        <p>
            Automated CI Pipeline for Dockerized Applications using Jenkins and GitHub
        </p>

        <hr>

        <h3>⚙️ Tools Used</h3>
        <ul>
            <li>GitHub</li>
            <li>Jenkins</li>
            <li>Docker</li>
            <li>Docker Hub</li>
            <li>Flask</li>
        </ul>

        <hr>

        <h3>✅ Pipeline Status</h3>
        <p>✔ GitHub Webhook Triggered Successfully</p>
        <p>✔ Docker Image Built Successfully</p>
        <p>✔ Container Test Passed</p>
        <p>✔ Docker Image Pushed to Docker Hub</p>

        <hr>

        <h3>🖥 Application Output</h3>
        <pre>
Hello World
Changed now
Test Successful
        </pre>

        <hr>

        <h3>📊 Project Scope</h3>
        <p>
            This project automates the software development workflow using Jenkins CI pipeline.
            Whenever code is pushed to GitHub, Jenkins automatically builds the Docker image,
            runs the container for testing, and pushes the final verified image to Docker Hub.
            This reduces manual effort and improves deployment speed and reliability.
        </p>

        <hr>

        <center>
            <h3>🎯 Final Result</h3>
            <p><b>Project completed successfully with Continuous Integration workflow.</b></p>
        </center>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
