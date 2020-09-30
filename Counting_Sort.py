def counting_sort(input_number):
    list_input_number = []  # initiate new list
    for x in input_number:
        list_input_number.append(int(x))  # convert string to list with integer
    # print(list_input_number)

    length_list = len(list_input_number)  # to find the length of the list(array)
    count = [0] * 10  # counter for 0-9 digits
    for element in list_input_number:  # loop to count the digits in the index
        count[element] += 1
    # print(count)

    for element in range(1, len(count)):  # Find cumulative sum
        count[element] += count[element - 1]
    # print(count)

    output_list_number = [0] * length_list  # initiate new list
    i = length_list - 1
    while i >= 0:  # sorting the numbers based on the cumulative sum
        output_list_number[count[list_input_number[i]] - 1] = list_input_number[
            i]  # placing the element in its position
        # print(output_list_number)
        count[list_input_number[i]] -= 1  # deducting the count number
        # print(count)
        i -= 1
    # print(output_list_number)

    sorted_numbers = []  # initialize new empty list
    for x in output_list_number:  # convert the int list to string
        sorted_numbers.append(str(x))

    result = ""  # initialize empty string variable
    return result.join(sorted_numbers)


user_input = input("Enter digits between 0-9: ")  # Take input from user as string

sorted_string = counting_sort(user_input)

print(f"The sorted list is: {sorted_string}")
