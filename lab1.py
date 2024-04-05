"""Вимоги:
- реалізувати завдання згідно до вашого номеру в групі (якщо ваш номер 16 або 17, то відповідно берете 1 або 2)
- обов'язкове покриття програми юніт-тестами
- мова програмування на ваш смак
- якщо програма виконалась успішно, вона має повернути код виходу 0
- будь-які помилки в програмі мають писатися в stderr, а сама програма при цьому повертати будь-який ненульовий код виходу
"""

import sys


def transorm_from_csv_to_json(csv_from_test=None, show_stdout=True, receive_stdout=False, show_stderr=True, absolute_false=True): #, receive_stderr=False
    if csv_from_test is None:
        text_csv = sys.stdin.readlines()
    else:
        if absolute_false:
            show_stdout = False
            show_stderr = False
        text_csv = csv_from_test
    
    # print(type(text_csv))
    
    if type(text_csv) != list:
        if show_stderr:
            sys.stderr.write(f"Values in file are invalid\n")
        exit_number = 2
        return exit_number
    
    is_first_line = True
    full_text = []
    exit_number = 0

    for line in text_csv:
        line_index = text_csv.index(line)
        line = line[:-1]
        if is_first_line:
            line_first = line.split(',')
            is_first_line = False
        else:
            line = line.split(',')
            if len(line) != len(line_first):
                if show_stderr:
                    sys.stderr.write(f"csv file on row {line_index+1} are not full\n")
                exit_number = 1
            else:
                for item_index in range(len(line)):
                    try:
                        if "." in line[item_index]:
                            line[item_index] = float(line[item_index])
                        else:
                            line[item_index] = int(line[item_index])
                    except ValueError:
                        pass
                        # sys.stderr.write(f"Cannot convert {line[item_index]} to float because value is wrong\n")
                line_text = ''
                for name_index in range(len(line_first)-1):
                    line_text += [f'"{line_first[name_index]}": "{line[name_index]}", ', f'"{line_first[name_index]}": {line[name_index]}, '][type(line[name_index]) is float or type(line[name_index]) is int]
                line_text += [f'"{line_first[name_index+1]}": "{line[name_index+1]}"', f'"{line_first[name_index+1]}": {line[name_index+1]}'][type(line[name_index+1]) is float or type(line[name_index+1]) is int]
                full_text += [{line_text}]

    json_text = str(full_text)
    json_text = "".join(json_text.split("'"))
    if show_stdout:
        print(json_text)
    if receive_stdout:
        return exit_number, json_text
    return exit_number


if __name__ == '__main__':
    exit_number = transorm_from_csv_to_json()
    sys.exit(exit_number)
