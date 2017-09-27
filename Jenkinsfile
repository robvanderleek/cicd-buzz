node {
 	// Clean workspace before doing anything yes
    deleteDir()

    try {
        stage ('Clone') {
        	checkout scm
                sh('git rev-parse --short HEAD -- > GIT_COMMIT')
                GIT_SHORTHASH=readFile('GIT_COMMIT')
                APP=cicd-buzz
        }
        stage ('Build') {
                IMAGE_TAG=$(GIT_SHORT_HASH)
        	sh "docker build -t ${APP}:${IMAGE_TAG} ."
        }
        stage ('Tests') {
	        parallel 'static': {
	            sh "echo 'shell scripts to run static tests...'"
	        },
	        'unit': {
	            sh "echo 'shell scripts to run unit tests...'"
	        },
	        'integration': {
	            sh "echo 'shell scripts to run integration tests...'"
	        }
        }
      	stage ('Deploy') {
            sh "echo 'shell scripts to deploy to server...'"
      	}
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
