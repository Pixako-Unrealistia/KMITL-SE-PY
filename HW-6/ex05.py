
k = int(input("Enter something: "))
lst = [1000,500,100,50,20,10,5,2,1]

while k > 0:
    if k < lst[0]:
        print(f"0-{lst[0]}-Baht notes")
    lst = lst.pop(0)
