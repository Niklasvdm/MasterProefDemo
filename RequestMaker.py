import requests

def makeRequest(URI):
    response = requests.get(URI)
    returnvalue = response.content
    #response.close()
    return returnvalue
