
def solution(U, L, C):

    number_of_columns = len(C) 
    
    first_row = [0] * number_of_columns
    second_row = [0] * number_of_columns

    ones_in_first_row = U
    ones_in_second_row = L

    if ones_in_first_row + ones_in_second_row != sum(C):
        return "IMPOSSIBLE"

    else:
        
        for i in range(number_of_columns):
            if C[i] == 2:
                first_row[i], second_row[i] = 1,1


            if C[i] == 1:
                sum_of_first = sum(first_row)
                sum_of_second = sum(second_row)

                if sum_of_first < U:
                    first_row[i], second_row[i] = 1, 0

                elif sum_of_second < ones_in_second_row:
                    first_row[i], second_row[i] = 0, 1

        ones_in_first = sum(first_row)
        ones_in_second = sum(second_row)

        if (ones_in_first < ones_in_first_row and ones_in_second > ones_in_second_row) or (ones_in_second < ones_in_second_row and ones_in_first > U):
            
            for i in range(number_of_columns):
                
                if first_row[i] == 0 and second_row[i] == 1 and sum(first_row) < ones_in_first_row and sum(second_row) > ones_in_second_row:
                    first_row[i], second_row[i] = 1, 0
                
                if first_row[i] == 1 and second_row[i] == 0 and sum(second_row) < ones_in_second_row and sum(first_row) > ones_in_first_row:
                    first_row[i], second_row[i] = 0, 1 

                else: break   

        
        for i in range(number_of_columns):
            print(first_row[i], end = "")
        
        print(", ", end = "")

        for i in range(number_of_columns):
            print(second_row[i], end = "")


solution(2, 4, [1,2,1,2])
                

            



