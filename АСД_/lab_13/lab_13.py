with open('example.txt') as f:
    hash = {}
    for line in f:
        key, value = line.strip().split('.', 1)
        hash[key] = int(value)
