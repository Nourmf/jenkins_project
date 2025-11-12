pipeline {
    agent any
    environment { 
        VIRTUAL_ENV = 'myenv'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    bat "\"C:\\Users\\nour\\AppData\\Local\\Programs\\Python\\Python310\\python.exe\" -m venv ${VIRTUAL_ENV}"
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && ${VIRTUAL_ENV}\\Scripts\\python.exe -m pip install --upgrade pip"
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Lint') {
            steps {
                bat "call ${VIRTUAL_ENV}\\Scripts\\activate && flake8 app.py"
            }
        }

        stage('Test') {
            steps {
                bat "call ${VIRTUAL_ENV}\\Scripts\\activate && pytest"
            }
        }

        stage('Coverage') {
            steps {
                bat "call ${VIRTUAL_ENV}\\Scripts\\activate && coverage run -m pytest && coverage report"
            }
        }

        stage('Security') {
            steps {
                bat '''
                chcp 65001
                call myenv\\Scripts\\activate
                bandit -r . > bandit_report.txt
                type bandit_report.txt
                '''
            }
        }

        stage('Deploy Locally') {
            steps {
                echo "Deploying application..."
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
