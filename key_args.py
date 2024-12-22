# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                       The order of the argument doesn't matter, unlike positional arguments
#                       Python knows the names of the arguments that our function receive

def hello(first,middle,last):
    print("hello,",first,",",middle,",",last)

hello(middle = "prashh",last = "priya",first = "shubs")