import sys
import os


def build_deployment(deployment_arg):
    match deployment_arg:
        case "app1":
            print("Building " + deployment_arg + ".....")
            os.system('cd ProjectsApp && cd financial-service-web && docker build -t financial-service-web .')
            os.system('docker stack deploy node --compose-file docker-compose-microservices.yml --with-registry-auth')
        case "app2":
            print("Building " + deployment_arg + ".....")
            os.system('cd ProjectsApp && cd pet-shop-web && docker build -t pet-shop-web .')
            os.system('docker stack deploy node --compose-file docker-compose-microservices.yml --with-registry-auth')

        case "app3":
            print("Building " + deployment_arg + ".....")
            os.system('cd ProjectsApp && cd selo-web && docker build -t selo-web .')
            os.system('docker stack deploy node --compose-file docker-compose-microservices.yml --with-registry-auth')
        case "all":
            print("Building " + deployment_arg + ".....")
            os.system('cd ProjectsApp && cd financial-service-web && docker build -t financial-service-web .')
            os.system('cd ProjectsApp && cd pet-shop-web && docker build -t pet-shop-web .')
            os.system('cd ProjectsApp && cd selo-web && docker build -t selo-web .')
            os.system('docker stack deploy node --compose-file docker-compose-microservices.yml --with-registry-auth')


def deploy():
    for app in sys.argv[1:]:
        build_deployment(app)

    # start swarm services
    # docker stack deploy node --compose-file docker-compose.yml --with-registry-auth

    # stop swarm services
    # docker stack rm node

    # print('Argument List: ', str(sys.argv))


if __name__ == '__main__':
    deploy()
