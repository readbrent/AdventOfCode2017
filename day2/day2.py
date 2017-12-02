def get_checksum(matrix):
    '''
    Calculates a checksum by getting the sum of the differences between the
    smallest and largest member of each row.
    '''
    return sum([max(row) - min(row) for row in matrix])

def get_divisible_checksum(matrix):
    '''
    Calculates a checksum by getting the sum of the first divisible
    pairs within each row.
    '''
    return sum([get_divisible_pair(row) for row in matrix])

def test_answer():
    '''
    Basic sanity tests.
    '''
    check_test = [[5, 1, 9, 5],
                  [7, 5, 3],
                  [2, 4, 6, 8]]
    assert get_checksum(check_test) == 18

    divisible_test = [[5, 9, 2, 8],
                      [9, 4, 7, 3],
                      [3, 8, 6, 5]]
    assert get_divisible_checksum(divisible_test) == 9

def get_divisible_pair(row):
    '''
    Starting with a brute-force approach. Takes in a row
    and returns the result of the first possible division amongst
    members of the row.
    '''
    for i in range(len(row)):
        for j in range(i+1, len(row)):
            first_val = row[i]
            second_val = row[j]

            if first_val % second_val == 0:
                return first_val / second_val
            elif second_val % first_val == 0:
                return second_val / first_val

    return -1

def create_test_matrix(input_path):
    '''
    Reads in a file at the specified path and 
    creates a matrix of integers.
    '''
    with open(input_path) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    test_matrix = [line.split('\t') for line in content]
    int_matrix = [[int(x) for x in row] for row in test_matrix]

    return int_matrix

def process_input(input_path):
    '''
    Prints the checksum and divisible checksum of the input
    path to the console.
    '''
    int_matrix = create_test_matrix(input_path)

    print("Checksum is " + str(get_checksum(int_matrix)))
    print("Divisible Checksum is " + str(get_divisible_checksum(int_matrix)))

def main():
    test_answer()

    process_input('day2input.txt')

if __name__ == "__main__":
    main()
