for row in range(1,10):
    for col in range(1,10):
        prod=row*col
        if col<10:
            print("",prod,"",end="")
        else:
            print(prod,"",end="")
