with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
    print(len(content.split()))
