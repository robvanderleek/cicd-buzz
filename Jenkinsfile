node ('ecs-staging') {
 	// Clean workspace before doing anything yes
    deleteDir()

    try {
        stage ('Clone') {
        	checkout scm
                sh('git rev-parse --short HEAD -- > GIT_COMMIT')
                git_shortcommit=readFile('GIT_COMMIT')
        }
        stage ('Build') {
        	sh "echo short commit version $git_shortcommit && ls -all && pwd && uptime  && echo $HOSTNAME && echo 'shell scripts to build project...'"
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
