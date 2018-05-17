msg = "Kyv wLIKyvJK uzJKrEtv zE Kyv NFICu, zJ EFK svKNvvE Czwv rEu uvrKy. sLK NyvE z JKrEu zE wIFEK Fw PFL, PvK PFL uFE'K BEFN KyrK z CFMv PFL"
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

for key in range(len(alphabet)):
    old_msg = ''
    for c in msg:
        pos = alphabet.find(c)
        if pos == -1:
            old_msg += c
        else:
            pos = (pos - key) % len(alphabet)
            old_msg += alphabet[pos]
    print('The Key: ', key)
    print('The decrypted message is: ', old_msg)
