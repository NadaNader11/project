# define the dictionary 
def morse_code(string, switch_morse_dict):
#split inputs into words 
 words = string.split(' ')
 for word in words:
  letters = word.split(' ')
  for letter in letters:
    if letter in switch_morse_dict.keys():
#print the letter 
      print(switch_morse_dict[letter])
    elif letter == " ":
# print a space
      print(" ") 
    else: 
      print(f"The {letter} key doesn't exist in the dictionary")
      return #Stop execution if unsupported character is entered


string = input("Enter something to print out to text\n")
 
#Rest of the code remains unchanged 

switch_morse_dict = {
              
'.-' : 'A',
'-...' : 'B',
'-.-.' : 'C',
'-..' : 'D',
'.' : 'E',
'..-.' : 'F',
'--.' : 'G',
'....' : 'H',
'..' : 'I',
'.---' : 'J',
'-.-' : 'K',
'.-..' : 'L',
'--' : 'M',
'-.' : 'N',
'---' : 'O',
'.--.' : 'P',
'--.-' : 'Q',
'.-.' : 'R',
'...' : 'S',
'-' : 'T',
'..-' : 'U',
'...-' : 'V',
'.--' : 'W',
'-..-' : 'X',
'-.--' : 'Y',
'--..' : 'Z',
'.----' : '1',
'..---' : '2',
'...--' : '3',
'....-' : '4',
'.....' : '5',
'-....' : '6',
'--...' : '7',
'---..' : '8',
'----.' : '9',
'-----' : '0',
'--..--' : ', ',
'.-.-.-' : '.',
'..--..' : '?',
'-..-.' : '/',
'-....-' : '-',
'-.--.' : '(',
'-.--.-' : ')',
'-.-.--' : '!'
}
# call the function to convert the morse code to a string
morse_code(string, switch_morse_dict)
