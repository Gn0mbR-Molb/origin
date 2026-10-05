name = input().strip()
parts = name.split()

sur = parts[0].capitalize()
ini1 = parts[1][0].upper()
ini2 = parts[2][0].upper()

print(f'{sur} {ini1}. {ini2}.')