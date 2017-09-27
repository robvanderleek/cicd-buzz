node ('ecs-staging') {
 	// Clean workspace before doing anything yes
    deleteDir()

    try {

        environment {
             // FOO will be available in entire pipeline
                APP = "cicd-buzz"
        }
        stage ('Clone') {
        	checkout scm
               sh('git rev-parse --short HEAD > GIT_COMMIT')
               def shortCommit = readFile('GIT_COMMIT').take(6)
        }
        stage ('Build') {
        	//sh "docker build -t $APP:$short_commit ."
                app = docker.build("cicd-buzz:${shortCommit}")
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
