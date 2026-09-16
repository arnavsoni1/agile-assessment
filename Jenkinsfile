pipeline {
    agent any

    environment {
        IMAGE = 'arnavsoni2007/assessment-build'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                powershell 'python3 main.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                powershell 'docker build -t "${env:IMAGE}:${env:BUILD_NUMBER}" -t "${env:IMAGE}:latest" .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    powershell '''
                        $env:DOCKERHUB_TOKEN | docker login --username $env:DOCKERHUB_USER --password-stdin
                        docker push "${env:IMAGE}:${env:BUILD_NUMBER}"
                        docker push "${env:IMAGE}:latest"
                    '''
                }
            }
        }
    }
}