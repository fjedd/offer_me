pipeline {
    agent any
    environment {
        COMPOSE_FILE = "docker-compose.yml"
        POSTGRES_DB = "postgres"
        POSTGRES_USERNAME = "postgres"
        POSTGRES_PASSWORD = "postgres"
        POSTGRES_HOST = "db"
        POSTGRES_PORT = "5432"

    }
    stages {
        stage("Build and start image") {
            steps {
                sh "docker-compose build"
                sh "docker-compose up -d"
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker-compose exec -T pytest'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker-compose down'
            }
        }
    }
}
