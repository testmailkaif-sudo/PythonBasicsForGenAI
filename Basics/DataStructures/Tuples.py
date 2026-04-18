# Tuple is ordered and unchangble. It is used when data should not be modified
server_ip_port = ('192.168.110.148',7869,7869)
user_credentials = ('Moha3204','Moha*@#547')

#we can access the items in tuble same as we accessed in list
print(server_ip_port[0])
print(user_credentials[-1])
print(user_credentials[0:2])

#unpacking the tuple
username, password = user_credentials
print(username,password,"Tuple is unpacked")


#Tuple Methods
print(server_ip_port.index(7869))
print(server_ip_port.count(7869))