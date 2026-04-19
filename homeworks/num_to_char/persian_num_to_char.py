# nums_in_char = {
#     '0 zero'    : ["", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"],
#      0          : ["صفر", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"],  # 'OG nums'
#      1          : ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"],  # '1 zero'
#     '3 zero'    : ["صد"],
#     'digit sep' : ["", "هزار", "میلیون", "میلیارد"]
# }

nums_in_char = {
    '0 zero'    : ["yazdah", "davazdah", "sizdah", "chahardah", "panzdah", "shanzdah", "hefdah", "hejdah", "noozdah"],
     0          : ["sefr", "yek", "do", "se", "chahar", "panj", "shesh", "haft", "hasht", "noh"],  # 'OG nums'
     1          : ["", "dah", "bist", "si", "chehel", "panjah", "shast", "haftad", "hashtad", "navad"],  # '1 zero'    (""?????)
    '3 zero'    : ["sad O", "devist O", "sisad O", "pansad O"],
    'digit sep' : ["", "hezar", "million", "milliard"]
}


def print_stack(stack):
    while(stack.__len__() != 0):
        print(stack.pop(), end=" ")


semi_stack = []

num = 4085704302
num_copy = num

digit_sep_counter = 0  # seprate times
while(num_copy != 0):
    triple_sep = num_copy % 1000  # seprate each three digits
    seprated_len = triple_sep.__str__().__len__()  # "zerohundred forty seven"  -->  "forty seven"

    digit_counter = 0  # from left to right ('yekan' to 'sadgan')

    if(digit_sep_counter > 0):
        semi_stack.append(nums_in_char["digit sep"][digit_sep_counter] + " va")

    for i in range(seprated_len):
        digit = triple_sep%10  # seprate each digit
        if(i<2):
            semi_stack.append(nums_in_char[digit_counter][digit]) if i==0 else semi_stack.append(nums_in_char[digit_counter][digit])
            if(i==0):  # save first digit(from left) for "if the second was 1"
                target = digit
            if(i==1 and digit==1):  # check second digit(from left)
                semi_stack.pop(), semi_stack.pop()  # pop two digits(from left) to replace with "10< num <20"
                semi_stack.append(nums_in_char['0 zero'][target+1])
            digit_counter+=1
        else:
            if(digit == 5):  #500
                semi_stack.append(nums_in_char['3 zero'][3])
            elif(digit == 2):  #200
                semi_stack.append(nums_in_char['3 zero'][1])
            elif(digit == 3):  #300
                semi_stack.append(nums_in_char['3 zero'][2])
            else:
                semi_stack.append(nums_in_char[0][digit] + nums_in_char['3 zero'][0])
        triple_sep = (triple_sep-digit)//10

    digit_sep_counter+=1
    num_copy = (num_copy - triple_sep)//1000

print_stack(semi_stack)

#MadMad_64