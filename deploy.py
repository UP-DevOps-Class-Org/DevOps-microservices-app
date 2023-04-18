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

    # Run docker login
    subprocess.run(['docker', 'login'])

    # Run the docker info command and capture the output
    output = subprocess.check_output(['docker', 'info']).decode()

    # Find the line containing the "Username" field
    username_line = [line for line in output.split('\n') if 'Username' in line]
    if username_line:
        # Extract the username from the line
        username = username_line[0].split(':')[1].strip()
    else:
        # Use a default username if the user is not logged in or has no username
        username = 'sithvothykiv'

    # Build the Docker image with the username in the tag
    tag = f'{username}/{dir_project}:latest'

    # Build Docker image using the CLI
    result_build = None
    result_pushed = None
    if os.path.isfile("docker-compose.yml"):
        result_build = subprocess.run(['docker', 'compose', 'build'])
    else:
        result_build = subprocess.run(['docker', 'build', '-t', tag, '.'])

    # Check if the build was successful
    if result_build.returncode == 0:
        print(
            f'{Fore.GREEN}{dir_project} image build successfully {Style.RESET_ALL} \n')
        if os.path.isfile("docker-compose.yml"):
            result_pushed = subprocess.run(['docker', 'compose', 'push'])
        else:
            result_pushed = subprocess.run(['docker', 'push', f'{tag}'])

        if result_pushed.returncode == 0:
            print(
                f'{Fore.GREEN}{dir_project} image push successfully {Style.RESET_ALL} \n')
            os.chdir("..")

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
