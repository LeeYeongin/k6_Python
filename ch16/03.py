try:
    with open('c.csv', 'r') as f:
        for line in f:
            print(line)
except Exception as e:
    pass
    # print(e)