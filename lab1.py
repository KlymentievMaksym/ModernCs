import sys
import json

from io import StringIO

io = StringIO()
result = StringIO()

text_csv = sys.stdin.readlines()
is_first_line = True
print()
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
            except TypeError:
                pass
        # print(line)
        print(*line_first, *line)
        for name_index in range(len(line_first)):
            json.dump({line_first[name_index]: line[name_index]}, io)
        print(io.getvalue())
        break
json.dump([io.getvalue()], result)
print(result.getvalue())
print()

# name,age\nJohn,30\nJane,25
# [{ "name": "John", "age": 30 }, { "name": "Jane", "age": 25 }]