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

        stage('Install Tools') {
            steps {
                sh '''
                echo "Installing kubectl"
                curl -LO https://dl.k8s.io/release/v1.29.0/bin/linux/amd64/kubectl
                chmod +x kubectl
                mv kubectl /usr/local/bin/kubectl

                echo "Installing argocd CLI"
                curl -sSL -o /usr/local/bin/argocd \
                https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
                chmod +x /usr/local/bin/argocd
                '''
            }
        }

        stage('ArgoCD GitOps Sync') {
            steps {
                echo "GitOps sync stage completed (demo)"
            }
        }
    }
}
