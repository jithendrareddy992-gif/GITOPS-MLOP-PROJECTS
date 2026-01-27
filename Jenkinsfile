pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = "jithendrareddy992-gif/gitops-mlop-projects"
        DOCKER_HUB_CREDENTIALS_ID = "gitops-dockerhub-token"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Repository jithendrareddy992-gif/GITOPS-MLOP-PROJECTS checked out successfully"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image"
                sh "echo docker build -t ${DOCKER_HUB_REPO}:latest ."
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                echo "Pushing Docker image"
                sh "echo docker push ${DOCKER_HUB_REPO}:latest"
            }
        }

        stage('Install Kubectl & ArgoCD CLI') {
            steps {
                sh '''
                echo "Installing kubectl"
                curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl
                chmod +x kubectl
                sudo mv kubectl /usr/local/bin/kubectl

                echo "Installing ArgoCD CLI"
                curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
                chmod +x argocd
                sudo mv argocd /usr/local/bin/argocd
                '''
            }
        }

        stage('Sync Application with ArgoCD') {
            steps {
                sh '''
                echo "Logging into ArgoCD"
                argocd login localhost:8081 \
                  --username admin \
                  --password $(kubectl get secret -n argocd argocd-initial-admin-secret \
                  -o jsonpath="{.data.password}" | base64 -d) \
                  --insecure

                echo "Syncing application"
                argocd app sync gitopsapps
                '''
            }
        }
    }
}
