pipeline {
    agent none 
    parameters {
        choice(name: 'HEDEF_ORTAM', choices: ['Development', 'Production'], description: 'Uygulama hangi ortama gönderilsin?')
        booleanParam(name: 'TEST_ET', defaultValue: true, description: 'Testler koşulsun mu? (Acil durumlarda kapatılabilir)')
    }

    stages {
        stage('Test Aşaması') {
            when {
                expression { return params.TEST_ET } 
            }
            agent {
                docker { image 'python:3.9-alpine' }
            }
            steps {
                sh 'pip install unittest-xml-reporting'
                
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
    stage('Deploy (Dağıtım) Aşaması') {
        agent { 
            docker { image 'alpine:latest' } 
        }
        steps {
            script {
                if (params.HEDEF_ORTAM == 'Production') {
                    echo "🚨 DİKKAT: CANLI SİSTEME (PRODUCTION) ÇIKILIYOR! 🚨"
                } else {
                    echo "🛠️ Geliştirme (Development) ortamına güncelleniyor..."
                }
            }
            echo "Deploy işlemi tamamlandı: ${params.HEDEF_ORTAM}"
        }
    }
    
    }
}