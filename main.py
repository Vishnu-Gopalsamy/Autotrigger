from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>CI Pipeline Dashboard</title>
        <style>
            body {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: Consolas, monospace;
                margin: 30px;
            }

            h1 {
                color: #58a6ff;
                text-align: center;
            }

            h2 {
                color: #3fb950;
                text-align: center;
            }

            h3 {
                color: #f85149;
            }

            .box {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            }

            .success {
                color: #3fb950;
                font-weight: bold;
            }

            .code-box {
                background-color: #010409;
                border: 1px solid #30363d;
                padding: 15px;
                border-radius: 8px;
                color: #79c0ff;
                white-space: pre-wrap;
                font-size: 15px;
            }

            p {
                line-height: 1.6;
            }

            hr {
                border: 1px solid #30363d;
            }
        </style>
    </head>
    <body>

        <h1>🚀 Continuous Integration Dashboard</h1>
        <h2>Dockerized Application using Jenkins + GitHub</h2>

        <div class="box">
            <h3>📌 Project Title</h3>
            <p>
                Automated CI Pipeline for Dockerized Applications using Jenkins and GitHub
            </p>
        </div>

        <div class="box">
            <h3>✅ Pipeline Status</h3>
            <p class="success">✔ GitHub Webhook Triggered Successfully</p>
            <p class="success">✔ Docker Image Built Successfully</p>
            <p class="success">✔ Container Test Passed</p>
            <p class="success">✔ Docker Image Pushed to Docker Hub</p>
        </div>

        <div class="box">
            <h3>🖥 Application Output</h3>
            <div class="code-box">
Hello World
Changed now
Test Successful
            </div>
        </div>

        <div class="box">
            <h3>📊 Project Scope</h3>
            <p>
                This project automates the software development workflow using Jenkins CI pipeline.
                Whenever code is pushed to GitHub, Jenkins automatically builds the Docker image,
                runs the container for testing, and pushes the final verified image to Docker Hub.
                This reduces manual effort and improves deployment speed and reliability.
            </p>
        </div>

        <div class="box">
            <h3>🎯 Final Result</h3>
            <p>
                <b>Project completed successfully with Continuous Integration workflow.</b>
            </p>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
