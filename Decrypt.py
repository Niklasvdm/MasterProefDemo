from cryptography.fernet import Fernet
from RequestMaker import makeRequest






file = open("key.txt","r")
key = file.read().encode("UTF-8")
file.close
print(key)
myFernet = Fernet(key)

URIEncrypted = input("Please tell me the url of your request you want to Decrypt:")
URIEncrypted = URIEncrypted.encode('UTF-8')
URIDecrypted = myFernet.decrypt(URIEncrypted)
URIDecrypted = URIDecrypted.decode('UTF-8')
print("Decrypted string:" ,URIDecrypted )
print(makeRequest(URIDecrypted))

