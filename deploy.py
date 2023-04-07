import sys
import os


def build_deployment(deployment_arg):
    match deployment_arg:
        case "app1":
            print("Building " + deployment_arg + ".....")
            os.system('cd microservices && cd nodejs-express-mongodb && docker build -t nodejs-express-mongodb .')
            os.system('docker stack deploy node --compose-file docker-compose.yml --with-registry-auth')
        case "app2":
            print("Building " + deployment_arg + ".....")
            os.system('cd microservices && cd pet-shop-web && docker build -t pet-shop-web .')
            os.system('docker stack deploy node --compose-file docker-compose.yml --with-registry-auth')

        case "app3":
            print("Building " + deployment_arg + ".....")
            os.system('cd microservices && cd selo-web && docker build -t selo-web .')
            os.system('docker stack deploy node --compose-file docker-compose.yml --with-registry-auth')
        case "app4":
            print("Building " + deployment_arg + ".....")
            os.system('cd microservices && cd php-sample-demo && docker build -t php-sample-demo .')
            os.system('docker stack deploy node --compose-file docker-compose.yml --with-registry-auth')

        case "all":
            print("Building " + deployment_arg + ".....")
            os.system('cd microservices && cd financial-service-web && docker build -t financial-service-web .')
            os.system('cd microservices && cd pet-shop-web && docker build -t pet-shop-web .')
            os.system('cd microservices && cd php-sample-demo && docker build -t php-sample-demo .')
            os.system('cd microservices && cd selo-web && docker build -t selo-web .')
            os.system('docker stack deploy node --compose-file docker-compose.yml --with-registry-auth')


def deploy():
    for app in sys.argv[1:]:
        build_deployment(app)

if __name__ == '__main__':
    deploy()
