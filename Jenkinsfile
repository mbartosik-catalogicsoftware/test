node("windows2019") {
    stage('Get Install Builder') {
        checkout scm
        bat 'ls -la'
        bat "py python-test.py"
    }
} 
