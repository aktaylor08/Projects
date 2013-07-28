
vowels = ['a', 'e', 'i','o','u']

string = raw_input('Give me a string please: ').strip()
for word in string.split():
    if word[0] in vowels:
        print word + 'way' , 
    else:
        print word[1:] + word[0] + 'ay',


