node ('ecs-staging') {
 	// Clean workspace before doing anything yes
    deleteDir()

    try {
        stage ('Clone') {
        	checkout scm
                sh('git rev-parse --short HEAD > GIT_COMMIT')
                GIT_SHORTHASH=readFile('GIT_COMMIT')
                def APP=cicd-buzz
        }
        stage ('Build') {
                //IMAGE_TAG=$(GIT_SHORT_HASH)
        	//sh "which docker && docker build -t ${APP}:${IMAGE_TAG} ."
                sh "echo the short has his $GIT_SHORT_HASH"
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
