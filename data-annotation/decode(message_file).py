def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extracting the number and corresponding word from each line
    number_word_pairs = {int(line.split()[0]): line.split()[1] for line in lines}

    # Building the pyramid structure
    numbers = set()
    current_line = 1
    current_num = 1

    while current_num <= max(number_word_pairs.keys()):
        if current_num == current_line * (current_line + 1) // 2:
            numbers.add(current_num)
            current_line += 1
        current_num += 1

    # Constructing the decoded message
    decoded_message = ' '.join([number_word_pairs[num] for num in sorted(numbers) if num in number_word_pairs])

    return decoded_message


decoded_message = decode('message_file.txt')
print(decoded_message)
