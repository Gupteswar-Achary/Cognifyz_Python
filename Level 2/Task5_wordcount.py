import string


def count(file_path):
    count_word = {}
    special_chars = string.punctuation

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.split()
            # Count occurrences of each word
            for word in words:
                # Remove special characters and convert to lowercase
                word = word.strip(special_chars).lower()
                # Count occurrence of the words
                if word:
                    count_word[word] = count_word.get(word, 0) + 1

    # Sort the dictionary by keys (words)
    sorted_word = sorted(count_word.items())

    # Display results
    for word, count in sorted_word:
        print(f"{word}: {count}")


# Provide the path to your text file
path = "text_file.txt"
count(path)
