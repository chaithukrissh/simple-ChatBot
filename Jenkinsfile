pipeline{
    agent any


    parameters{

    booleanParam(name:'check',defaultValue:true, description:"this is for check purpose")

    }

    stages{
        stage("Docker Build"){
            steps{
                echo "this stage is for building the docker image"
                sh " docker build -t ChatBot:1.0 ."
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

                sh " docker tag ChatBot:1.0 chaithukrissh/ChatBot:1.0"
                sh " docker push  chaithukrissh/ChatBot:1.0 "
    }
        }
}
