def show_stars(rows):
   for i in range(0,rows):
       for j in range(0,i+1):
           print("*",end ="")
           
        print("\r")

print(show_stars(5))
