def main():
    print_square(5)
# my solution
def print_square(size):
    # for each row in range of size
    for i in range(size):
        # print value * size
         print("#" * size)

# CS50 solution (prefer mine)
def print_squares(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        print()
main()