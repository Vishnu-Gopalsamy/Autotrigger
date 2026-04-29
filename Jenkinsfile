pipeline {
    agent any

    environment {
        IMAGE_NAME = "vishnugopalsamy/autotrigger"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Clean Docker Space') {
            steps {
                echo "Cleaning Docker space..."

                sh '''
                docker system prune -a -f
                docker volume prune -f
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container Test') {
            steps {
                echo "Running container test..."

                sh '''
                docker ps -aq --filter "name=test-container" | xargs -r docker rm -f
                '''

                sh '''
                docker run -d --name test-container -p 8501:8501 $IMAGE_NAME
                sleep 10
                docker logs test-container
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image..."

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
            echo "Final cleanup..."

            sh '''
            docker rm -f test-container || true
            '''
        }
    }
}
