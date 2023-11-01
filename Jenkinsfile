pipeline{
    agent any

    
    parameters{

    booleanParam(name:'check',defaultValue:true, description:"this is for check purpose")
    
    }

    stages{
        stage("A"){
            steps{
                echo "this is printing A"
            }

            post{
                always{

                    echo "completed successfully"

                }

                success{

                    echo "this will print when it is success"

                }
                failure{

                    echo "this will print when it is failure"

                }
            }
        }

        stage("docker"){

            when{
                expression{
                    params.check
                }
            }


            steps{
                withCredentials([usernamePassword(credentialsId:'docker-repo',usernameVariable:'user',passwordVariable:'pass')]){

                    sh ' docker login -u $user -p $pass'



                }
            }
        }
    }

    post{
        always{
            echo "====++++always++++===="
        }
        success{
            echo "====++++only when successful++++===="
        }
        failure{
            echo "====++++only when failed++++===="
        }
    }
}
