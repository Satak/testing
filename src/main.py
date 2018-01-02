"""Test Python script."""


def greet_me(word: str, name: str) -> str:
    """Hello world function."""

    return "{word} {name}!".format(
        name=name.capitalize(),
        word=word.capitalize()
    )

def main():
    """Da main man."""

    name = input('Give yar namee: ')
    word = input('Give greeting: ')
    greeting = greet_me(word=word, name=name)
    print(greeting)

if __name__ == '__main__':
    main()
