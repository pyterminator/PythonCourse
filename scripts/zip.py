# zip() 

from string import ascii_lowercase, ascii_uppercase, ascii_letters
letters = ascii_uppercase + ascii_lowercase

def Change(letter):
    return ord(letter)

letters = map(Change, letters)
ascii_letters = map(Change, ascii_letters)

my_table = dict(zip(letters, ascii_letters))
 

text = "AzErBayCaN"
 
print(
    text.translate(my_table)
)
print(text.swapcase())