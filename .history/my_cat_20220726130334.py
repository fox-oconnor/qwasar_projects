def my_cat(*args):
    output = ""
    for item in args:
        with open(item) as output:
            output = output.read()
            output = output.write()

        print(data)             
        
   
    

my_cat("test.txt")    