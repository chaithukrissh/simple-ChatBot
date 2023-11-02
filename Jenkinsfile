pipeline{
    agent any


    parameters{

    booleanParam(name:'check',defaultValue:true, description:"this is for check purpose")

    }

    environment {
        // Define the version number using the Jenkins BUILD_NUMBER
        VERSION = "${BUILD_NUMBER}"
        IMAGE_NAME="chatbot"
        DOCKER_IMAGE_TAG = "${IMAGE_NAME}:${VERSION}"
        DOCKER_HUB_REPO = "chaithukrissh/chatbot"
        DOCKER_HUB_TAG = "${DOCKER_HUB_REPO}:${VERSION}"
    }

    stages {
        stage('Prepare Dockerfile') {
            steps {
                script {
                    // Define the placeholder in the Dockerfile
                    def placeholder = "##VERSION_PLACEHOLDER##"

                    // Read the Dockerfile content
                    def dockerfileContent = readFile("Dockerfile")

                    // Replace the placeholder with the version number
                    def updatedDockerfileContent = dockerfileContent.replaceAll(placeholder, VERSION)

                    // Write the updated content back to the Dockerfile
                    writeFile(file: "Dockerfile", text: updatedDockerfileContent)
                }
            }
        }
        

        stage("docker login"){

            when{
                expression{
                    params.check
                }
            }

steps{
                withCredentials([usernamePassword(credentialsId:'ChatBot' , usernameVariable:'user' , passwordVariable:'pass')]){
                         sh " docker login -u $user -p $pass "



                }



                }
            }

    
        stage("Image push to Docker hub "){

        steps{
                sh "docker build -t ${DOCKER_IMAGE_TAG} ."
                sh " docker tag ${DOCKER_IMAGE_TAG} ${DOCKER_HUB_TAG}"
                sh " docker push  ${DOCKER_HUB_TAG} "
    }
        }
    }
}
