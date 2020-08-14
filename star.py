limit=int(input("ENTER THE NUMBER OF ROWS :"))
row=1
space=limit
while row<=limit:
    print(space*(" ")+row*("* "))
    row=row+1
    space=space-1


  