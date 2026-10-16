pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:${env.PATH}"
        STUDENT_NAME    = 'Yernar'
        STUDENT_SURNAME = 'Temirkhan'
        STUDENT_GROUP   = 'IT2-2314'
        STUDENT_ID      = '37722'
        IMAGE_NAME      = 'temirkhan-yernar-devops'
        CONTAINER_NAME  = 'temirkhan-yernar-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/app.py'
                echo 'Application syntax check passed'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    test -f Dockerfile
                    test -f docker-compose.yml
                    test -f Temirkhan_Yernar_info.txt
                    bash -n scripts/Temirkhan_Yernar_system.sh
                    echo "All checks passed"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
                sh 'docker images ${IMAGE_NAME}'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 8081:8080 \
                        -e STUDENT_NAME=${STUDENT_NAME} \
                        -e STUDENT_SURNAME=${STUDENT_SURNAME} \
                        -e STUDENT_GROUP=${STUDENT_GROUP} \
                        -e STUDENT_ID=${STUDENT_ID} \
                        ${IMAGE_NAME}
                    sleep 3
                    docker ps --filter name=${CONTAINER_NAME}
                    docker logs ${CONTAINER_NAME}
                    curl -s http://localhost:8081
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully' }
        failure { echo 'Pipeline failed' }
    }
}

