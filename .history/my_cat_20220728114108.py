
def my_cat(*args):
    output = ""
    with open(*args, 'r') as file:
        file = file.read()
        output += file
    print(output)   

my_cat("test")    