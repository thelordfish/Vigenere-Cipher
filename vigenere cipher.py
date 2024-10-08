plaintext = "Hello World".lower()
key = "Ollie".lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
numkey = []
encryption =""
for n in key:
    numkey.append(alphabet.find(n))

print(numkey)
input()
counter = 0
for l in plaintext:
    if l == " ":
        encryption = encryption + " "
        continue
    location = alphabet.find(l)
    newlocation = location + numkey[counter]
    if newlocation >= 26:
        newlocation = newlocation - 26
    encryption = encryption + alphabet[newlocation]
    counter = counter + 1
    if counter >= len(numkey):
        counter = 0

print(encryption)
