with open('test.txt', 'r') as text_file:
    reader = text_file.readlines()

    content = ''
    for word in reader:
        cleaned_word = word.replace('\n', '')
        content += cleaned_word
        print(cleaned_word)
    print(content)