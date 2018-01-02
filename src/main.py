"""Test file."""

def new_test(something):
    return "Here is {}".format(something)

def greet(word, name):
    """Hello world function."""

    return "{word} {name}!".format(name=name, word=word)

def main():
    """Da main man."""

    greeting = greet(word='Yello', name='Milkyway')
    print(greeting)

if __name__ == '__main__':
    main()
