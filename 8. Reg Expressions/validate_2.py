import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    # r = raw string - not to interpret backslash  \ in the usual way (r is a good habit for regular expressions to avoid errors with regular expressions)
    print("Valid")
else:
    print("Invalid")


#  . any character except a newline
#  * 0 or more repetitions
#  + 1 or more repetitions
#  ? 0 or 1 repetiton
#  {m} m repetitions
#  {m,n} m - n repetitions

#  \ escape character
#  ^ matches the start of the string
#  $ matches the end of the string
# [] set of characters (include) - e.g: a-zA-Z0-9
# [^] complementing the set (e.g anything but / exclude)

# \w word character + numbers + underscore
# \d decimal digit
# \D not a decimal digit
# \s whitespace character
# \w word character ... as well as numbers and the underscore
# \W not a word character

# A | B | C either A B or C etc.
# (...) a group
# (?:...)  non-capturing version


# re.IGNORECASE
# re.MULTILINE
# re.DOTALL
# re.match
# re.fullmatch

