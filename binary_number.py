from stack import Stack

def div_by_2(dec_num):
    s = []
    while dec_num > 0:
        remainder = dec_num % 2
        s.append(remainder)
        dec_num = dec_num // 2
    
    binary_num = ''
    while len(s) is not 0:
        binary_num = binary_num + str(s.pop())
    
    return binary_num

print("binary : ",div_by_2(242))
    