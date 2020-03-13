import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
operator_list = ("+", "-", "*", "/")
num_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')

def process_string(exp_list, str, index):
    while index < len(str):
        if str[index] == "(":
            new_list = list()
            new_list, index = process_string(new_list, str, index + 1)
            exp_list.append(new_list)
        elif str[index] in operator_list:
            exp_list.append(str[index])
            index += 1
        elif str[index] in num_list:
            num_str = str[index]
            index += 1
            while index < len(str) and str[index] in num_list:
                num_str += str[index]
                index += 1
            try:
                num = int(num_str)
            except:
                num = float(num_str)
            exp_list.append(num)
        elif str[index] == ')':
            return exp_list, (index + 1)
        else:
            logging.error("Error Occurred! Invalid expression!")
    return exp_list

def calculate_result(exp_list, index):
    if len(exp_list) <= 0:
        return 0
    if len(exp_list) % 2 == 0:
        logging.error('ERROR!')
        return 0
    if isinstance(exp_list[index], list):
        pre = calculate_result(exp_list[index], 0)
    else:
        pre = exp_list[index]
    cur = 0
    while index < len(exp_list) - 2:
        if isinstance(exp_list[index + 2], list):
            cur = calculate_result(exp_list[index + 2], 0)
        else:
            cur = exp_list[index + 2]
        if exp_list[index + 1] == '+':
            pre = pre + cur
        elif exp_list[index + 1] == '-':
            pre = pre - cur
        elif exp_list[index + 1] == '*':
            pre = pre * cur
        elif exp_list[index + 1] == '/':
            pre = pre / cur
        else:
            logging.error('Error occurred! Invalid operation!')
            return 0
        index += 2
    return pre
            

if __name__ == "__main__":
    input_string = ''
    while True:
        input_string = input()
        if input_string == 'quit':
            print('Bye')
            break
        expression_list = list()
        expression_list = process_string(expression_list, input_string, 0)
        index = 0
        while index < len(expression_list) - 2:
            if expression_list[index + 1] in ('*', '/'):
                new_list = [expression_list[index], expression_list[index + 1], expression_list[index + 2]]
                del expression_list[index: index + 3]
                expression_list.insert(index, new_list)
            else:
                index += 1
        result = calculate_result(expression_list, 0)
        if isinstance(result, float):
            if result.is_integer():
                result = int(result)
        print(round(result, 10))
        
