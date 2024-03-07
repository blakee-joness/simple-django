pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Testing the app'
            }
        }
        stage('Build') {
            input {
                message "Deploy to production?"
                id "simple-input"
            }
            steps {
                echo 'Building the app'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the app'
            }
        }
    }
}
