pipeline {
    agent none 

    stages {
        stage('Test Ortamı Hazırlığı') {
            agent {
                docker { image 'python:3.9-alpine' }
            }
            steps {
                sh 'python --version'
                echo 'Python container içindeyiz, testler başlıyor...'
                
                sh 'python -m unittest discover'
            }
        }
    }
    
    post {
        success {
            echo '✅ Harika! Kodların sorunsuz çalışıyor.'
        }
        failure {
            echo '❌ Hata! Kodlarında bir bozukluk var.'
        }
    }
}