
string = raw_input('Give me a string please: ').strip()
str_r = ''
for i in xrange(len(string)-1 , -1, -1):
    str_r += string[i]
print str_r
