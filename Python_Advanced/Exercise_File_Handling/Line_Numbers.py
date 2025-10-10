with open("numbers.txt") as input_file, open("output.txt", "w") as output_file:
    result= []
    for index_row, text_line in enumerate(input_file):
        letters_count = 0
        punctuation_count = 0

        for character in text_line:
            if character.isalpha():
                letters_count += 1
            elif character.isdigit():
                punctuation_count += 1
        result.append(f"Line {index_row + 1}: {text_line.strip()} ({letters_count}) ({punctuation_count})")
    output_file.write("\n".join(result))
