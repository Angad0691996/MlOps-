pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yourname/mlops-cat-dog.git'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 train.py'
            }
        }

        stage('Run Inference') {
            steps {
                sh 'python3 inference.py data/test/some_image.jpg'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t catdog-detector .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push catdog-detector
                    '''
                }
            }
        }
    }
}
