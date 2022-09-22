import os
import time
import sys


def osInfo():
    os_name = os.name
    if os_name in ("nt", "dos", "ce"):
        os_name = 'Windows'
        if os.system("ping -n 1 oceanofanythingofficial.github.io > nul") == 0:
            pass
        else:
            print("Internet Not Connected")
            exit()
    elif os_name == 'posix':
        os_name = 'Linux'
        if os.geteuid() != 0:
            print("Please run this script as root")
            exit()
        elif os.system("curl -s oceanofanythingofficial.github.io > /dev/null") == 0:
            print("Internet Connected")
        else:
            print("Internet Not Connected")
            exit()
    elif os_name == 'darwin':
        os_name = 'MacOS'
        if os.system("curl -s oceanofanythingofficial.github.io > /dev/null") == 0:
            pass
        else:
            print("Internet Not Connected")
            exit()
    else:
        os_name = 'Unknown'
    return os_name


def typeWrite(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


typeWrite(f"You Are Using {osInfo()} OS\n", 0.06)
typeWrite("Installing Requirements Needed For This Tool......\n", 0.06)


def installPackage(package):
    os.system(f"pip install {package} > log/{package}.log")


def mainProcess():

    packages = [
        'beautifulsoup4',
        'certifi',
        'charset-normalizer',
        'click',
        'collection',
        'colorama',
        'commonmark',
        'cursor',
        'idna',
        'lxml',
        'mypy-extensions',
        'pathspec',
        'platformdirs',
        'psutil',
        'Pygments',
        'regex',
        'requests',
        'rich',
        'soupsieve',
        'termcolor',
        'tomli',
        'typing_extensions',
        'urllib3'
    ]
    try:
        for package in packages:
            typeWrite(f"Installing {package} Module......\n", 0.03)
            if package in sys.modules:
                typeWrite(f"{package} Already Installed\n", 0.03)
            else:
                installPackage(package)
            typeWrite(f"Successfully installed {package} Module\n", 0.03)
    except Exception:
        try:
            os.system("pip install -r requirements.txt > log/requirements.log")
        except Exception as err:
            print(f"Can't Install Requirements {err}")


if __name__ == '__main__':
    mainProcess()
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    elif os.name == 'darwin':
        os.system('clear')
    else:
        os.system('cls||clear')
    sys.stderr.write("\x1b[2J\x1b[H")
    typeWrite("Successfully Installed All Requirements. Now You Can Use MailGrab Without Any Interruptions!\n\n\n", 0.03)
    typeWrite("                                 Happy Hacking !!!!!!! \n\n", 0.03)
    input("Press Any Key To Exit")
else:
    print("Please Run This Script Directly On Terminal")
