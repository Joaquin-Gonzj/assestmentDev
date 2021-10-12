#import
import requests
import json
from emailSender import email_sender

#connectingAPI
dataSource = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey="
                          "at_kvLn8Ud88dypxp55yslh3FVcAAxA9&domainName=cryptotradexinvest.com/",
                          "outputFormat=JSON")

# #formattedJSON
packageJSON = dataSource.json()

createdDate = json.dumps(packageJSON["WhoisRecord"]['createdDate'], indent=4)
updatedDate = json.dumps(packageJSON["WhoisRecord"]['updatedDate'], indent=4)
expiresDate = json.dumps(packageJSON["WhoisRecord"]['expiresDate'], indent=4)
contactEmail = json.dumps(packageJSON["WhoisRecord"]['contactEmail'], indent=4)
domainName =  "cryptotradexinvest.com"

#conditional
def conditional_inquiry4():
    if domainName != packageJSON["WhoisRecord"]["domainName"]:
        # email sender
        email_sender()
    elif createdDate != packageJSON["WhoisRecord"]["createdDate"]:
        email_sender()
    elif updatedDate != packageJSON["WhoisRecord"]['updatedDate']:
        email_sender()
    elif expiresDate != packageJSON["WhoisRecord"]['expiresDate']:
        email_sender()
    elif contactEmail != packageJSON["WhoisRecord"]['contactEmail']:
        email_sender()

