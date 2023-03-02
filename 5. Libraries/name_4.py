import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    # for inputs in the input i.e "David, Peter Josh"
    print("hello, my name is", arg)