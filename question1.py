def integer_factorial_function(threshold):

    current_number = 1
    current_product = 1
    while current_product <= threshold:
        current_product = current_product * current_number
        current_number = current_number + 1
    print("Final product:", current_product)
    print("Integer that exceeded threshold:", current_number - 1)

integer_factorial_function(100)

