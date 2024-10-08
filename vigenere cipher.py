plaintext = "we are discovered save yourself".lower()
key = "deceptive".lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
numkey = []
encryption =""

#turn the key into it's numbers in the alphabet
for n in key:
    numkey.append(alphabet.find(n))

print(numkey)
input()
counter = 0
for l in plaintext:
#if it's a space, dont increment the counter and continue
    if l == " ":
        continue
#find the cipher letter by adding the key number to the location of the plaintext
    location = alphabet.find(l)
    newlocation = location + numkey[counter]

#loop back to the start of the alphabet if it's going over
    if newlocation >= 26:
        newlocation = newlocation - 26

#add cipher letter to result
    encryption = encryption + alphabet[newlocation]
    counter = counter + 1
    if counter >= len(numkey):
        counter = 0

print(encryption)
