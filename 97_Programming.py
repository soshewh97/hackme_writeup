#-*-coding:utf-8-*-
import numpy as np
from pwn import *
r = remote('hackme.inndy.tw', 7707)
print(r.recvuntil("start the game.\n"))
r.sendline("Yes I know")
#print (r.recv())

answer=[]
for i in range(10000):
    c = r.recvuntil("=")[0:-1]
    print(c)
    r.recvline()
    #math = (r.recv(timeout=0.5))
    math_split = c.decode().strip().split(' ')
    if (math_split[1] == "+"):
        #print(math_split)
        answer.append(np.int32(int(math_split[0])+int(math_split[2])))
    elif (math_split[1] == "-"):
        #print(math_split)
        answer.append(np.int32(int(math_split[0])-int(math_split[2])))
    elif (math_split[1] == "*"):
        #print(math_split)
        answer.append(np.int32(int(math_split[0])*int(math_split[2])))
    elif (math_split[1] == "/"):
        #print(math_split)
        answer.append(np.int32(int(math_split[0])/int(math_split[2])))
    #answers = range_math(math_array)
    #print(_answer)
    #try:
_answer = (" ".join("%s"% _id for _id in answer))
r.sendline(_answer)
r.interactive()
r.close()
