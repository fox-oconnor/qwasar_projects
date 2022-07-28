
def my_cat(*args):
    output = ""
    with open(*args, 'r') as file:
        file = file.read()
        output = output +  file
    print(output)   

my_cat("test.txt", "test.txt")    