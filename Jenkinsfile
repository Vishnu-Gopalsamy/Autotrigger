pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Vishnu-Gopalsamy/Autotrigger.git'
            }
        }

        stage('Build') {
            steps {
                echo "Running Python App"
                sh 'python3 main.py'
            }
        }
    }
}
