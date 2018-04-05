print ("x   1  2  3  4  5  6  7  8  9  10  11  12")

for count in range(1, 13):
		print (count, count, count * 2, count * 3, count * 4, count * 5, count * 6, count * 7, count * 8, count * 9, count * 10, count * 11, count * 12)



#answer key ---- thought i had it but i quess this made alot more sense so ill exlain how everything in this answer key is working
# print ' x 1 2 3 4 5 6 7 8 9 10 11 12'  <---- prints the first base top layer of the multiplication table
# for row in range(1, 12 + 1): <----- starts a loop for in between 1 and 13 which will be 1-12 with the variable row
#     display_string  = '' <-----orimes a blank string
#     for column in range(0, 12 + 1): <----creates a coloumn and starts another loop between 0-13 or going though 0-12
#         if column is 0:  <-----the first time the column is created it will pass this line of code
#             display_string += ' ' + str(row)
#         else:    <------ everyother time we go through the loop it will 
#             display_string += ' ' + str(column * row)
#     print display_string   <------ displays the string one line at a time with each number 


for row in range(1, 12 + 1): 
    display_string  = ''
    # print display_string    
    for column in range(0, 12 + 1):
        if column is 0:
            display_string += ' ' + str(row)
        else:    
            display_string += ' ' + str(column * row)
            # print display_string    
    print display_string