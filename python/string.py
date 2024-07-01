def swap_case(s):
    """Convert upper to lower, lower to upper
    
    """
    print(s.swapcase())

# output = 'ABa'
swap_case('abA')

def split_string(s):
    """Split string by delimiter
    """
    print(s.split(' '))
    
#output = ['split'. 'string']
split_string('split string')


def mutate_string(string, position, character):
    """Lists are mutable (can be changed), tuple / string are immutable
    """
    txt = string[:position] + character + string[position:]
    print(txt)

#output = 'Append String'
mutate_string('Appen String', 5, 'd')