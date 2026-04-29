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
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f5f7fa;
                padding: 40px;
            }
            h1 {
                color: #2c3e50;
            }
            h2 {
                color: #34495e;
            }
            .box {
                background: white;
                padding: 20px;
                margin: 20px auto;
                width: 70%;
                border-radius: 10px;
                box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
            }
            .success {
                color: green;
                font-weight: bold;
                margin: 10px 0;
            }
            pre {
                background: #f4f4f4;
                padding: 15px;
                border-radius: 8px;
                text-align: left;
                display: inline-block;
            }
        </style>
    </head>
    <body>

        <h1>🚀 Continuous Integration Dashboard</h1>
        <h2>Dockerized Application using Jenkins + GitHub</h2>

        <div class="box">
            <h3>Project Title</h3>
            <p>Automated CI Pipeline for Dockerized Applications using Jenkins and GitHub</p>
        </div>

        <div class="box">
            <h3>Pipeline Status</h3>
            <p class="success">✔ GitHub Webhook Triggered Successfully</p>
            <p class="success">✔ Docker Image Built Successfully</p>
            <p class="success">✔ Container Test Passed</p>
            <p class="success">✔ Docker Image Pushed to Docker Hub</p>
        </div>

        <div class="box">
            <h3>Application Output</h3>
            <pre>Hello World
Changed now
test</pre>
        </div>

        <div class="box">
            <p><b>Project completed successfully with Continuous Integration workflow.</b></p>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
