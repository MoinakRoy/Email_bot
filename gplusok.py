import easyimap as e
def gmail(user,password):
    server=e.connect("imap.gmail.com",user,password)
    server.listids()
    for i in range(len(server.listids())):
        email=server.mail(server.listids()[i])
        print(email.title)
        print(email.from_addr)
        print(email.body)

def outlook(user,password):
    server=e.connect("imap.outlook.com",user,password)
    server.listids()
    for i in range(len(server.listids())):
        email=server.mail(server.listids()[i])
        print("Subject",email.title)
        print("From",email.from_addr)
        print("Body",email.body)

print("select 1 for gmail, 2 for outlook")
x=input("input: ")
print("enter id and password")
id=input("id: ")
p=input("password: ")




if x=='1':
    gmail(id,p)
elif x=='2':
    outlook(id,p)