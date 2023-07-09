import socket as soc
s=soc.socket()
s.bind(("",500))
s.listen(1)
c,addr=s.accept()
qns=str('1.which is capital of tamil nadu?')
ans="chennai"
mark=0
c.send(qns.encode())
ans_1=c.recv(1000)
ans1=ans_1.decode()
if(ans==ans1):
        mark+=10
        m=str(mark)
        print("total marks:",mark)
        c.send(m.encode())
               
        
