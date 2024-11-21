import random
import time

def load_text():
    filename = input("Enter the name of the file: ")
    time.sleep(0.5)

    lines = ''
    with open(filename, "r", encoding='utf8') as infile:
        lines = infile.readlines()

    if lines != '':
        text = ""
        for line in lines:
            line = line.strip()
            line = line.lower()

            chars = list(line)
            modified_line = ""
            for char in chars:
                if char.isalnum() and char != ' ':
                    modified_line += char
                elif char == ' ':
                    modified_line += " "
            if len(line) > 0:
                text = text + " " + modified_line

        return text
    else:
        print("Error reading file")

def markov_analysis(text):
    # Assume a space means a new word
    words = text.split(" ")
    words = [word.strip() for word in words if word != ' ']
    
    n_true = True
    while n_true:
        n_grams = input("How many n-grams would you like to consider? (1 or 2): ")
        n_grams = int(n_grams)
        if n_grams == 1 or n_grams== 2:
            n_true = False

    analysis = {}
    if n_grams == 1:
        for prefix, candidate in zip(words, words[1:]):
            if prefix not in analysis:
                analysis[prefix] = []

            analysis[prefix].append(candidate.strip(' '))
    else:
        n_words = []
        for i in range(1,len(words)):
            if words[i-1] != '' and words[i] != '':
                n_words.append((words[i-1].strip(' '), words[i].strip(' ')))

        for prefix, candidate in zip(n_words, words[n_grams:]):
            if prefix not in analysis:
                analysis[prefix] = []

            analysis[prefix].append(candidate.strip(' '))

    return analysis

def stats(analysis):
    prefix_count = 0
    average_prefix_associations = 0
    for prefix, candidates in analysis.items():
        prefix_count += 1
        average_prefix_associations += len(candidates)

    average_prefix_associations /= prefix_count
    time.sleep(0.5)
    apa_string = f'Average prefix associations: {average_prefix_associations:.2f}'
    print(apa_string)
    time.sleep(0.5)
    print("Total prefixes:", prefix_count)

def generate(analysis):
    w = True
    while w:
        time.sleep(0.5)
        amount = float(input('How many words would you like to generate? '))
        amount = int(amount)
        if amount > 0:
            w = False
        else:
            time.sleep(0.5)
            print("Please enter a positive integer")


    # Choose a random prefix
    prefix = random.choice(list(analysis.keys()))
    time.sleep(0.5)

    line = []
    if type(prefix) == tuple:
        for x in prefix:
            line.append(x.strip())
    else:
        line.append(prefix)

    # Generate 10 words
    for i in range(amount):
        if type(prefix) != tuple:
            keys = list(analysis.keys())
            prefix_keys = [x for x in keys if prefix in list(x)]
            prefix = random.choice(prefix_keys)

        options = analysis.get(prefix)
        try:
            choice = random.choice(options)
            if type(choice) == tuple:
                for x in choice:
                    line.append(choice)
            else:
                line.append(choice)
            prefix = choice
        except:
            print("Error generating choice")
    
    line[0] = line[0].title()
    line[-1] = line[-1] + '.'
    print()
    time.sleep(0.1)
    for l in line:
        time.sleep(0.1)
        print(l, end=' ')
    print(' ')
    print()

    time.sleep(0.5)
    output_file = input("Enter the name of the output file: ")
    if output_file[-4:] != '.txt':
        output_file += '.txt'
    with open(output_file, "w") as outfile:
        outfile.write(' '.join(line))

def markov_setup():
    text = load_text()
    analysis = markov_analysis(text)
    stats(analysis)
    generate(analysis)
    print('\nThank you for using the Markov Text generator!')

## Text generation
text = load_text()
analysis = markov_analysis(text)
stats(analysis)
generate(analysis)
