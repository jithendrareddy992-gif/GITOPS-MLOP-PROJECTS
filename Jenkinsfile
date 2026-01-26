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
                echo "Docker image build stage (demo)"
                sh "echo docker build -t ${DOCKER_HUB_REPO}:latest ."
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                echo "Docker image push stage (demo)"
                sh "echo docker push ${DOCKER_HUB_REPO}:latest"
            }
        }

        stage('Kubernetes & ArgoCD Deployment') {
            steps {
                echo "Argo CD GitOps deployment stage (demo)"
            }
        }
    }
}

        stage('Install Kubectl & ArgoCD CLI Setup') {
            steps {
                sh '''
                echo 'installing Kubectl & ArgoCD cli...'
                curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                chmod +x kubectl
                mv kubectl /usr/local/bin/kubectl
                curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
                chmod +x /usr/local/bin/argocd
                '''
            }
        }
        stage('Apply Kubernetes & Sync App with ArgoCD') {
            steps {
                script {kubeconfig(credentialsId: 'kubeconfig', serverUrl: ' https://127.0.0.1:32771') {
    // some block
}
                     {
                        sh '''
                        argocd login localhost:8081/applications --username admin --password $(kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d) --insecure
                        argocd app sync gitopsapp
                        '''
                    }
                }
            }
        }
    }
}

