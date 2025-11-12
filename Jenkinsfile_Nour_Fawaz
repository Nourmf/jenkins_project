pipeline {
  agent any
  environment { VIRTUAL_ENV = 'venv' }

  stages {
    stage('Setup') {
      steps {
        // On Windows agents, replace sh with bat and use: "venv\\Scripts\\activate && ..."
        sh '''
          if [ ! -d "$VIRTUAL_ENV" ]; then python -m venv $VIRTUAL_ENV; fi
          . $VIRTUAL_ENV/bin/activate
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Lint') {
      steps {
        sh '''
          . $VIRTUAL_ENV/bin/activate
          flake8 app.py
        '''
      }
    }

    stage('Test') {
      steps {
        sh '''
          . $VIRTUAL_ENV/bin/activate
          pytest -q
        '''
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying application...' // placeholder per lab
      }
    }
  }

  post {
    always {
      cleanWs()
    }
  }
}
