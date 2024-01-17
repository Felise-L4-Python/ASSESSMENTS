glossary = {
    'Comment' : 'Comments are the notes of the programmer which are ignored by the Python interpreter.',
    'Variables' : 'Variable is a name that represents a value stored in a computer memory',
    'Data structures' : 'Data structure are containers that organize and group data according to its type.',
    'List' : 'List is an object that contains multiple data items',
    'Loop' : 'Loops are repetiton of a command to minimize the repetition of statements',
    'String' : 'String is a sequence of characters.',
    'Tuple' : 'Tuples are used as keys in dictionaries, it also cannot be modified once they are created',
    'Dictionary' : 'Dictionary is a collection of key-value pairs',
    'Float' : 'Float is a numerical value with a decimal component',
    'Integer' : 'Integer is a whole number, positive or negative, without any decimal'
    } # The variable "glossary" is stored data including 'comment', 'variables', 'data structures', 'list', 'loop' and their information.

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}") # This prints the the names and descriptions in the glossary.