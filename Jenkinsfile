pipeline {
    agent any

    environment {
        IMAGE_NAME = "vishnugopalsamy/autotrigger"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container Test') {
            steps {
                sh 'docker rm -f test-container || true'
                sh 'docker run --name test-container $IMAGE_NAME'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker login -u vishnugopalsamy -p YOUR_PASSWORD'
                sh 'docker push $IMAGE_NAME'
            }
        }
    }

    post {
        always {
            sh 'docker rm -f test-container || true'
        }
    }
}
