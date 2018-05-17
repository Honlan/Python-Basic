import random

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'

base = alphabet.split(',')
target = base.copy()
random.shuffle(target)

cipher = {}
d_cipher = {}
for i in range(len(base)):
    cipher[base[i]] = target[i]
    d_cipher[target[i]] = base[i]
# d_cipher = {v: k for k, v in cipher.items()}

msg = input('Please input a message: ')
new_msg = ''
for c in msg:
    new_msg = new_msg + cipher.get(c, c)
print('The secret message is: ', new_msg)

plain_msg = ''
for c in new_msg:
    plain_msg = plain_msg + d_cipher.get(c, c)

print('The plain message is: ', plain_msg)



    
