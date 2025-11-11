pipeline {
  agent any
  environment {
    DOCKER_IMAGE = "imp98/aceest-fitness:${env.BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') {
      steps { git 'https://github.com/pguser12-beep/ACEest_Fitness.git' }
    }
    stage('Test') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest'
      }
    }
    stage('SonarQube analysis') {
      steps {
        // Needs SonarQube Jenkins plugin configured
        withSonarQubeEnv('My SonarQube Server') {
          sh 'sonar-scanner'
        }
      }
    }
    stage('Build Docker image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }
    stage('Push Docker image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-id', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          sh 'docker push $DOCKER_IMAGE'
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f k8s/deployment.yaml'
      }
    }
  }
  post {
    always {
      junit '**/TEST-*.xml'
      cleanWs()
    }
  }
}

