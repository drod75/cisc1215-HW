def decode_camel_case(variable):
    snake_case = ""
    for i in range(len(variable)):
        if variable[i].isupper():
            if i > 0:
                snake_case += " "
            snake_case += variable[i].lower()
        else:
            snake_case += variable[i]

    return snake_case


def encode_camel_case(variable):
    camel_case = ""
    capitalize_next = False
    for i in range(len(variable)):
        if variable[i] == "_":
            capitalize_next = True
        else:
            if capitalize_next:
                camel_case += variable[i].lower()
                capitalize_next = False
            else:
                camel_case += variable[i].lower()

    return camel_case


def decode_snake_case(variable):
    camel_case = ""
    capitalize_next = False
    for i in range(len(variable)):
        if variable[i] == "_":
            capitalize_next = True
        else:
            if capitalize_next:
                camel_case += variable[i].upper()
                capitalize_next = False
            else:
                camel_case += variable[i]

    return camel_case


def encode_snake_case(variable):
    snake_case = ""
    for i in range(len(variable)):
        if variable[i].isupper():
            if i > 0:
                snake_case += "_"
            snake_case += variable[i].lower()
        else:
            snake_case += variable[i]

    return snake_case

def convert(variable, style_from, style_to):
    if (style_from != 'camel' or style_from != 'snake' or style_from != 'none') or (style_to != 'camel' or style_to != 'snake' or style_to != 'none'):
        print('Error: invalid style')
    else:
        if style_from == style_to:
            return variable
        elif style_from == 'camel' and style_to == 'snake':
            return encode_snake_case(decode_camel_case(variable))
        elif style_from == 'snake' and style_to == 'camel':
            return encode_camel_case(decode_snake_case(variable))
        elif style_from == 'snake' and style_to == 'none':
            return decode_snake_case(variable)
        elif style_from == 'camel' and style_to == 'none':
            return decode_camel_case(variable)
        elif style_from == 'none' and style_to == 'snake':
            return encode_snake_case(variable)
        elif style_from == 'none' and style_to == 'camel':
            return encode_camel_case(variable)


print(convert("Hello world", "none", "camel"))
print(convert("helloWorld", "camel", "snake"))
print(convert("hello_world", "snake", "none"))
