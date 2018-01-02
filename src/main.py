"""Test Python script."""


def greet_me(word, name):
    """Hello world function."""

    return "{word} {name}!".format(name=name, word=word)

def main():
    """Da main man."""

    greeting = greet_me(word='Yello', name='Milkyway')
    print(greeting)

if __name__ == '__main__':
    main()
