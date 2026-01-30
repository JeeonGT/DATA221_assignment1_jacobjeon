def percentage_distribution_dictionary(numbers_list):
    distributed_numbers_result = {}
    length_numbers_list = len(numbers_list)

    for value in numbers_list:
        if value not in distributed_numbers_result:
            count = 0
            for x in numbers_list:
                if x <= value:
                    count += 1
            distributed_numbers_result[value] = (count / length_numbers_list) * 100

    return sorted(distributed_numbers_result.items())

print(percentage_distribution_dictionary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))