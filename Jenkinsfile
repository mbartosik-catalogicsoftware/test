node("docker") {
    stage('Get Install Builder') {
        checkout scm
        sh 'ls -la'
        sh "python3 python-test.py"
    }
} 