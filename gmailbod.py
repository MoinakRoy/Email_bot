import easyimap as e
password="hdcf48a01"
user="rmainak01@gmail.com"
server=e.connect("imap.gmail.com",user,password)
server.listids()
for i in range(len(server.listids())):
    email=server.mail(server.listids()[i])
    print(email.title)
    print(email.from_addr)
    print(email.body)