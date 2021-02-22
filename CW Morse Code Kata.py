# here is basic translator with interactive input
# and a character dictionary, which will take as input keystroked
# dot and dash morse code and return the match letter value  

MORSE_CODE = dict({"  ": " * ",".-": "A","-...": "B","-.-.": "C","-..": "D",".": "E","..-.": "F",
                   "--.": "G","....": "H","..": "I",".---": "J","-.-": "K",".-..": "L",
                   "--": "M","-.": "N","---": "O",".--.": "P","--.-": "Q",".-.": "R",
                   "...": "S","-": "T","..-": "U","...-": "V",".--": "W","-..-": "X",
                   "-.--": "Y","--..": "Z","-----": "0",".----": "1","..---": "2","...--": "3",
                   "....-": "4",".....": "5","-....": "6","--...": "7","---..": "8","----.": "9",
                   ".-.-.-.": ".","--.--": ",","---...": ":","..--..": "?",".----.": "'"})


# Convert the input message string into a list
def Convert(string):
    li = list(string.split(" ")) 
    return li                   

message = input("Enter Morse Code  ") # enter space delimited morse code
parsed = (Convert(message)) # Call "convert" function  and  "convert" morse code "message" into a list >> "parsed".
decode = list() #define the list variable "decode" to which the dict value for each can be appended

for i in parsed: # iterates through "parsed" list of morse code characters
    x = (MORSE_CODE.get(i," ")) # for each i in "parsed" retreives its dictionary value
    decode.append(x) # append values to the list x
    """print (x, end='') # prints x after iteration complete""" #iterates horizontally -- I like the line below better

print ("Decoded Message    ",*decode, sep="") #Print decode without the delimiters (*Val, sep"")



    
    
    
    
    

    


