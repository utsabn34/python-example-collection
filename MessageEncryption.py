#!/bin/python3

alphabet = 'qwertyuioplkjhgfdsazxcvbnm0987654321' //creating random alphabet list for encryption
newMessage =''
message = input('Enter a message to encrypt: ')
key = int(input('Enter a key to encrypt message: '))
for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 36
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
   else:
    newMessage += character
  
print ('Your encrypted message is: ', newMessage)
