import cowsay
import sys 
if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])

# sys.argv is used for using user input as an entry upon running say_1.py