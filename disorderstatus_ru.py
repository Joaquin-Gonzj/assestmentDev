#import
import requests
import json
from emailSender import email_sender

#connectingAPI
dataSource = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey="
                          "at_kvLn8Ud88dypxp55yslh3FVcAAxA9&domainName=disorderstatus.ru/",
                          "outputFormat=JSON")

# #formattedJSON
packageJSON = dataSource.json()

createdDate = json.dumps(packageJSON["WhoisRecord"]['audit'], indent=4)
updatedDate = json.dumps(packageJSON["WhoisRecord"]['audit'], indent=4)
#expiresDate = json.dumps(packageJSON["WhoisRecord"]['registryData'], indent=4)
#contactEmail = json.dumps(packageJSON["WhoisRecord"]['contactEmail'], indent=4)
domainName =  "disorderstatus.ru"

#conditional
def conditional_inquiry2():
    if domainName != packageJSON["WhoisRecord"]["domainName"]:
        # email sender
        email_sender()
    elif createdDate != packageJSON["WhoisRecord"]["audit"]:
        email_sender()
    elif updatedDate != packageJSON["WhoisRecord"]['audit']:
        email_sender()
    # elif expiresDate != packageJSON["WhoisRecord"]['expiresDate']:
    #     email_sender()
    # # elif expiresDate != packageJSON["WhoisRecord"]['expiresDate']:
    #     email_sender()

