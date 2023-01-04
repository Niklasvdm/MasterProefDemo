from cryptography.fernet import Fernet







file = open("key.txt","r")
key = file.read().encode("UTF-8")
file.close
print(key)
myFernet = Fernet(key)

URIUnEncrypted = input("Please tell me the url of your request you want to Encrypt:")
URIUnEncrypted = URIUnEncrypted.encode('UTF-8')
URIEncrypted = myFernet.encrypt(URIUnEncrypted)
print("Original String : " , URIUnEncrypted)
print("Encrypted Sting :" , URIEncrypted)


URIDecrypted = myFernet.decrypt(URIEncrypted)
print("Decrypted string:" , URIDecrypted.decode('UTF-8'))