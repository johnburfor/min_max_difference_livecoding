the_array = [15,22,84,14,88,23]

i = 0
for i in the_array:
    if the_array[i] > the_array[i+1]:
        highest_number = the_array[i]
    else:
        highest_number = the_array[i+1]

i = 0
for i in the_array:
    if the_array[i] < the_array[i+1]:
        lowest_number = the_array[i]
    else:
        lowest_number = the_array[i+1]        

difference = highest_number - lowest_number