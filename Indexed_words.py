def find_indexed_words(text):
    import re


    # Split the passage into sentences using period as the delimiter
    sentences = re.split(r'\.\s*', text)

    # Iterate over each sentence and convert the first word to lowercase
    modified_sentences = [re.sub(r'^(\w+)', lambda match: match.group(1).lower(), sentence) for sentence in sentences]

    # Join the modified sentences back into a single passage
    text = '. '.join(modified_sentences)
    sentences = text.split('. ')  # Split the text into sentences

    indexed_words = []  # List to store the indexed words and their indices
    index = 1  # Word index

    for sentence in sentences:
        words = sentence.split()  # Split each sentence into words

        for word in words:
            word = word.rstrip('.;')  # Remove period and semicolon from the end of the word

            if word and word[0].isupper() and not word.isspace():  # Check if the word starts with an uppercase letter, is not empty, and not only whitespace
                indexed_words.append((index, word))

            index += 1
            

    if not indexed_words:  # If no indexed words are found
        return None

    return indexed_words


text = input()
result = find_indexed_words(text)

if result is None:
    print("None")
else:
    for index, word in result:
        print(f"{index}:{word}")