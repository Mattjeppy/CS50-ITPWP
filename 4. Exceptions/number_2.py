def main():
    x = get_int("What's x?")
    print("x is", x)

def get_int(prompt):
    while True:
        try: return int(input(prompt))
        except ValueError: print("x is not an integer")
        # handle an exception but not doing anything with it
        except: pass

main()