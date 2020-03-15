from editor import editor
import argparse
# Create the parserr
parser= argparse.ArgumentParser(description='JEDI is a Ed clone, made in the 21st Century')

# Add the arguments
parser.add_argument('file', type=str, help='The path used to access the file to edit (Ex: ~/.bashrc')
parser.add_argument('-p', nargs='?', const='', action='store', type=str, help='The prompt string to be used')
def split(word): 
    return [char for char in word] 
args = parser.parse_args()

e = editor(args.file)
p = args.p
if p == 'None':
    p=''
while True:
    command = split(input(p))
    if command[0] == 'a':
        data = []
        txt = ""
        while txt != "`":
            data.append(txt) 
            txt = input()
        data.remove(data[0])
        e.append(data)
    elif command[0] == 'w':
        e.write()
    elif e.isint(command[0]):
        e.goto(command[0])
    elif command[0] == 'p':
        if len(command) == 1:
           print( e.getln())
        elif len(split(command)) == 2:
            print(e.getln(int(command[1])))
    elif command[0] == 'd':
        if len(command) == 1:
            e.delline()
        elif len(command) == 2:
            error = e.delline(command[1])
    elif command[0] == 'q':
        break

