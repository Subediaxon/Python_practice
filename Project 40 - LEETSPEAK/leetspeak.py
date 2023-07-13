from random import randrange

try:
    import paperclip
except:
    pass

def main():
    print('''L3375P34]< (leetspeek)
    By Al Sweigart al@inventwithpython.com
    Enter your leet message:''')
    usr_input = input('> ')
    print()
    englishToLeetspeak(usr_input)
    
    try:
        # Trying to use pyperclip will raise a NameError exception if
        # it wasn't imported:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass  # Do nothing if pyperclip wasn't installed.



def englishToLeetspeak(message):
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    
    for letter in message:
        letter = letter.lower()
        charmapping_key = charMapping.keys()

        if (letter in charmapping_key):
            
            length=len(charMapping.get(letter))
            if (length > 1 ):
                rand = randrange(0, length-1)
                letter = charMapping[letter][rand]
                print(letter, end="")
            else :
                letter = charMapping[letter][0]
                print(letter, end="")
        else:
            if ( letter == " "):
                print(letter, end=" ")
            else:
                print(letter, end="")
                
main()
