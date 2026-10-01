pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Registration HTML...'
                bat 'dir'
            }
        }

        stage('Test HTML') {
            steps {
                bat '''
                if not exist index.html (
                    echo ERROR: index.html not found
                    exit /b 1
                )

                findstr /C:"<html" index.html >nul
                if errorlevel 1 exit /b 1

                findstr /C:"<form" index.html >nul
                if errorlevel 1 exit /b 1

                findstr /C:"<input" index.html >nul
                if errorlevel 1 exit /b 1

                findstr /C:"<button" index.html >nul
                if errorlevel 1 exit /b 1

                echo HTML TEST PASSED
                '''
            }
        }
    }

    post {
        success {
            echo 'Build and HTML Test Successful!'
        }

        failure {
            echo 'HTML Test Failed!'
        }
    }
}