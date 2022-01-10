class Parser:
    def __init__(self, parse_file):
        self.lines = open(parse_file, "r").readlines()
        self.char = open(parse_file, "r").read()

    def parser_function(self):
        total_sentences = len(self.lines)
        total_char = len(self.char)

        return {"sentences": [total_sentences],
                "stats": dict(total_sentences=total_sentences, total_char=total_char)}
