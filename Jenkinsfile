
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'docker-tut-backend:ci'
        KUBECONFIG = '/var/jenkins_home/.kube/config'
        IMAGE_ARCHIVE = '/tmp/backend-ci.tar'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                dir('backend') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        python -m unittest -v
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME backend/'
            }
        }

        stage('Load Image into Minikube') {
            steps {
                sh '''
                    docker save "$IMAGE_NAME" -o "$IMAGE_ARCHIVE"
                    docker exec -i minikube ctr -n k8s.io images import - < "$IMAGE_ARCHIVE"
                    rm -f "$IMAGE_ARCHIVE"
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl set image deployment/flask-deployment flask="$IMAGE_NAME"
                    kubectl rollout status deployment/flask-deployment --timeout=120s
                    kubectl get deployment flask-deployment
                '''
            }
        }
    }
}

