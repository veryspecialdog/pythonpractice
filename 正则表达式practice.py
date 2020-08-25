import re
str = 'The white dog wears a black hat.'
pttn = r'The (white|black) dog wears a (white|black) hat.'
re.findall(pttn,str)

repl = r'The \2 dog wears a \1 hat.'
print(re.sub(pttn,repl,str))