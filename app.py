from class_parser import Parser


def main():
    new_parser = Parser("example.txt")
    text = new_parser.parser_function()
    print(text)


if __name__ == '__main__':
    main()
