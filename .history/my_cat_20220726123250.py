def my_cat(files):
    output = open(files)
    print(output.read())
    output.close()

my_cat("text")    