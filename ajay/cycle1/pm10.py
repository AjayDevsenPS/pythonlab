def exchange_first_last_characters(input_string):
    if len(input_string) < 2:
        return input_string
    first_char = input_string[0]
    last_char = input_string[-1]
    new_string = last_char + input_string[1:-1] + first_char
    return new_string
input_string = input("Enter a string: ")
result_string = exchange_first_last_characters(input_string)
print("String with first and last characters exchanged:", result_string)

