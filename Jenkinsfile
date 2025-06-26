node("docker") {
    stage('Get Install Builder') {
        checkout scm
        sh "python3 python-test.py"
    }
} 
