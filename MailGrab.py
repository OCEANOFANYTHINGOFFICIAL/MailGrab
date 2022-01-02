# This Program Will Take Input(url) and Will Harvest The Email Addresses From The Website
# This Is The Main File For The Program

# importing required modules. External Modules Used In This Program Can Be Found In The requirements.txt File
import sys
from bs4 import BeautifulSoup as bs
import requests as r
import urllib.parse as up
from collections import deque as dq
import re
from rich.console import Console
from rich.text import Text
import time
import colorama as c
from termcolor import colored
import cursor
import os
import psutil
import platform
import datetime
import warnings
import logging

if __name__ == "__main__":
    """
    Name - MailGrab
    Description - Email Harvester Tool
    Author - OCEAN OF AMNYTHING
    """
    # Configuring Logging System
    FORMAT = "[%(lineno)d]: %(levelname)s - %(message)s"
    logging.basicConfig(
        level=logging.DEBUG, format=FORMAT, datefmt="[%X]", filename="_MailGrabLog.txt", filemode='w', encoding="utf-8"
    )
    log = logging.getLogger()
    log.removeFilter(sys.stderr)
    log.propagate = False
    date = datetime.datetime.now()
    time1 = date.strftime("%H:%M:%S")
    log.info("Starting MailGrab")
    log.info("Srapped Url List By MailGrab A Powerful Email Scraper Tool Made By OCEAN OF ANYTHING")
    log.info("This File Contains The Urls Scrapped From The Url Provided By The User")
    log.info("https://oceanofanythingofficial.github.io")
    log.info("https://github.com/oceanofanythingofficial")
    log.info("https://oceanofanythingg.blogspot.com")
    log.info(f"Date Of Last Scan: {date}")
    log.info(f"Time Of Last Scan: {time1}")

    # Creating Universal Signs
    # Primarry  Sign
    sPrimary = Text("[+]")
    sPrimary.stylize("bold #0275d8")
    log.info("Primary Sign: [+]")
    # Warning Sign
    sWarning = Text("[!]")
    sWarning.stylize("bold #eed202")
    log.info("Warning Sign: [!]")
    # Danger Sign
    sDanger = Text("[!]")
    sDanger.stylize("bold #d9534f")
    log.info("Danger Sign: [!]")
    # Success Sign
    sSuccess = Text("[+]")
    sSuccess.stylize("bold #5fd700")
    log.info("Success Sign: [+]")
    # info Sign
    sInfo = Text("[+]")
    sInfo.stylize("bold #5bc0de")
    log.info("Info Sign: [+]")
    # success Input Sign
    sInput = Text("[?] ")
    sInput.stylize("bold #00ff00")
    log.info("Input Sign: [?]")


    # initializing rich console and coloroma
    console = Console(record=True)
    c.init(autoreset=True)

    # universal Variables
    __author__ = Text("OCEAN OF ANYTHING")
    __author__.stylize("bold yellow")
    __email__ = Text("oceanofanything@gmail.com")
    __email__.stylize("bold white")

    # Check If The User Is Connected To The Internet

    if r.get("https://oceanofanythingofficial.github.io") == None:
        log.error("Program Closing No Internet Connection")
        console.print(sDanger + " You Are Not Connected To The Internet")
        log.error("You Are Not Connected To The Internet")
        console.print(sInfo + " Please Connect To The Internet To Continue Using This Program")
        log.info("Please Connect To The Internet To Continue Using This Program")
        console.print(sInfo + " Press Enter To Exit", end="")
        input('')
        log.info("Press Enter To Exit")
        sys.exit()
    elif r.get("https://oceanofanythingofficial.github.io") != None:
        pass
    else:
        pass

    # Preventing Creation Of __pycache__ Folder
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    sys.dont_write_bytecode = True
    # chexk if exists __pycache__ folder if yes delete it
    if os.path.exists("__pycache__"):
        log.info("__pycache__ Folder Exists")
        log.info("__pycache__ Folder Exists")
        log.info("Deleting __pycache__ Folder")
        os.system("rm -rf __pycache__")
        log.info("__pycache__ Folder Deleted")
        pass
    else:
        pass
    # Functions And Classes
    # Banner
    class BANNER:
        def __init__(self):
            console.print(
                Text(" _______  _______ _________ _        ", "bold green"), end=""
            )
            console.print(Text("                                 ", "bold red"), end="\n")
            console.print(
                Text("(       )(  ___  )\__   __/( \       ", "bold green"), end=""
            )
            console.print(Text("                                 ", "bold red"), end="\n")
            console.print(
                Text("| () () || (   ) |   ) (   | (       ", "bold green"), end=""
            )
            console.print(Text("                                 ", "bold red"), end="\n")
            console.print(
                Text("| || || || (___) |   | |   | |       ", "bold green"), end=""
            )
            console.print(Text("  ________            ___.       ", "bold red"), end="\n")
            console.print(
                Text("| |(_)| ||  ___  |   | |   | |       ", "bold green"), end=""
            )
            console.print(Text(" /  _____/___________ \_ |__     ", "bold red"), end="\n")
            console.print(
                Text("| |   | || (   ) |   | |   | |       ", "bold green"), end=""
            )
            console.print(Text("/   \  __\_  __ \__  \ | __ \    ", "bold red"), end="\n")
            console.print(
                Text("| )   ( || )   ( |___) (___| (____/\ ", "bold green"), end=""
            )
            console.print(Text("\    \_\  \  | \// __ \| \_\ \   ", "bold red"), end="\n")
            console.print(
                Text("|/     \||/     \|\_______/(_______/ ", "bold green"), end=""
            )
            console.print(Text(" \______  /__|  (____  /___  /   ", "bold red"), end="\n")
            console.print(
                Text("                                     ", "bold green"), end=""
            )
            console.print(Text("        \/           \/    \/    ", "bold red"), end="\n")
            console.print(Text("Mail", "bold Green"), end="")
            console.print(Text("Grab", "bold red"), end="")
            console.print(Text(" A Powerful Email Harvester Tool", "bold blue"), end="")
            console.print(Text(" By OCEAN OF ANYTHING", "bold yellow"), end="\n")
            console.print(Text("", "bold red"))
            console.print(Text("", "bold red"))
    def ordered_set(in_list):
        out_list = []
        added = set()
        for val in in_list:
            if not val in added:
                out_list.append(val)
                added.add(val)
        return out_list
    # coloring block
    block = colored("█", "green")
    # Progress Bar
    def progressBar(
        iterable, prefix="", suffix="", decimals=1, length=100, fill=block, printEnd="\r"
    ):
        """
        Call in a loop to create terminal progress bar
        @params:
            iterable    - Required  : iterable object (Iterable)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        cursor.hide()
        total = len(iterable)
        # Progress Bar Printing Function
        def printProgressBar(iteration):
            percent = ("{0:." + str(decimals) + "f}").format(
                100 * (iteration / float(total))
            )
            filledLength = int(length * iteration // total)
            hStick = colored("-", "green")
            bar = fill * filledLength + hStick * (length - filledLength)
            bar2 = Text(bar, style="bold, green")
            stick = colored("|", "green")
            print(f"\r{prefix} {stick}{bar2}{stick} {percent}% {suffix}", end=printEnd)

        # Initial Call
        printProgressBar(0)
        # Update Progress Bar
        for i, item in enumerate(iterable):
            yield item
            printProgressBar(i + 1)
        # Print New Line on Complete
        print("\n")
        cursor.show()

    def MAILGRAB():
        if 1<2:
            # Now Check If The _inputUrls.txt File Is Empty Or Not. If Empty Then Pass The Program
            # if exists _inputUrls.txt file then open it
            f = open("_inputUrls.txt", "r")
            # Read The Content Of The Text File And Append It To An Empty List
            # Creating A Empty String For Store The Urls
            urlListFromTxtFile = []
            # Now Reading The Content Of The Text File And Append It To The List By Replacing \n With ,
            for line in f:
                urlListFromTxtFile.append(line.strip())
            # Closing The File
            f.close()
            # Replacing Blank Lines And Spaces With , From urlListFromTxtFile
            if '' in urlListFromTxtFile:
                urlListFromTxtFile.remove('')
            elif ' ' in urlListFromTxtFile:
                urlListFromTxtFile.remove(' ')
                urlListFromTxtFile.remove('')
            elif '\n' in urlListFromTxtFile:
                urlListFromTxtFile.remove('\n')
                urlListFromTxtFile.remove('')
            elif '\r' in urlListFromTxtFile:
                urlListFromTxtFile.remove('\r')
                urlListFromTxtFile.remove('')
            elif '\t' in urlListFromTxtFile:
                urlListFromTxtFile.remove('\t')
                urlListFromTxtFile.remove('')
            elif '\r\n' in urlListFromTxtFile:
                urlListFromTxtFile.remove('\r\n')
                urlListFromTxtFile.remove('')
            elif '\t\n' in urlListFromTxtFile:
                urlListFromTxtFile.remove('\t\n')
                urlListFromTxtFile.remove('')
            elif "" in urlListFromTxtFile:
                urlListFromTxtFile.remove("")
            else:
                pass
            urlListFromTxtFile = [x.strip() for x in urlListFromTxtFile if x.strip()]
            urlListFromTxtFile = ordered_set(urlListFromTxtFile)
            # Now Printing The Banner
            try:
                BANNER()
            except Exception as e:
                console.print(sDanger + "Error: {}".format(e))
                console.print(sInfo + "Error While Printing The Banner")
                log.warning("Error: {}".format(e))
                log.info("Error While Printing The Banner")
            # Now Take Each Url From The List And Harvest The Email From The Url and The url's subdomains
            # Taking Input From The User For The Depth Of The Search
            console.print(sInput + "Enter The Search Depth For Each Url (Max Is 200): ", end="")
            depthInput = input()
            log.info("User Inputted Depth")
            startTimeg = time.time()
            while True:
                while True:
                    # checking the input is float or not
                    if type(depthInput) == float:
                        console.print(sWarning + " Input Cannot Be A Float!")
                        log.warn("User Entered Invalid Depth")
                        console.print(sInput + "Enter The Search Depth For Each Url (Max Is 200): ", end="")
                        depthInput = input()
                        log.info("User Inputted Depth")
                    else:
                        break
                while True:
                    # checking the input is digit or not, if yes breal while loop
                    if depthInput.isdigit():
                        depthInput = int(depthInput)
                        break
                    # checking the input is digit or not, if not continuing while loop
                    elif not depthInput.isdigit():
                        console.print(sWarning + " Input Must Be A Number!")
                        log.warn("User Entered Invalid Depth")
                        console.print(sInput + "Enter The Search Depth For Each Url (Max Is 200): ", end="")
                        depthInput = input()
                        log.info("User Inputted Depth")
                    # checking the input is digit or not, else continuing while loop
                    else:
                        console.print(sWarning + " Input Must Be A Number!")
                        log.warn("User Entered Invalid Depth")
                        console.print(sInput + "Enter The Search Depth For Each Url (Max Is 200): ", end="")
                        depthInput = input()
                        log.info("User Inputted Depth")
                if depthInput < 0:
                    console.print(sWarning + " Search Depth Cannot Be Negative")
                    log.warn("User Entered Invalid Depth")
                    console.print(sInput + "Enter The Search Depth For Each Url (Max Is 200): ", end="")
                    depthInput = input()
                    log.info("User Inputted Depth")
                    # depth = depthInput
                elif depthInput == 0:
                    console.print(sWarning + " Search Depth Cannot Be Zero")
                    log.warn("User Entered Invalid Depth")
                    console.print(sInput + "Enter The Search Depth For Each Url (Max Is 200): ", end="")
                    depthInput = input()
                    log.info("User Inputted Depth")
                    # depth = depthInput
                elif depthInput > 200:
                    console.print(
                        sWarning
                        + " To Prevent Crashing The Program, Search Depth Cannot Be Greater Than 200"
                    )
                    log.warn("User Entered Invalid Depth")
                    console.print(sInput + "Enter The Search Depth For Each Url (Max Is 200): ", end="")
                    depthInput = input()
                    log.info("User Inputted Depth")
                    # depth = depthInput
                else:
                    depth = depthInput
                    break
                depth = int(depthInput)
                cursor.hide()
            console.print(sSuccess + " Search Depth Is Set To: " + str(depth))
            log.info("Search Depth Set To: " + str(depth))
            scrappedUrls = set()
            emails = set()
            for url in urlListFromTxtFile:
                count = 0
                emailCount = 0
                # Removing white spaces from the url
                url = url.replace(" ", "")
                log.info("Removed White Spaces From: {}".format(url))
                # Now Check If The Url Is Valid Or Not
                if not url.startswith("http"):
                    outputUrl = "http://" + url
                else:
                    outputUrl = url
                # Storing The Url In dq
                urls = dq([outputUrl])
                date = datetime.datetime.now()
                time3 = date.strftime("%H:%M:%S")
                scrappedUrlList = [
                    'Srapped Url List By MailGrab A Powerful Email Scraper Tool Made By OCEAN OF ANYTHING',
                    'This File Contains The Urls Scrapped From The Url Provided By The User',
                    'https://oceanofanythingofficial.github.io',
                    'https://github.com/oceanofanythingofficial',
                    'https://oceanofanythingg.blogspot.com',
                    f'Date Of Last Scan: {date}',
                    f'Time Of Last Scan: {time3}',
                    'Scrapped Urls:'
                    ' '
                ]
                emailList = [
                    'Srapped Url List By MailGrab A Powerful Email Scraper Tool Made By OCEAN OF ANYTHING',
                    'This File Contains The Emails Scrapped From The Url Provided By The User',
                    'https://oceanofanythingofficial.github.io',
                    'https://github.com/oceanofanythingofficial',
                    'https://oceanofanythingg.blogspot.com',
                    f'Date Of Last Scan: {date}',
                    f'Time Of Last Scan: {time3}',
                    'Scrapped Emails:',
                    ' '
                ]
                # Checking The Current Time
                startTime = time.time()
                depthLimit = str(depthInput)
                print("\n\n")
                console.print(sSuccess + " Base Url Is Set To:  " + url)
                log.info("Base Url Set To: " + url)
                startTimeg = time.time()
                while len(urls):
                    # preventing the program from crashing
                    count += 1
                    if count > depth:
                        break
                    url = urls.popleft()
                    scrappedUrls.add(url)
                    # formating the url
                    parts = up.urlsplit(url)
                    baseUrl = "{}://{}".format(parts.scheme, parts.netloc)
                    # Formating The Subdomain And Displaying It
                    path = url[: url.rfind("/") + 1] if "/" in parts.path else url
                    bn = Text(f"[{count}]")
                    bn.stylize("bold #5bc0de")
                    pText = Text(" Processing: ")
                    pText.stylize("bold #d700d7")
                    cUrl = Text(url)
                    cUrl.stylize("bold #0087d7")
                    console.print(bn + pText + cUrl)
                    # getting the html code from the url
                    try:
                        response = r.get(url)
                    # Error Handling
                    except r.exceptions.HTTPError as e:
                        console.print(sDanger + " HTTP Error: {}".format(e))
                        log.error("HTTP Error: {}".format(e))
                        log.exception("HTTP Error: {}".format(e))
                        eUrl = Text(url)
                        eUrl.stylize("bold #d75f00")
                        console.print(sInfo + " Skipping Url: {}".format(eUrl))
                        log.info("Skipping Url: {}".format(eUrl))
                        console
                        continue
                    except r.exceptions.ConnectionError as e:
                        console.print(sDanger + " Connection Error: {}".format(e))
                        log.error("Connection Error: {}".format(e))
                        log.exception("Connection Error: {}".format(e))
                        eUrl = Text(url)
                        eUrl.stylize("bold #d75f00")
                        console.print(sInfo + " Skipping Url: {}".format(eUrl))
                        log.info("Skipping Url: {}".format(eUrl))
                        continue
                    except r.exceptions.Timeout as e:
                        console.print(sDanger + " Timeout Error: {}".format(e))
                        log.error("Timeout Error: {}".format(e))
                        log.exception("Timeout Error: {}".format(e))
                        eUrl = Text(url)
                        eUrl.stylize("bold #d75f00")
                        console.print(sInfo + " Skipping Url: {}".format(eUrl))
                        log.info("Skipping Url: {}".format(eUrl))
                        continue
                    except r.exceptions.TooManyRedirects as e:
                        console.print(sDanger + " Too Many Redirects: {}".format(e))
                        log.error("Too Many Redirects: {}".format(e))
                        log.exception("Too Many Redirects: {}".format(e))
                        eUrl = Text(url)
                        eUrl.stylize("bold #d75f00")
                        console.print(sInfo + " Skipping Url: {}".format(eUrl))
                        log.info("Skipping Url: {}".format(eUrl))
                        continue
                    except r.exceptions.RequestException as e:
                        console.print(sDanger + " Request Exception: {}".format(e))
                        log.error("Request Exception: {}".format(e))
                        log.exception("Request Exception: {}".format(e))
                        eUrl = Text(url)
                        eUrl.stylize("bold #d75f00")
                        console.print(sInfo + " Skipping Url: {}".format(eUrl))
                        log.info("Skipping Url: {}".format(eUrl))
                        continue
                    except Exception as e:
                        console.print(sDanger + " Exception: {}".format(e))
                        log.error("Exception: {}".format(e))
                        log.exception("Exception: {}".format(e))
                        eUrl = Text(url)
                        eUrl.stylize("bold #d75f00")
                        console.print(sInfo + " Skipping Url: {}".format(eUrl))
                        log.info("Skipping Url: {}".format(eUrl))
                        continue
                    # finding the emails in the html code
                    newEmails = set(
                        re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
                    )
                    emails.update(newEmails)
                    soup = bs(response.text, features="lxml")
                    # finding the urls in the html code
                    
                    for anchor in soup.find_all("a"):
                        link = anchor.attrs["href"] if "href" in anchor.attrs else ""
                        if link.startswith("/"):
                            link = baseUrl + link
                        elif not link.startswith("http"):
                            link = path + link
                        if not link in scrappedUrls:
                            urls.append(link)
            print("\n\n\n")
            #  Now Showing The Time Taken To Collect Emails And Urls
            try:
                console.print(
                    sSuccess + " Time Taken To Collect Emails: {} MiliSeconds".format(time.time() - startTimeg)
                )
                log.info("Time Taken To Collect Emails: {}".format(time.time() - startTimeg))
                console.print(
                    sSuccess + " Time Taken To Collect Sub Urls: {} MiliSeconds".format(time.time() - startTimeg)
                )
                log.info("Time Taken To Collect Sub Urls: {}".format(time.time() - startTimeg))
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The Time Taken\n")
                log.info("An Error Ocurred While Printing The Time Taken\n")
            # appending the emails to a list
        for mail in emails:
            emailList.append(mail)
        # appending the urls to a list
        for linkList in scrappedUrls:
            scrappedUrlList.append(linkList)
            try:
                print(" ")
                print(" ")
                while len(emails):
                    emailCount += 1
                    ben = Text(f"[{emailCount}]")
                    ben.stylize("bold #5fd700")
                    cEmails = Text(emails.pop())
                    cEmails.stylize("bold #a8a8a8")
                    console.print(ben + "Email: " + cEmails)
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The Emails")
                log.info("An Error Ocurred While Printing The Emails")

            # Saving Emails In A Text File
            try:
                items = list(range(0, 100))
                console.print(sInfo + "Saving Scrapped Emails In A Text File(_emails.txt)\n")
                for item in progressBar(items, prefix="Progress:", suffix="Complete", length=90):
                    with open("_emails.txt", "w") as f:
                        for item in emailList:
                            f.write("%s\n" % item)
                    f.close()
                time.sleep(0.1)
                console.print(sSuccess + " Scrapped Emails Are Successfully Saved!\n\n")
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Saving The Emails")
                log.info("An Error Ocurred While Saving The Emails")

            # Saving Scrapped Urls In A Text File
            try:
                items = list(range(0, 100))
                console.print(sInfo + "Saving Scrapped Urls In A Text File(_scrappedUrls.txt)\n")
                for item in progressBar(items, prefix="Progress:", suffix="Complete", length=90):
                    with open("_scrappedUrls.txt", "w") as k:
                        for item in scrappedUrlList:
                            k.write("%s\n" % item)
                    k.close()
                time.sleep(0.1)
                console.print(sSuccess + " Scrapped Urls Are Successfully Saved!\n\n")
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Saving The Urls")
                log.info("An Error Ocurred While Saving The Urls")

            # Now Showing How Many Emails And Urls Are Collected
            try:
                console.print(sSuccess + " Number Of Scrapped Emails: {}".format(emailCount))
                log.info("Number Of Scrapped Emails: {}".format(emailCount))
                console.print(sSuccess + " Number Of Scrapped Urls: {}".format(len(scrappedUrlList)))
                log.info("Number Of Scrapped Urls: {}".format(len(scrappedUrlList)))
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The Emails And Urls")
                log.info("An Error Ocurred While Printing The Emails And Urls")
            #  Now Showing The Time Taken To Collect Emails And Urls
            try:
                console.print(
                    sSuccess + " Time Taken To Collect Emails: {} MiliSeconds".format(time.time() - startTime)
                )
                log.info("Time Taken To Collect Emails: {}".format(time.time() - startTime))
                console.print(
                    sSuccess + " Time Taken To Collect Sub Urls: {} MiliSeconds".format(time.time() - startTime)
                )
                log.info("Time Taken To Collect Sub Urls: {}".format(time.time() - startTime))
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The Time Taken\n")
                log.info("An Error Ocurred While Printing The Time Taken\n")
            # showing How Much system resource is using
            try:
                console.print(sSuccess + " Current Usage Of System Resource:")
                log.info("Current Usage Of System Resource:")
                console.print(sSuccess + " CPU: {}%".format(psutil.cpu_percent()))
                log.info("CPU: {}%".format(psutil.cpu_percent()))
                console.print(sSuccess + " RAM: {}%".format(psutil.virtual_memory()[2]))
                log.info("RAM: {}%".format(psutil.virtual_memory()[2]))
                console.print(sSuccess + " Disk: {}%".format(psutil.disk_usage("/")[3]))
                log.info("Disk: {}%".format(psutil.disk_usage("/")[3]))
                console.print(sSuccess + " Network: {}%".format(psutil.net_io_counters()[0]))
                log.info("Network: {}%".format(psutil.net_io_counters()[0]))
                console.print(sSuccess + " Network Speed: {} kbps".format(psutil.net_io_counters()[1]))
                log.info("Network Speed: {} kbps".format(psutil.net_io_counters()[1]))
                
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The System Resource Used By The Program\n")
                log.info("An Error Ocurred While Printing The System Resource Used By The Program\n")
            # Showing The os Information
            try:
                console.print(sSuccess + " OS Information: {}".format(platform.platform()))
                log.info("OS Information: {}".format(platform.platform()))
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The OS Information\n")
                log.info("An Error Ocurred While Printing The OS Information\n")
            # showing the name of the os
            try:
                console.print(sSuccess + " OS Name: {}".format(platform.system()))
                log.info("OS Name: {}".format(platform.system()))
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The OS Name\n")
                log.info("An Error Ocurred While Printing The OS Name\n")
            # showing the Current Date And Time in a formal way
            try:
                console.print(sSuccess + " Current Date And Time: {}".format(datetime.datetime.now()))
                log.info("Current Date And Time: {}".format(time.ctime()))
            except Exception as e:
                console.print(sDanger + " Error: {}".format(e))
                log.error("Error: {}".format(e))
                console.print(sInfo + " An Error Ocurred While Printing The Current Date And Time\n")
                log.info("An Error Ocurred While Printing The Current Date And Time\n")

            console.print(sSuccess + " All Scrapped Emails And Urls Are Saved In _emails.txt And _scrappedUrls.txt\n")
            log.info("All Scrapped Emails And Urls Are Saved In _emails.txt And _scrappedUrls.txt\n")

            console.print(sSuccess + " Thanks For Using MailGrab!")
            console.print(sSuccess + " Made By: " + __author__)
            console.print(sInfo + " If You Have Any Suggestion Or Bug Please Contact Me At: " + __email__)
            cursor.show()
            console.print(sInfo + " Press Any Key To Exit", end="")
            input()
            log.info("Thanks For Using MailGrab!")
            log.info("Program Ended Successfully")
            log.info("----------------------------------------------------------------------------------------------------------------------")
            sys.exit()
        else:
            pass

    # checking if user provide a text file containing bunch of urls, if not pass the program
    # Checking if _inputUrls is a Empty File
    if os.path.isfile("_inputUrls.txt") and os.path.getsize("_inputUrls.txt") > 0:
        MAILGRAB()
    else:
        pass
    # this code will try to get the emails from the url
    count = 0
    emailCount = 0
    try:
        # Showing Banner
        BANNER()
        log.info("Banner Printed")
        # taking url input as a string from user
        console.print(sInput + "Enter The Url To Be Scanned: ", end="")
        inputUserUrl = str(input())
        log.info("User Inputted Url")
        # Removing White Spaces From The URL
        inputUserUrl = inputUserUrl.replace(" ", "")
        log.info("Removed White Spaces From Url")
        # checking the user input is a valid url or not. if not then formatting the string as url

        while True:
            if inputUserUrl == " ":
                console.print(sWarning + " Please Enter A Valid Url")
                log.warn("User Entered Invalid Url")
                console.print(sInput + "Enter The Url To Be Scanned: ", end="")
                inputUserUrl = str(input())
                log.info("User Inputted Url")
            elif inputUserUrl == "":
                console.print(sWarning + " Url Cannot Be Blank")
                log.warn("User Entered Invalid Url")
                console.print(sInput + "Enter The Url To Be Scanned: ", end="")
                inputUserUrl = str(input())
                log.info("User Inputted Url")
            elif " " in inputUserUrl:
                console.print(sWarning + " You Cannot Use White Spaces As/In Url")
                log.warn("User Entered Invalid Url")
                console.print(sInput + "Enter The Url To Be Scanned: ", end="")
                inputUserUrl = str(input())
                log.info("User Inputted Url")
            else:
                inputUserUrl = inputUserUrl.replace(" ", "")
                break
        if not inputUserUrl.startswith("http"):
            userUrl = "http://" + inputUserUrl
        else:
            userUrl = inputUserUrl
        
        # Taking Input From The User For The Depth Of The Search
        console.print(sInput + "Enter The Depth Of The Search: ", end="")
        depthInput = input()
        log.info("User Inputted Depth")
        # checking the input is int or not. if not then taking the input again and again continously in loop until the input is int
        while True:
            while True:
                # checking the input is float or not
                if type(depthInput) == float:
                    console.print(sWarning + " Input Cannot Be A Float!")
                    log.warn("User Entered Invalid Depth")
                    console.print(sInput + "Enter The Depth Of The Search (Max Is 500): ", end="")
                    depthInput = input()
                    log.info("User Inputted Depth")
                else:
                    break
            while True:
                # checking the input is digit or not, if yes breal while loop
                if depthInput.isdigit():
                    depthInput = int(depthInput)
                    break
                # checking the input is digit or not, if not continuing while loop
                elif not depthInput.isdigit():
                    console.print(sWarning + " Input Must Be A Number!")
                    log.warn("User Entered Invalid Depth")
                    console.print(sInput + "Enter The Depth Of The Search (Max Is 500): ", end="")
                    depthInput = input()
                    log.info("User Inputted Depth")
                # checking the input is digit or not, else continuing while loop
                else:
                    console.print(sWarning + " Input Must Be A Number!")
                    log.warn("User Entered Invalid Depth")
                    console.print(sInput + "Enter The Depth Of The Search (Max Is 500): ", end="")
                    depthInput = input()
                    log.info("User Inputted Depth")
            if depthInput < 0:
                console.print(sWarning + " Search Depth Cannot Be Negative")
                log.warn("User Entered Invalid Depth")
                console.print(sInput + "Enter The Depth Of The Search (Max Is 500): ", end="")
                depthInput = input()
                log.info("User Inputted Depth")
                # depth = depthInput
            elif depthInput == 0:
                console.print(sWarning + " Search Depth Cannot Be Zero")
                log.warn("User Entered Invalid Depth")
                console.print(sInput + "Enter The Depth Of The Search (Max Is 500): ", end="")
                depthInput = input()
                log.info("User Inputted Depth")
                # depth = depthInput
            elif depthInput > 500:
                console.print(
                    sWarning
                    + " To Prevent Crashing The Program, Search Depth Cannot Be Greater Than 500"
                )
                log.warn("User Entered Invalid Depth")
                console.print(sInput + "Enter The Depth Of The Search (Max Is 500): ", end="")
                depthInput = input()
                log.info("User Inputted Depth")
                # depth = depthInput
            else:
                depth = depthInput
                break
            depth = int(depthInput)
        # giving the urls to deque
        urls = dq([userUrl])
        # storing the urls and emails in sets
        scrappedUrls = set()
        emails = set()
        date = datetime.datetime.now()
        time2 = date.strftime("%H:%M:%S")
        scrappedUrlList = [
            'Srapped Url List By MailGrab A Powerful Email Scraper Tool Made By OCEAN OF ANYTHING',
            'This File Contains The Urls Scrapped From The Url Provided By The User',
            'https://oceanofanythingofficial.github.io',
            'https://github.com/oceanofanythingofficial',
            'https://oceanofanythingg.blogspot.com',
            f'Date Of Last Scan: {date}',
            f'Time Of Last Scan: {time2}',
            'Scrapped Urls:'
            ' '
        ]
        emailList = [
            'Srapped Url List By MailGrab A Powerful Email Scraper Tool Made By OCEAN OF ANYTHING',
            'This File Contains The Emails Scrapped From The Url Provided By The User',
            'https://oceanofanythingofficial.github.io',
            'https://github.com/oceanofanythingofficial',
            'https://oceanofanythingg.blogspot.com',
            f'Date Of Last Scan: {date}',
            f'Time Of Last Scan: {time2}',
            'Scrapped Emails:',
            ' '
        ]
        os.system("cls")
        log.info("Cleared The Screen")
        BANNER()
        # Checking The Current Time
        startTime = time.time()
        depthLimit = str(depthInput)
        console.print(sSuccess + " Base Url Is Set To:  " + userUrl)
        log.info("Base Url Set To: " + userUrl)
        console.print(sSuccess + " Search Depth Is Set To: " + depthLimit)
        log.info("Search Depth Set To: " + depthLimit)
        console.print("\n")

        while len(urls):
            # preventing the program from crashing
            count += 1
            if count > depth:
                break
            url = urls.popleft()
            scrappedUrls.add(url)
            # formating the url
            parts = up.urlsplit(url)
            baseUrl = "{}://{}".format(parts.scheme, parts.netloc)
            # Formating The Subdomain And Displaying It
            path = url[: url.rfind("/") + 1] if "/" in parts.path else url
            bn = Text(f"[{count}]")
            bn.stylize("bold #5bc0de")
            pText = Text(" Processing: ")
            pText.stylize("bold #d700d7")
            cUrl = Text(url)
            cUrl.stylize("bold #0087d7")
            console.print(bn + pText + cUrl)
            # getting the html code from the url
            try:
                response = r.get(url)
            # Error Handling
            except r.exceptions.HTTPError as e:
                console.print(sDanger + " HTTP Error: {}".format(e))
                log.error("HTTP Error: {}".format(e))
                log.exception("HTTP Error: {}".format(e))
                eUrl = Text(url)
                eUrl.stylize("bold #d75f00")
                console.print(sInfo + " Skipping Url: {}".format(eUrl))
                log.info("Skipping Url: {}".format(eUrl))
                console
                continue
            except r.exceptions.ConnectionError as e:
                console.print(sDanger + " Connection Error: {}".format(e))
                log.error("Connection Error: {}".format(e))
                log.exception("Connection Error: {}".format(e))
                eUrl = Text(url)
                eUrl.stylize("bold #d75f00")
                console.print(sInfo + " Skipping Url: {}".format(eUrl))
                log.info("Skipping Url: {}".format(eUrl))
                continue
            except r.exceptions.Timeout as e:
                console.print(sDanger + " Timeout Error: {}".format(e))
                log.error("Timeout Error: {}".format(e))
                log.exception("Timeout Error: {}".format(e))
                eUrl = Text(url)
                eUrl.stylize("bold #d75f00")
                console.print(sInfo + " Skipping Url: {}".format(eUrl))
                log.info("Skipping Url: {}".format(eUrl))
                continue
            except r.exceptions.TooManyRedirects as e:
                console.print(sDanger + " Too Many Redirects: {}".format(e))
                log.error("Too Many Redirects: {}".format(e))
                log.exception("Too Many Redirects: {}".format(e))
                eUrl = Text(url)
                eUrl.stylize("bold #d75f00")
                console.print(sInfo + " Skipping Url: {}".format(eUrl))
                log.info("Skipping Url: {}".format(eUrl))
                continue
            except r.exceptions.RequestException as e:
                console.print(sDanger + " Request Exception: {}".format(e))
                log.error("Request Exception: {}".format(e))
                log.exception("Request Exception: {}".format(e))
                eUrl = Text(url)
                eUrl.stylize("bold #d75f00")
                console.print(sInfo + " Skipping Url: {}".format(eUrl))
                log.info("Skipping Url: {}".format(eUrl))
                continue
            except Exception as e:
                console.print(sDanger + " Exception: {}".format(e))
                log.error("Exception: {}".format(e))
                log.exception("Exception: {}".format(e))
                eUrl = Text(url)
                eUrl.stylize("bold #d75f00")
                console.print(sInfo + " Skipping Url: {}".format(eUrl))
                log.info("Skipping Url: {}".format(eUrl))
                continue
            # finding the emails in the html code
            newEmails = set(
                re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
            )
            emails.update(newEmails)
            soup = bs(response.text, features="lxml")
            # finding the urls in the html code
            for anchor in soup.find_all("a"):
                link = anchor.attrs["href"] if "href" in anchor.attrs else ""
                if link.startswith("/"):
                    link = baseUrl + link
                elif not link.startswith("http"):
                    link = path + link
                if not link in scrappedUrls:
                    urls.append(link)

    except KeyboardInterrupt:
        console.print(sDanger + " Closing! Because User Interrupted The Program")
        log.error("Closing! Because User Interrupted The Program")
        console.print(sInfo + " Keyboard Interrupt Detected")
        log.info("Keyboard Interrupt Detected")
    # appending the emails to a list
    for mail in emails:
        emailList.append(mail)

    # appending the urls to a list
    for linkList in scrappedUrls:
        scrappedUrlList.append(linkList)
    # printing the extracted emails
    try:
        print(" ")
        print(" ")
        while len(emails):
            emailCount += 1
            ben = Text(f"[{emailCount}]")
            ben.stylize("bold #5fd700")
            cEmails = Text(emails.pop())
            cEmails.stylize("bold #a8a8a8")
            console.print(ben + "Email: " + cEmails)
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Printing The Emails")
        log.info("An Error Ocurred While Printing The Emails")

    # Saving Emails In A Text File
    try:
        items = list(range(0, 100))
        console.print(sInfo + "Saving Scrapped Emails In A Text File(_emails.txt)\n")
        for item in progressBar(items, prefix="Progress:", suffix="Complete", length=90):
            with open("_emails.txt", "w") as f:
                for item in emailList:
                    f.write("%s\n" % item)
            f.close()
        time.sleep(0.1)
        console.print(sSuccess + " Scrapped Emails Are Successfully Saved!\n\n")
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Saving The Emails")
        log.info("An Error Ocurred While Saving The Emails")

    # Saving Scrapped Urls In A Text File
    try:
        items = list(range(0, 100))
        console.print(sInfo + "Saving Scrapped Urls In A Text File(_scrappedUrls.txt)\n")
        for item in progressBar(items, prefix="Progress:", suffix="Complete", length=90):
            with open("_scrappedUrls.txt", "w") as k:
                for item in scrappedUrlList:
                    k.write("%s\n" % item)
            k.close()
        time.sleep(0.1)
        console.print(sSuccess + " Scrapped Urls Are Successfully Saved!\n\n")
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Saving The Urls")
        log.info("An Error Ocurred While Saving The Urls")

    # Now Showing How Many Emails And Urls Are Collected
    try:
        console.print(sSuccess + " Number Of Scrapped Emails: {}".format(emailCount))
        log.info("Number Of Scrapped Emails: {}".format(emailCount))
        console.print(sSuccess + " Number Of Scrapped Urls: {}".format(len(scrappedUrlList)))
        log.info("Number Of Scrapped Urls: {}".format(len(scrappedUrlList)))
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Printing The Emails And Urls")
        log.info("An Error Ocurred While Printing The Emails And Urls")
    #  Now Showing The Time Taken To Collect Emails And Urls
    try:
        console.print(
            sSuccess + " Time Taken To Collect Emails: {} MiliSeconds".format(time.time() - startTime)
        )
        log.info("Time Taken To Collect Emails: {}".format(time.time() - startTime))
        console.print(
            sSuccess + " Time Taken To Collect Sub Urls: {} MiliSeconds".format(time.time() - startTime)
        )
        log.info("Time Taken To Collect Sub Urls: {}".format(time.time() - startTime))
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Printing The Time Taken\n")
        log.info("An Error Ocurred While Printing The Time Taken\n")
    # showing How Much system resource is using
    try:
        console.print(sSuccess + " Current Usage Of System Resource:")
        log.info("Current Usage Of System Resource:")
        console.print(sSuccess + " CPU: {}%".format(psutil.cpu_percent()))
        log.info("CPU: {}%".format(psutil.cpu_percent()))
        console.print(sSuccess + " RAM: {}%".format(psutil.virtual_memory()[2]))
        log.info("RAM: {}%".format(psutil.virtual_memory()[2]))
        console.print(sSuccess + " Disk: {}%".format(psutil.disk_usage("/")[3]))
        log.info("Disk: {}%".format(psutil.disk_usage("/")[3]))
        console.print(sSuccess + " Network: {}%".format(psutil.net_io_counters()[0]))
        log.info("Network: {}%".format(psutil.net_io_counters()[0]))
        console.print(sSuccess + " Network Speed: {} kbps".format(psutil.net_io_counters()[1]))
        log.info("Network Speed: {} kbps".format(psutil.net_io_counters()[1]))
        
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Printing The System Resource Used By The Program\n")
        log.info("An Error Ocurred While Printing The System Resource Used By The Program\n")
    # Showing The os Information
    try:
        console.print(sSuccess + " OS Information: {}".format(platform.platform()))
        log.info("OS Information: {}".format(platform.platform()))
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Printing The OS Information\n")
        log.info("An Error Ocurred While Printing The OS Information\n")
    # showing the name of the os
    try:
        console.print(sSuccess + " OS Name: {}".format(platform.system()))
        log.info("OS Name: {}".format(platform.system()))
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Printing The OS Name\n")
        log.info("An Error Ocurred While Printing The OS Name\n")
    # showing the Current Date And Time in a formal way
    try:
        console.print(sSuccess + " Current Date And Time: {}".format(datetime.datetime.now()))
        log.info("Current Date And Time: {}".format(time.ctime()))
    except Exception as e:
        console.print(sDanger + " Error: {}".format(e))
        log.error("Error: {}".format(e))
        console.print(sInfo + " An Error Ocurred While Printing The Current Date And Time\n")
        log.info("An Error Ocurred While Printing The Current Date And Time\n")

    console.print(sSuccess + " All Scrapped Emails And Urls Are Saved In _emails.txt And _scrappedUrls.txt\n")
    log.info("All Scrapped Emails And Urls Are Saved In _emails.txt And _scrappedUrls.txt\n")
    console.print(sSuccess + " Thanks For Using MailGrab!")
    console.print(sSuccess + " Made By: " + __author__)
    console.print(sInfo + " If You Have Any Suggestion Or Bug Please Contact Me At: " + __email__)
    console.print(sInfo + " Press Any Key To Exit", end="")
    input()
    log.info("Thanks For Using MailGrab!")
    log.info("Program Ended Successfully")
    log.info("----------------------------------------------------------------------------------------------------------------------")
    sys.exit()