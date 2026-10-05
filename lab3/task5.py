data = input()
print(f'Длина: {len(data)}')
print(f'Только буквы: {data.isalpha()}')
print(f'Только цифры: {data.isdigit()}')
print(f'Только цифренно-цифровая: {data.isalnum()}')
print(f'Содержит дефис: {"-" in data}')


