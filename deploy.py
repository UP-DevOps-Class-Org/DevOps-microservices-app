import sys


def switch_app_deployment(deployment_arg):
    match deployment_arg:
        case "app1":
            print("Gonna deploy app1")
        case "app2":
            print("Gonna deploy app2")
        case "app3":
            print("Gonna deploy app3")
        case _:
            print("")


def deploy():
    for app in sys.argv[1:]:
        switch_app_deployment(app)
    print('Argument List: ', str(sys.argv))


if __name__ == '__main__':
    deploy()
