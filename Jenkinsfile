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
               // write a file with the short git hash
                sh 'git rev-parse HEAD > GIT_COMMIT'
                def shortCommit = readFile('GIT_COMMIT').take(6)
        }
        stage ('Build') {
        	// Get the short git hash and use it as the $IMAGE_TAG variable
                def IMAGE_TAG = readFile('GIT_COMMIT').take(6)
                app = docker.build("cicd-buzz:${IMAGE_TAG}")
        }
        stage ('Tests') {
	        parallel 'static': {
                  node ('ecs-staging')
                    def IMAGE_TAG = readFile('GIT_COMMIT').take(6)
//                    docker.image("cicd-buzz:${IMAGE_TAG}").inside {
//                       sh """pip freeze"""
                      docker.image('maven:3.3.3-jdk-8').inside {
                      sh 'ls -all'
                 }
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
