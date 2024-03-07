pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Testing the app'
            }
        }
        stage('Build') {
            when { equals expected: true, actual: Deploy }
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
