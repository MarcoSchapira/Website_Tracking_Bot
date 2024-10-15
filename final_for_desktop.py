
from selenium import webdriver
import time

import hashlib
from urllib.request import urlopen, Request

import smtplib


LastQueens6Bed = 0
LastQueens7Bed = 0
LastFrontenac6Bed = 0
LastFrontenac7Bed = 0
LastAxon6Bed = 0
LastAxon7Bed = 0
thequeenshouse = 0

NewQueens6Bed = NewQueens7Bed = 0
NewFrontenac6Bed = NewFrontenac7Bed = 0
NewAxon6Bed = NewAxon7Bed = 0

def SendeMail(websiteName, NumBedrooms):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login("qhousingbot@gmail.com", "jjmumkxfduwekvni") #jjmumkxfduwekvni

        subject = 'House posted on ' + websiteName + ' website'
        body = 'This house has ' + NumBedrooms + ' bedrooms'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail("qhousingbot@gmail.com", '21mjs15@queensu.ca', msg)
        smtp.sendmail("qhousingbot@gmail.com", '20an46@queensu.ca', msg)
        smtp.sendmail("qhousingbot@gmail.com", '20tdm2@queensu.ca', msg)
        smtp.sendmail("qhousingbot@gmail.com", '20cjcj@queensu.ca', msg)

def SendQueenseMail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login("mjschapira@gmail.com", "ypnctwoogfqttcsr") #ypnctwoogfqttcsr

        subject = '184 University'
        body = 'Hi,\n\nI am a Queens University Student and I just saw your property listed on the queens lising service for 184 University street! My friends and I have been constantly monitoring your website for the last month in the hopes of being first to apply. I hope that the house is still avaliable and if so, what are the next steps to finilizing a lease. \nMy student number is 20294325 and my student email is 21mjs15@queensu.ca\n\nThanks,\nMarco Schapira'

        msg = f'Subject: {subject}\n\n{body}' 

        smtp.sendmail("mjschapira@gmail.com", 'community.housing@queensu.ca', msg)#community.housing@queensu.ca


firstRun = True
emailsent = False

while True:

    # start web browser
    browser=webdriver.Firefox()

    #Queens Comunity housing **********************************************
    
    # get source code
    browser.get("https://listingservice.housing.queensu.ca/")
    time.sleep(10)
    html = browser.page_source
    #print(html)
    # close web browser
    browser.close()
    
    #count houses
    NewQueens6Bed =  html.count("<td>6</td>")
    NewQueens7Bed =  html.count("<td>7</td>")
    thequeenshouse = html.count("184 University") + html.count("184 university")

    #print the number of houses
    print("Number of 6 person Queens Comunity Houses: " + str(NewQueens6Bed))
    print("Number of 7 person Queens Comunity Houses: " + str(NewQueens7Bed))
    if(thequeenshouse == 0):
        print("The queens house at 184 University is not posted")

    if (thequeenshouse != 0) & (emailsent == False):
        SendQueenseMail()
        SendeMail("184 UNIVERSITY AVENUE", "6")
        emailsent = True

    #******************************************************
    # Frontinac housing

    #6 bedroom
    url = Request('https://www.frontenacproperty.com/properties/stud/?bedrooms=6&sort=availability&order=ASC',
                headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    strReplace = response.decode('UTF-8')
    NewFrontenac6Bed = strReplace.count("May 1, 2023")

    print("Number of 6 person Frontenac Houses: " + str(NewFrontenac6Bed))

    #7 bedroom
    url = Request('https://www.frontenacproperty.com/properties/stud/?bedrooms=7&sort=availability&order=ASC',
                headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    strReplace = response.decode('UTF-8')
    NewFrontenac7Bed = strReplace.count("May 1, 2023")

    print("Number of 7 person Frontenac Houses: " + str(NewFrontenac7Bed))

    #firstRun = False
    if firstRun == False:
        if NewQueens6Bed > LastQueens6Bed:
            SendeMail("Queens Comunity housing", "6")
        if NewQueens7Bed > LastQueens7Bed:
            SendeMail("Queens Comunity housing", "7")
        if NewFrontenac6Bed > LastFrontenac6Bed:
            SendeMail("Frontenac Housing", "6")
        if NewFrontenac7Bed > LastFrontenac7Bed:
            SendeMail("Frontenac Housing", "7")

    LastQueens6Bed = NewQueens6Bed
    LastQueens7Bed = NewQueens7Bed
    LastFrontenac6Bed = NewFrontenac6Bed
    LastFrontenac7Bed = NewFrontenac7Bed
    
    firstRun = False