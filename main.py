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
                background-color: #f4f7fa;
                font-family: Arial, sans-serif;
                margin: 40px;
                color: #333;
            }

            h1 {
                color: #0d6efd;
            }

            h2 {
                color: #198754;
            }

            h3 {
                color: #dc3545;
            }

            p {
                font-size: 16px;
            }

            .box {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }

            .success {
                color: green;
                font-weight: bold;
            }

            pre {
                background-color: #eeeeee;
                padding: 15px;
                border-radius: 8px;
                font-size: 15px;
            }

            hr {
                border: 1px solid #ccc;
            }
        </style>
    </head>
    <body>

        <center>
            <h1>🚀 Continuous Integration Dashboard</h1>
            <h2>Dockerized Application using Jenkins + GitHub</h2>
        </center>

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
            <pre>
Hello World
Changed now
Test Successful
            </pre>
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
            <center>
                <h3>🎯 Final Result</h3>
                <p><b>Project completed successfully with Continuous Integration workflow.</b></p>
            </center>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
