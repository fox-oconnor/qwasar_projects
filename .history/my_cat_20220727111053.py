import glob
def my_cat(*args):
    final_output = ""
    for item in args:
        print(item)
        item = glob.glob(item)
        with open(item) as output:
            output = output.read()
            final_output += output
    print(final_output)                   


        
   
    

my_cat("test")    