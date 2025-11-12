pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\Users\nour\AppData\Local\Programs\Python\Python310\python.exe'
    }

    stages {
        stage('Setup') {
            steps {
                bat '''
                "%PYTHON_PATH%" -m venv venv
                call venv\\Scripts\\activate
                "%PYTHON_PATH%" -m pip install --upgrade pip
                "%PYTHON_PATH%" -m pip install -r requirements.txt
                '''
            }
        }
    }
}
