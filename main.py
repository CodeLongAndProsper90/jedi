from editor import editor
import argparse
# Create the parserr
parser= argparse.ArgumentParser(description='JEDI is a Ed clone, made in the 21st Century')

# Add the arguments
parser.add_argument('file', type=str, help='The path used to access the file to edit (Ex: ~/.bashrc')
parser.add_argument('-p', action='store', type=str, help='The prompt string to be used')

args = parser.parse_args()

e = editor(args.file)
while True:
    command = input(args.p) # TODO: Make prompt with -p
    if command == 'a':
        data = []
        txt = ""
        while txt != "`":
            txt = input()
            data.append(txt)
        e.append(data)
    elif command == 'w':
        e.write()
    elif command == 'q':
        break
