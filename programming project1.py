#define a function to convert a string to morse code 
def morse_code(string, morse_dict):
  string = string.upper()  
# convert the string to uppercase to ensure case sensitivity 
  for letter in string:
    if letter in morse_dict.keys():
      print(morse_dict[letter])
    elif letter == " ":
      # print a space 
      print(" ")
    else:
      #print an error message 
      print(f"The {letter} key doesn't exist in the dictionary")


string = input("Enter something to print out to morse code\n")

# define a dictionary for morse code 
morse_dict = {
  'A':'.-', 
  'B':'-...', 
  'C':'-.-.', 
  'D':'-..', 
  'E':'.', 
  'F':'..-.', 
  'G':'--.', 
  'H':'....', 
  'I':'..', 
  'J':'.---', 
  'K':'-.-', 
  'L':'.-..', 
  'M':'--', 
  'N':'-.', 
  'O':'---', 
  'P':'.--.', 
  'Q':'--.-', 
  'R':'.-.', 
  'S':'...', 
  'T':'-', 
  'U':'..-', 
  'V':'...-', 
  'W':'.--', 
  'X':'-..-', 
  'Y':'-.--', 
  'Z':'--..', 
  '1':'.----', 
  '2':'..---', 
  '3':'...--', 
  '4':'....-', 
  '5':'.....', 
  '6':'-....', 
  '7':'--...', 
  '8':'---..', 
  '9':'----.', 
  '0':'-----', 
  ',':'--..--', 
  '.':'.-.-.-', 
  '?':'..--..', 
  '/':'-..-.', 
  '-':'-....-', 
  '(':'-.--.', 
  ')':'-.--.-',
  '!':'-.-.--',
  }

# call the function to convert the user string to morse code 
morse_code(string, morse_dict)  
  