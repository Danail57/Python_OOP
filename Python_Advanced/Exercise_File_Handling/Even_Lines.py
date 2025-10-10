with open("even_lines.txt") as file:
    for index_row, text_line in enumerate(file):
        if index_row % 2 == 0:
            for symbol in {"-", ",", ".", "!", "?"}:
                text_line = text_line.replace(symbol, "@")
            print(" ".join(reversed(text_line.split())))
