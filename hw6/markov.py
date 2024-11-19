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
    words = [word for word in words if word != ' ']
    
    n_grams = float(input("How many n-grams would you like to consider? "))
    n_grams = int(n_grams)
    analysis = {}
    if n_grams == 1:
        for prefix, candidate in zip(words, words[1:]):
            if prefix not in analysis:
                analysis[prefix] = []

            analysis[prefix].append(candidate.strip(' '))
    else:
        n_words = [(words[i], words[i-1]) for i in range(1, len(words))]
        for prefix, candidate in zip(n_words, words[n_grams:]):
            if prefix.strip() not in analysis:
                analysis[prefix.strip()] = []

            analysis[prefix.strip()].append(candidate.strip(' '))

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

    adjusted_prefix = ''
    if type(prefix) == tuple:
        a_prefix = list(prefix)
        a_prefix[0] = a_prefix[0].title().strip(' ')
        adjusted_prefix = tuple(a_prefix)
    else:
        adjusted_prefix = prefix.title().strip(' ')
    
    line = []
    line.append(adjusted_prefix)
    # Generate 10 words
    for i in range(amount):
        choice = random.choice(analysis[prefix])
        if type(choice) == tuple():
            for x in choice:
                line.append(choice)
        else:
            line.append(choice)
        prefix = choice
    

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
    with open(output_file, "w") as outfile:
        outfile.write(' '.join(line))

## Text generation
text = load_text()
analysis = markov_analysis(text)
stats(analysis)
generate(analysis)
