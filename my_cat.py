def my_cat(files):
    output = open(files, "r")
    print(output.read())
    output.close()

my_cat("js_test2.js")    