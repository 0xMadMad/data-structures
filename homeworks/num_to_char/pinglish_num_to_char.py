nums_in_char = {
    '0 zero'    : ["",      "eleven", "twelve",  "thertheen", "fortheen", "fiftheen", "sixteen", "seventeen", "eighteen", "nineteen"],
     0          : ["zero",  "one",    "two",     "three",     "four",     "five",     "six",     "seven",     "eight",    "nine"],   # 'OG nums'
     1          : ["",      "ten",    "twenty",  "thirty",    "forty",    "fifty",    "sixty",   "seventy",   "eighty",   "ninety"], # '1 zero'
    '3 zero'    : ["hundred"],
    'digit sep' : ["", "thousand", "million", "billion"]
}

def print_stack(stack):
    while(stack.__len__() != 0):
        print(stack.pop(), end=" ")


semi_stack = []

num = 408574302
num_copy = num

digit_sep_counter = 0  # seprate times
while(num_copy != 0):
    triple_sep = num_copy % 1000  # seprate each three digits
    seprated_len = triple_sep.__str__().__len__()  # "zerohundred forty seven"  -->  "forty seven"

    digit_counter = 0  # from left to right ('yekan' to 'sadgan')

    if(digit_sep_counter > 0):
        semi_stack.append(nums_in_char["digit sep"][digit_sep_counter] + " and")

    for i in range(seprated_len):
        digit = triple_sep%10  # seprate each digit
        if(i<2):
            semi_stack.append(nums_in_char[digit_counter][digit])
            if(i==0):  # save first digit(from left) for "if the second was 1"
                target = digit
            if(i==1 and digit==1):  # check second digit(from left)
                semi_stack.pop(), semi_stack.pop()  # pop two digits(from left) to replace with "10< num <20"
                semi_stack.append(nums_in_char['0 zero'][target])
            digit_counter+=1
        else:
            semi_stack.append(nums_in_char[0][digit] + nums_in_char['3 zero'][0])
        triple_sep = (triple_sep-digit)//10

    digit_sep_counter+=1
    num_copy = (num_copy - triple_sep)//1000

print_stack(semi_stack)

#MadMad_48