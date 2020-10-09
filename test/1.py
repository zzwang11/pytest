import re
with open('exam1.txt', 'r', encoding='utf-8') as f:
    a = f.read()

b = re.sub(r'#[^\n]*', '', a)
print(b)

with open('exam2.txt', 'w+', encoding='utf-8') as f:
    f.write(b)

