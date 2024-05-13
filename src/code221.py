import keyword

def python_syntax():

    print(keyword.kwlist)
    """
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
    'try', 'while', 'with', 'yield']
    """

if __name__ == '__main__':
    print("This is main function!")
    python_syntax()