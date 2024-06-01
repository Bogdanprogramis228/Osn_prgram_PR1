print("\n6 ЗАВДАННЯ\n") 

number_list = ["01010101", "00011100011"]

for number in number_list:
    valid = True
    i = 0
    n = len(number)
    
    while i < n:
        if number[i] == '0':
            
            zero_count = 0
            while i < n and number[i] == '0':
                zero_count += 1
                i += 1
            
            one_count = 0
            while i < n and number[i] == '1':
                one_count += 1
                i += 1
            
            if zero_count != one_count:
                valid = False
                break
        else:
            i += 1
            
    print(valid)