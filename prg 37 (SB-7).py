def fullJustify(words, maxWidth):
    result = []  
    current_line = []  
    current_length = 0
    for word in words:
        if current_length + len(current_line) + len(word) > maxWidth:
            for i in range(maxWidth - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            result.append(''.join(current_line))
            current_line, current_length = [], 0  
        current_line.append(word)
        current_length += len(word)
    result.append(' '.join(current_line).ljust(maxWidth))
    return result
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = fullJustify(words, maxWidth)
for line in output:
    print(f'"{line}"')  
