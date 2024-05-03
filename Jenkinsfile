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
                sh "cp .env.dev .env"
                sh "docker-compose build"
                sh "docker-compose up -d"
            }
        }

        stage('Run tests') {
            steps {
                script {
                    sh 'docker-compose exec -T app pytest -p no:cacheprovider'
                }
            }
        }

        stage('Run automatic web tests') {
            steps {
                script {
                    sh 'docker-compose exec -T app python manage.py create_example_data'
                    sh "ls -lah"
                    sh 'docker-compose exec -T test pytest -p no:cacheprovider'
                    sh 'rm .auth/state.json'
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
