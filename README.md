<p align="center" width="100%">
    <img width="60%" align="center" src="https://oceanofanythingofficial.github.io/MailGrab/thumbnail.png"/>
    <div align="center">
    <a href="https://www.python.org/downloads/release/python-3912/" title="Go to Python homepage"><img src="https://img.shields.io/badge/Python-3.9-lemonyellow?logo=python&logoColor=white" alt="Made with Python"></a>
      <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/OCEANOFANYTHINGOFFICIAL/MailGrab?style=flat">
  <img alt="GitHub Repo Version" src="https://img.shields.io/badge/Version-2.0.0.0-brightgreen?style=flat">
  <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a href="https://www.linux.org/" title="Go to Linux homepage"><img src="https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white" alt="OS - Linux"></a>
  <a href="https://www.apple.com/macos/" title="Go to Apple homepage"><img src="https://img.shields.io/badge/OS-macOS-blue?logo=apple&logoColor=white" alt="OS - macOS"></a>
  <a href="https://www.microsoft.com/" title="Go to Microsoft homepage"><img src="https://img.shields.io/badge/OS-Windows-blue?logo=windows&logoColor=white" alt="OS - Windows"></a>
	<a href="https://oceanofanythingofficial.github.io/MailGrab" title="Go to GitHub Pages homepage"><img src="https://img.shields.io/badge/Hosted_with-GitHub_Pages-blue?logo=github&logoColor=white" alt="Hosted with GH Pages"></a>
	<img  src="https://img.shields.io/badge/maintained-yes-blue"  alt="maintained - yes">
	<div><a href="https://oceanofanythingofficial.github.io/MailGrab/" title="Go to project documentation"><img src="https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge" alt="view - Documentation"></a></div>
   </div>
</p>


<div>
  <strong>Just Provide Urls, And It Will Harvest Emails From Those Urls. Not Only One Url , It Will Automatically Find _SubUrls_ From Given Url. It Can Also Find Emails From Thousands Of Urls At One Time. Dont Have Time To Copy All Emails? No Worry! It Will Save All Emails And Harvested Urls In Saperate Text Files. Emails Will Be Saved In *`_emails.txt`* And Scrapped Urls Will Be Saved In *`_scrappedUrls.txt`*. You Can Provide A Huge List Of Urls To Be Scanned</strong>
</div>



  

##  requirements

  

- Python 3.9 (keep Scrawling To See Installation Tutorial)

- Windows/Linux/Mac

- Pip3

- Internet Connection (Obviously😜)

  

##  Installation

Clone The Repo From Official Page Of **OCEAN OF ANYTHING** And Change Directory To MailGrab

```
git clone https://github.com/oceanofanythingofficial/MailGrab

cd MailGrab
```

###  Windows

  

Just Run The `install.bat` File And Wait For The Installation To Complete.

  

```shell
install.bat
```

or

```shell
python -u install.py
```

  

###  Linux

Its Just Simple As That 😎. Just Run The Following Command And Wait For The Installation To Complete🙂.

  
  

```shell
sudo python -u install.py
```

  

> ProTip! It's Necessary To Run Tis In Root Or Sudo

  

###  Mac

  
  
  

#####  Install Python 3.9 (For Kids Who Dont Know How To Install Python 3.9)

  


Go And Visit The Official Page Of Python. Then Install Python On Your System. Make Sure To Install Python Version 3.9.0. To Prevent Any ~~Mistake~~ Please Use Link Bellow

