"""Вимоги:
- реалізувати завдання згідно до вашого номеру в групі (якщо ваш номер 16 або 17, то відповідно берете 1 або 2)
- обов'язкове покриття програми юніт-тестами
- мова програмування на ваш смак
- якщо програма виконалась успішно, вона має повернути код виходу 0
- будь-які помилки в програмі мають писатися в stderr, а сама програма при цьому повертати будь-який ненульовий код виходу
"""

import sys

text_csv = sys.stdin.readlines()
is_first_line = True
full_text = []
for line in text_csv:
    line = line[:-1]
    if is_first_line:
        line_first = line.split(',')
        is_first_line = False
    else:
        line = line.split(',')
        for item_index in range(len(line)):
            try:
                line[item_index] = float(line[item_index])
            except TypeError and ValueError:
                pass
        line_text = ''
        for name_index in range(len(line_first)-1):
            line_text += [f'"{line_first[name_index]}": "{line[name_index]}", ', f'"{line_first[name_index]}": {line[name_index]}, '][type(line[name_index]) is float]
        line_text += [f'"{line_first[-1]}": "{line[-1]}"', f'"{line_first[-1]}": {line[-1]}'][type(line[-1]) is float]
        full_text += [{line_text}]

json_text = str(full_text)
json_text = "".join(json_text.split("'"))
print(json_text)

sys.exit(0)

# with open("test.txt", "w") as jsn:
#     jsn.write(json_text)
