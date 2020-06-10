"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# It creates a list with string-variables
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# Select each variables and print them seprately within the terminal.
for word in some_words:
    print(word)

# it does the same action as the command above. The point is variables could be called as any names in the list.
for x in some_words:
    print(x)

# Print the list within the terminal.
print(some_words)

# It creates the statement of the length of the list is greater than 3. The boolean answer is true and it operates the next line which is printing the string in the terminal.
if len(some_words) > 3:
    print('some_words contains more than 3 words')

# Uname is used to get information from the current device operating system. The print command is able to display the info within the terminal.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
