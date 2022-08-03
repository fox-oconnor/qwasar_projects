def my_cat(*args):
    output = ""
    for item in args:
        with open(item) as output:
            output = output.read()
    print(output)                   
        
   
    

my_cat("test.txt", "test.txt")    