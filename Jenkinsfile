pipeline {
    agent any

    environment {
        IMAGE_NAME = "vishnu/autotrigger"
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Vishnu-Gopalsamy/Autotrigger.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container Test') {
            steps {
                sh 'docker run -d --name test-container $IMAGE_NAME'
                sh 'sleep 5'
                sh 'docker stop test-container'
                sh 'docker rm test-container'
            }
        }
    }
}
