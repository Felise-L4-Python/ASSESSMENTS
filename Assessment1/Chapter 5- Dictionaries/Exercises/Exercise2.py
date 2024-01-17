glossary = {
    'Comment' : 'Comments are the notes of the programmer which are ignored by the Python interpreter.',
    'Variables' : 'Variable is a name that represents a value stored in a computer memory',
    'Data structures' : 'Data structure are containers that organize and group data according to its type.',
    'List' : 'List is an object that contains multiple data items',
    'Loop' : 'Loops are repetiton of a command to minimize the repetition of statements',
    } # The variable "glossary" is stored data including 'comment', 'variables', 'data structures', 'list', 'loop' and their information.
word = 'Comment' #word is assigned 'Comment'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'Variables' #word is assigned 'Variables'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'Data structures' #word is assigned 'Data Structure'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'List' #word is assigned 'List'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description

word = 'Loop' #word is assigned 'Loop'
print(f"\n{word.title()}: {glossary[word]}") #prints the title and its description