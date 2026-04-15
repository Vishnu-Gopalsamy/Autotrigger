pipeline {
    agent any

    environment {
        IMAGE_NAME = "vishnu/autotrigger"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container Test') {
            steps {
                // Remove old container if exists (prevents errors)
                sh 'docker rm -f test-container || true'

                // Run container in foreground to see output
                sh 'docker run --name test-container $IMAGE_NAME'
            }
        }
    }

    post {
        always {
            // Cleanup after execution
            sh 'docker rm -f test-container || true'
        }
    }
}
