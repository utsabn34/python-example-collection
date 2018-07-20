#!/bin/python3

alphabet = 'qwertyuioplkjhgfdsazxcvbnm0987654321' //creating random alphabet list for encryption
key =3
character = input('Enter a character')
position = alphabet.find(character)
newPosition = (position + key) % 26
print(newPosition)
newCharacter = alphabet[newPosition]
