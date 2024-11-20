def decode_camel_case(variable):
    split_variable = ""
    for i, char in enumerate(variable):
        if i > 0 and char.isupper():
            split_variable += " "
        split_variable += char
    split_variable = split_variable.lower()
    split_variable = split_variable.title()
    return split_variable
    

def encode_camel_case(variable):
    split_variable = variable.split(" ")
    for i in range(len(split_variable)):
        if i != 0:
            split_variable[i] = split_variable[i].title()
        else:
            split_variable[i] = split_variable[i].lower()

    return "".join(split_variable)


def decode_snake_case(variable):
    split_variable = variable.split("_")
    split_variable[0] = split_variable[0].title()

    return ' '.join(split_variable)


def encode_snake_case(variable):
    split_variable = variable.split(" ")
    split_variable = [x.lower() for x in split_variable]

    return "_".join(split_variable)

def convert(variable, style_from, style_to):
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
        else:
            return "Error: Invalid style"


print(convert("Hello world", "none", "camel"))
print(convert("helloWorld", "camel", "none"))
print(convert("helloWorld", "camel", "snake"))
print(convert("hello_world", "snake", "camel"))
print(convert("hello_world", "snake", "none"))
print(convert("Hello world", "none", "snake"))