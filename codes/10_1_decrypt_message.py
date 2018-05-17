alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = int(input('> Please input the Key: '))
msg = input('> Please input a message: ')
msg = msg.lower()

new_msg = ''
for c in msg:
    pos = alphabet.find(c)
    if pos == -1:
        new_msg += c
    else:
        pos = (pos + key) % len(alphabet)
        new_msg += alphabet[pos]

print('The encrypted message is: ', new_msg)

old_msg = ''
for c in new_msg:
    pos = alphabet.find(c)
    if pos == -1:
        old_msg += c
    else:
        pos = (pos - key) % len(alphabet)
        old_msg += alphabet[pos]

print('The encrypted message is: ', old_msg)

