#  If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def my_funec(*kids):
    print("The youngest child is "+kids[2])

my_funec("John","Leonel","Toby")