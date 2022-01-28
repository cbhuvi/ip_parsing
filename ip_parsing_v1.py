import sys
def convert_number_string(number: int) -> str:
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0
    if is_divisible_by_3 and is_divisible_by_5:
        return 'fizzbuzz'
    if is_divisible_by_3:
        return 'fizz'
    if is_divisible_by_5:
        return 'buzz'
    return number
local_file_name = "C:\\Users\\bhuvi\\Desktop\\Interview\\file\\problem_input.txt"
if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as ip_file:
        for line in ip_file:
            # distinguishing between subnet and port
            if '/' in line:
                idx = line.rfind('/')
            if ':' in line:
                idx = line.rfind(':')
            number = int(line[idx+1:].strip())
            print(convert_number_string(number))
else:
    print("python ip_parsing_v1.py file_name")

