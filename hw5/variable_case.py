# Convert a normalstring to camel case
def encodeCamelCase(string_in):
    step1 = string_in.split(' ')
    step2 = [word.upper() for word in step1]
    step2[0] = step2[0].lower()
    step3 = ''.join(step2)
    return step3

# Convert a camel case string to a normal string as best as possible
def decodeCamelCase(string_in):
    step1 = []
    avoid = 0
    for idx, char in enumerate(string_in):
        avoid = 0
        if char.isupper():
            step1.append(string_in[avoid:idx])
            avoid = idx + 1
    step1.append(string_in[avoid:len(string_in)])
    step2 = [word.capitalize() for word in step1]
    step3 = ' '.join(step2)
    return step3

# Convert a normal string to snake case
def encodeSnakeCase(string_in, style_from):
    step1 = string_in.split(' ')
    step2 = [word.lower() for word in step1]
    step3 = '_'.join(step2)
    return step3

# Convert a snake case string to a normal string as best as possible
def decodeSnakeCase(string_in):
    step1 = string_in.split('_')
    step2 = [word.capitalize() for word in step1] 
    step3 = ''.join(step2)
    return step3

def convert(string_in, style_from, style_to):
    if (style_from != 'camel' or style_from != 'snake' or style_from != 'none') and (style_to != 'camel' or style_to != 'snake' or style_to != 'none'):
        print('Error: invalid style')

    if style_from == style_to:
        return string_in
    elif style_from == 'camel' and style_to == 'snake':
        step = decodeCamelCase(string_in)
        return encodeSnakeCase(string_in)
    elif style_from == 'snake' and style_to == 'camel':
        step = decodeSnakeCase(string_in)
        return encodeCamelCase(string_in)
    elif style_from == 'snake' and style_to == 'none':
        return decodeSnakeCase(string_in)
    elif style_from == 'none' and style_to == 'snake':
        return encodeSnakeCase(string_in)
    elif style_from == 'none' and style_to == 'camel':
        return encodeCamelCase(string_in)
