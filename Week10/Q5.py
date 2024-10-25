def func(file_path):

    with open(file_path, 'r') as file:
        content = file.read()

    words = content.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    common_word = max(word_counts, key=word_counts.get)
    common_count = word_counts[common_word]

    print(f"The word with the maximum instances is '{common_word}' with {common_count} occurrences.")

    updated_content = content.replace(common_word, "Aligarh")

    with open(file_path, 'w') as file:
        file.write(updated_content)

    print("All occurrences of the word have been replaced with 'Aligarh'.")

file_path = 'sample.txt'
func(file_path)
