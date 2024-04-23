pipeline {
    agent any
    environment {
        COMPOSE_FILE = "docker-compose.yml"
        DOCKERFILE = "Dockerfile-jenkins"
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

        stage('Run tests') {
            steps {
                script {
                    sh 'docker-compose exec app -T pytest'

                }
            }
        }

        stage('Run automatic web tests') {
            steps {
                script {
                    echo "Creating example data"
                    sh 'docker-compose exec app -T python manage.py create_example_data'
                    echo "Starting web tests"
                    sh 'docker-compose exec test -T pytest'
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
