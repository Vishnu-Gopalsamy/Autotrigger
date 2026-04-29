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
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container Test') {
            steps {
                echo "Running container test..."

                // Remove old container if it exists
                sh 'docker rm -f test-container || true'

                sh 'docker run -d --name test-container -p 8501:8501 $IMAGE_NAME'
                sh 'sleep 10'
                sh 'docker logs test-container'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image to Docker Hub..."

                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-cred',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up container..."

            // Remove container after execution
            sh 'docker rm -f test-container || true'
        }

        success {
            echo "Pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed. Please check logs."
        }
    }
}
