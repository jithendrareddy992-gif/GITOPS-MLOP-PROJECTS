pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = "jithendrareddy992-gif/gitops-mlop-projects"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Repository checked out successfully"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image (demo)"
                sh "echo docker build -t ${DOCKER_HUB_REPO}:latest ."
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image (demo)"
                sh "echo docker push ${DOCKER_HUB_REPO}:latest"
            }
        }

        stage('GitOps Trigger') {
            steps {
                echo "ArgoCD will auto-sync from Git repository"
            }
        }
    }
}
