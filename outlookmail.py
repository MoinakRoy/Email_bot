import easyimap as e
password="hdud34a01"
user="rmainak01@outlook.com"
server=e.connect("imap.outlook.com",user,password)
server.listids()
for i in range(len(server.listids())):
    email=server.mail(server.listids()[i])
    print(email.title)
    print(email.from_addr)
    print(email.body)