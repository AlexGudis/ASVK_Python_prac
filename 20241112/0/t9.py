while True:
    try:
        s = int(input())
        break
    except Exception as e:
        print(e.args)