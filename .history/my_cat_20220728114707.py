
def my_cat(*args):
    output = ""
    with open(*args) as file:
        file = file.read()
        output = file
    print(output)   

my_cat("test.txt", "test.txt")    