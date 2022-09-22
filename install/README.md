#  MailGrab

####  A Powerful Email Harvester Tool By OCEAN OF ANYTHING

# requirements 
  

 - Python 3.9 (keep Scrawling To See Installation Tutorial)
 - Windows/Linux/Mac
 - Pip3
 - Internet Connection (Obviously😜)

#  Installation Process

  

##  Windows 

  

Just Run The `install.bat` File And Wait For The Installation To Complete.

  

```shell
install.bat
```
or
```shell
python -u install.py
```

  

##  Linux
  

Its Just Simple As That 😎. Just Run The Following Command And Wait For The Installation To Complete🙂.

  

```shell
sudo python -u install.py
```

> ProTip! It's Necessary To Run Tis In Root Or Sudo


## Mac

Its Also V3ery Easy To Install This On Mac. Just Run The Following Command And Wait Until the installation is Complete

```shell
sudo python -u install.py
```

> ProTip! It's Necessary To Run Tis In Root Or Sudo



#####  Install **Python 3.9** In Your Pc And Do The Followings

#####  Install Python 3.9

Go And Visit The Official Page Of Python. Then Install Python On Your System. Make Sure To Install Python Version 3.9.0. To Prevent Any ~~Mistake~~ Please Use Link Bellow

You Can Also Install From This [Link](https://www.python.org/downloads/release/python-390/)

#####  For Linux Or Ubuntu

Install Python 3.9 In Linux.

  

1.  #####  Step1- Install supporting additional packages

```shell
sudo apt install software-properties-common
```

  

![enter image description here](https://cloudlinuxtech.com/ezoimgfmt/i1.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/install-software-properties-common-ubuntu.png?resize=1024,360&ssl=1&ezimgfmt=ng:webp/ngcb55)

  

2.  #####  Step2- Add Deadsnakes Ppa Repository To Install Latest Python 3.9

Open Terminal And Enter The Following Command

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
```

  

![add-deadsnakes-ppa](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/add-deadsnake-ppa-for-latest-python-1024x66.png?resize=1024%2C66&ezimgfmt=rs:640x41/rscb55/ng:webp/ngcb55)

  
  

3.  #####  Step3- Update Ubuntu/Kali Repository

```shell
sudo apt update
```

  

![sudo-apt-update](https://cloudlinuxtech.com/ezoimgfmt/i1.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/sudo-apt-update.png?resize=918%2C282&ezimgfmt=rs:640x197/rscb55/ng:webp/ngcb55)

  
  

4.  #####  Step4- Install latest Python 3 (Version 3.9.0)

```shell
sudo apt install python3.9
```

  

![How-to-install-Python-in-Linux](https://cloudlinuxtech.com/ezoimgfmt/i0.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/how-to-install-python-linux.png?resize=922%2C391&ezimgfmt=rs:640x271/rscb55/ng:webp/ngcb55)

  
  

5.  #####  Step5- Check python version

```shell
python --version
```

#####  Installing Pip (Only For Linux Or Ubuntu)

By-default _python3-pip_ is not installed in Ubuntu 20.04 and installing it from **apt** will install old pip package. So let's see step by step installation of latest **python3-pip**  **version (20.3.3)**. It will be a two-step process, first, we will install **pip 20.0.2** using the apt repository. Then, download and install the latest pip package i.e. 20.3.3 version.

  

1.  #####  Step1- Install python3-pip package using apt command

```shell
sudo apt install python3-pip
```

  

![How-to-install-Python3-pip](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Install-python3-pip-using-apt-1024x425.png?resize=1024%2C425&ezimgfmt=rs:640x266/rscb55/ng:webp/ngcb55)

  
  

2.  #####  Step2- Check python3-pip version

  

Here pip version 20.0.2 got installed and we need to **upgrade** it to version 20.3.3. Installing package 3.8 from **apt** will help to meet all dependent packages and libraries which will be required for **pip 20.3.3**. If you will skip this step, you may get dependent modules error.

  
  

![check-latest-pip-version](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/check-pip3-version-1.png?resize=862%2C147&ezimgfmt=rs:640x109/rscb55/ng:webp/ngcb55)

  
  

3.  #####  Step3- Install **curl** command first.

  

If curl is already installed your system, you can skip this step. Most of the Ubuntu 20.04 don't have curl installed by default. So use **apt install** command to install it. **Curl** is required to execute _step 4_.

  

```shell
sudo apt install curl
```

  

![install-curl](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Install-curl-package-1.png?resize=883%2C416&ezimgfmt=rs:640x301/rscb55/ng:webp/ngcb55)

  
  

4.  #####  Step4- Download pip from **bootstrap.pypa.io** website

Now you need to **download get pip** from bootstrap.pypa.io website using **curl** command as shown in image.

```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

  

![download-pip-script](https://cloudlinuxtech.com/ezoimgfmt/i0.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Download-python3-pip-1024x167.png?resize=1024%2C167&ezimgfmt=rs:640x104/rscb55/ng:webp/ngcb55)

  
  

5.  #####  Step5- Upgrade python3-pip version to pip-20.3.3

  

Run **python3.9** command to execute "get-pip.py" package file you downloaded. It will automatically download and install the latest pip in your Ubuntu/Kali Linux.

```shell
sudo python3.9 get-pip.py
```

  

![Install-python3-pip-ubuntu-20.04](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Install-latest-pip-20.3.3-ubuntu-20.04-1024x229.png?resize=1024%2C229&ezimgfmt=rs:640x143/rscb55/ng:webp/ngcb55)

  
  

6.  #####  Step6 (optional)- Add pip3.9 directory to PATH.

This can be achieved by editing **/etc/environment** file using your favourite editor. Otherwise, exporting and appending "**PATH**" variable for the local user profile will also do the trick. Make sure you add _~/.local/bin/_ in PATH variable.

```shell
export PATH=~/.local/bin/:$PATH
```

  

![add-pip-path-variable](https://cloudlinuxtech.com/ezoimgfmt/i0.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Add-pip-path-variable-2-1024x79.png?resize=1024%2C79&ezimgfmt=rs:640x49/rscb55/ng:webp/ngcb55)