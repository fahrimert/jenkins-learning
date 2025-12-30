pipeline {
    agent none 

    stages {
        stage('Test Ortamı Hazırlığı') {
            agent {
                docker { image 'python:3.9-alpine' }
            }
            steps {
                echo '📦 Gerekli paketler yükleniyor...'
                sh 'pip install unittest-xml-reporting'
                
                echo '🚀 Testler XML Raporu üretecek şekilde başlatılıyor...'
                sh 'python -m xmlrunner discover -o test-reports'
            }
    post {
        always {
            junit 'test-reports/*.xml'
        }
        success {
            echo '✅ Harika! Kodların sorunsuz çalışıyor.'
        }
        failure {
            echo '❌ Hata! Kodlarında bir bozukluk var.'
        }
    }
        }
    
    }
}