nums_in_char = {
    '0 zero'    : ["",      "eleven", "twelve",  "thertheen", "fortheen", "fiftheen", "sixteen", "seventeen", "eighteen", "nineteen"],
     0          : ["zero",  "one",    "two",     "three",     "four",     "five",     "six",     "seven",     "eight",    "nine"],   # 'OG nums'
     1          : ["",      "ten",    "twenty",  "thirty",    "forty",    "fifty",    "sixty",   "seventy",   "eighty",   "ninety"] # '1 zero'
    # 'digit sep' : ["hundred", "thousand", "million", "billion"]
}


num = 12022032480
num_copy = num

semi_stack = []
while(num_copy != 0):
    semi_stack.append(num_copy%10)
    num_copy = (num_copy-num_copy%10)//10

while(semi_stack):  # while semi_stack has number
    double_sep = []
    for i in range(2):
        if(semi_stack):
            double_sep.append(semi_stack.pop())
    seprated_len = len(double_sep)

    if(seprated_len==1):
        print(nums_in_char[0][double_sep[0]])
    else:        
        if(double_sep[0] == 0):  # like "02"
            print(nums_in_char[0][0], nums_in_char[0][double_sep[1]], end=" ")
        elif(double_sep[1] == 0):  # like "20"
            print(nums_in_char[1][double_sep[0]], end=" ")
        elif(double_sep[0] == 1):  # like "12"
            print(nums_in_char['0 zero'][double_sep[1]], end=" ")
        else:  # any
            print(nums_in_char[1][double_sep[0]], nums_in_char[0][double_sep[1]], end=" ")

#MadMad_36