You Can Also Install From This [Link](https://www.python.org/downloads/release/python-390/)

##### For Linux Or Ubuntu

Install Python 3.9 In Linux.

  

1. ##### Step1- Install supporting additional packages

```
sudo apt install software-properties-common
```

  

![enter image description here](https://cloudlinuxtech.com/ezoimgfmt/i1.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/install-software-properties-common-ubuntu.png?resize=1024,360&ssl=1&ezimgfmt=ng:webp/ngcb55)

  

2. ##### Step2- Add Deadsnakes Ppa Repository To Install Latest Python 3.9

Open Terminal And Enter The Following Command

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
```

  

![add-deadsnakes-ppa](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/add-deadsnake-ppa-for-latest-python-1024x66.png?resize=1024%2C66&ezimgfmt=rs:640x41/rscb55/ng:webp/ngcb55)

  
  

3. ##### Step3- Update Ubuntu/Kali Repository

```
sudo apt update
```

  

![sudo-apt-update](https://cloudlinuxtech.com/ezoimgfmt/i1.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/sudo-apt-update.png?resize=918%2C282&ezimgfmt=rs:640x197/rscb55/ng:webp/ngcb55)

  
  

4. ##### Step4- Install latest Python 3 (Version 3.9.0)

```
sudo apt install python3.9
```

  

![How-to-install-Python-in-Linux](https://cloudlinuxtech.com/ezoimgfmt/i0.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/how-to-install-python-linux.png?resize=922%2C391&ezimgfmt=rs:640x271/rscb55/ng:webp/ngcb55)

  
  

5. ##### Step5- Check python version

```shell
python --version
```

##### Installing Pip (Only For Linux Or Ubuntu)

By-default _python3-pip_ is not installed in Ubuntu 20.04 and installing it from **apt** will install old pip package. So let's see step by step installation of latest **python3-pip** **version (20.3.3)**. It will be a two-step process, first, we will install **pip 20.0.2** using the apt repository. Then, download and install the latest pip package i.e. 20.3.3 version.

  

1. ##### Step1- Install python3-pip package using apt command

```
sudo apt install python3-pip
```

  

![How-to-install-Python3-pip](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Install-python3-pip-using-apt-1024x425.png?resize=1024%2C425&ezimgfmt=rs:640x266/rscb55/ng:webp/ngcb55)

  
  

2. ##### Step2- Check python3-pip version

  

Here pip version 20.0.2 got installed and we need to **upgrade** it to version 20.3.3. Installing package 3.8 from **apt** will help to meet all dependent packages and libraries which will be required for **pip 20.3.3**. If you will skip this step, you may get dependent modules error.

  
  

![check-latest-pip-version](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/check-pip3-version-1.png?resize=862%2C147&ezimgfmt=rs:640x109/rscb55/ng:webp/ngcb55)

  
  

3. ##### Step3- Install **curl** command first.

  

If curl is already installed your system, you can skip this step. Most of the Ubuntu 20.04 don't have curl installed by default. So use **apt install** command to install it. **Curl** is required to execute _step 4_.

  

```shell
sudo apt install curl
```

  

![install-curl](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Install-curl-package-1.png?resize=883%2C416&ezimgfmt=rs:640x301/rscb55/ng:webp/ngcb55)

  
  

4. ##### Step4- Download pip from **bootstrap.pypa.io** website

Now you need to **download get pip** from bootstrap.pypa.io website using **curl** command as shown in image.

```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

  

![download-pip-script](https://cloudlinuxtech.com/ezoimgfmt/i0.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Download-python3-pip-1024x167.png?resize=1024%2C167&ezimgfmt=rs:640x104/rscb55/ng:webp/ngcb55)

  
  

5. ##### Step5- Upgrade python3-pip version to pip-20.3.3

  

Run **python3.9** command to execute "get-pip.py" package file you downloaded. It will automatically download and install the latest pip in your Ubuntu/Kali Linux.

```shell
sudo python3.9 get-pip.py
```

  

![Install-python3-pip-ubuntu-20.04](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Install-latest-pip-20.3.3-ubuntu-20.04-1024x229.png?resize=1024%2C229&ezimgfmt=rs:640x143/rscb55/ng:webp/ngcb55)

  
  

6. ##### Step6 (optional)- Add pip3.9 directory to PATH.

This can be achieved by editing **/etc/environment** file using your favourite editor. Otherwise, exporting and appending "**PATH**" variable for the local user profile will also do the trick. Make sure you add _~/.local/bin/_ in PATH variable.

```
export PATH=~/.local/bin/:$PATH
```

  

![add-pip-path-variable](https://cloudlinuxtech.com/ezoimgfmt/i0.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/Add-pip-path-variable-2-1024x79.png?resize=1024%2C79&ezimgfmt=rs:640x49/rscb55/ng:webp/ngcb55)

  
  

7. ##### Step7- Check pip version

```shell
pip3.9 --version
```

  

![check-pip3.9-version](https://cloudlinuxtech.com/ezoimgfmt/i2.wp.com/cloudlinuxtech.com/wp-content/uploads/2021/01/check-pip3.9-version.png?resize=1012%2C111&ezimgfmt=rs:640x70/rscb55/ng:webp/ngcb55)

  
  

**Congrats**!! till this point you have installed latest Python 3.9.0 and pip 20.3.3 successfully.

  

#### Install Required Modules

```shell
pip install -r requirements.txt
```

##### For Windows

If You Are On Windows Machine, You Can Just Run `windows.bat` FileTo Start The Program Directly.

You Can Also Do It Manually-

Just Open Powershell Or Command Prompt And Then Type Following Command

```
python -m MailGrab.py
```

##### For Linux

For Linux Users, You Just Have To Type The Same Thing To Terminal.

Just Open Terminal And Type The Following Command

```
python -m MailGrab.py
```

## Usage

MailGrab Is An Easy To Use, User Friendly, Cross Platform And Reliable Tool

After Launching MailGrab Just Input Url And It Will Automatically Do It's

Work.

It Will List All Emails And SubUrls In Terminal. It Will Save Them Also In A Text File For Future

> ## !ProTip

You Can Provide A Huge List Of Urls In A File Named `_inputUrls.txt`

. It Will Automatically Detect The File In Current Directory And Will Harvest From The Emails One By One!

***~~This Is A Sicret Please Dont Tell It To Anyone!~~***

# Attribute

## This Tool Mail Grab Is Made ***By OCEAN OF ANYTHING*** (***Nakshatra Ranjan Saha***)
