strings_list = ["hi", "hello"]
def length_and_parity_of_strings(strings_list):
    length_and_parity_dict = {}
    for string in strings_list:
        length = len(string)
        length_and_parity_dict["length"] = length
        if length % 2 == 0:
            length_and_parity_dict["parity"] = "even"
        else:
            length_and_parity_dict["parity"] = "odd"
        print(f"{string} : {length_and_parity_dict}")

length_and_parity_of_strings(strings_list)


