count=0
for i in range(100):
    print(count)
    count=count+1
    if count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    else:
        print(count)

