
from class_parser import Parser
import time

def main():
    new_parser = Parser("example.txt")
    text = new_parser.parser_function()
    print(text)


if __name__ == '__main__':
    main()
    start = time.time()
    print(f"Total time to execute was {time.time() - start}")
