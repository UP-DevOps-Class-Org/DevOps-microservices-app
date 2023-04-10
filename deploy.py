import os
import subprocess
import sys

from colorama import init, Fore, Style


def deploy():
    # Initialize colorama
    init(autoreset=True)

# In case you want to deploy all microservices
# Loop through input arguments from command line

    for app in sys.argv[1:]:
        if(app == 'all'):
           
           # Loop through all directories in the current working directory
            for dirname in os.listdir():
                if os.path.isdir(dirname):
                    # cd microservices
                    os.chdir(dirname)
                    for project in os.listdir():
                        # Loop through all project files in the current(microservices) working directory
                        if project != '.DS_Store' and os.path.exists(os.path.join(project, 'Dockerfile')):
                            build_docker_images(project)
            break
# In case of one mircoservices or multiple 
        elif(len(sys.argv) >= 2):
            for dirname in os.listdir():
                if os.path.isdir(dirname):
                    os.chdir(dirname)
                    for project in os.listdir():
                        for i in (sys.argv):
                            if(i == project and i != 'deploy.py'):
                                build_docker_images(i)
            break                    
    else:
        print(f'{Fore.RED} Invalid {app} name {Style.RESET_ALL}')


def build_docker_images(dir_project):
    os.chdir(dir_project)

    # Build Docker image using the CLI
    result = subprocess.run(
        ['docker', 'build', '-t', f'{dir_project}', '.'])

    # Check if the build was successful
    if result.returncode == 0:
        os.chdir("..")
        print(
            f'{Fore.GREEN}{dir_project} image build successfully {Style.RESET_ALL} \n')
    else:
        print(
            f'{Fore.RED}{dir_project} image build failed {Style.RESET_ALL}')


def docker_login_registry():
    print(f'{Fore.GREEN} docker_login_registry')


def get_current_directory():
    result = ''
    for dirname in os.listdir():
        if os.path.isdir(dirname):
            os.chdir(dirname)
            for project in os.listdir():
                result = project
    return result

# def deploy():

    # for app in sys.argv[1:]:
    #     print(app)

    # build_deployment(app)

    # start swarm services
    # docker stack deploy node --compose-file docker-compose.yml --with-registry-auth
    # stop swarm services
    # docker stack rm node
    # print('Argument List: ', str(sys.argv))
if __name__ == '__main__':
    deploy()
