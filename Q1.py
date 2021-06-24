number_of_rows = int(input('Number of rows : '))
if number_of_rows >=1:
    number_of_columns = int(input('Number of columns : '))
    if number_of_columns<= 1000:
        arr = []
        for single_row in range(number_of_rows):
            arr += [0]
        for single_row in range(number_of_rows):
            arr[single_row] = [0] * number_of_columns
        for single_row in range(number_of_rows):
            for single_column in range(number_of_columns):
                arr[single_row][single_column] = (input("please enter a single value and then press enter\t"))
        for single_row in range(number_of_rows):
            for single_column in range(number_of_columns):
                pass# print(arr[single_row][single_column], end=" ")
            print("\n")
        row_comparable = 0
        column_comparable = 0
        end=" "
        while (row_comparable < number_of_rows and column_comparable < number_of_columns):
            for single_column in range(column_comparable, number_of_columns):
                print(arr[row_comparable][single_column], end=" ")
            row_comparable += 1
            for single_row in range(row_comparable, number_of_rows):
                print(arr[single_row][number_of_columns - 1], end=" ")
            number_of_columns -= 1
            if (row_comparable < number_of_rows):
                for single_column in range(number_of_columns - 1, (column_comparable - 1), -1):
                    print(arr[number_of_rows - 1][single_column], end=" ")
                number_of_rows -= 1
            if (column_comparable < number_of_columns):
                for single_row in range(number_of_rows - 1, row_comparable - 1, -1):
                    print(arr[single_row][column_comparable], end=" ")
                column_comparable += 1
    else:
        print("Number of Columns must be 1000 or less")

else:
    print("Number of Rows must be 1 or Grater")


