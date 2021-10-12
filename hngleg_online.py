#import
import requests
import json
from emailSender import email_sender

#connectingAPI
dataSource = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey="
                          "at_kvLn8Ud88dypxp55yslh3FVcAAxA9&domainName=hngleg.online/",
                          "outputFormat=JSON")

# #formattedJSON
packageJSON = dataSource.json()

createdDate = json.dumps(packageJSON["WhoisRecord"]['registryData'], indent=4)
updatedDate = json.dumps(packageJSON["WhoisRecord"]['registryData'], indent=4)
expiresDate = json.dumps(packageJSON["WhoisRecord"]['registryData'], indent=4)
contactEmail = json.dumps(packageJSON["WhoisRecord"]['contactEmail'], indent=4)
domainName =  "hngleg.online"

#conditional
def conditional_inquiry3():
    if domainName != packageJSON["WhoisRecord"]["domainName"]:
        # email sender
        email_sender()
    elif createdDate != packageJSON["WhoisRecord"]["registryData"]:
        email_sender()
    elif updatedDate != packageJSON["WhoisRecord"]['registryData']:
        email_sender()
    elif expiresDate != packageJSON["WhoisRecord"]['registryData']:
        email_sender()
    elif contactEmail != packageJSON["WhoisRecord"]['contactEmail']:
        email_sender()
