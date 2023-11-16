def print_out(a):
    print("Outer: {}".format(a))

    def print_in():
        print("\tInnter: {}".format(a))

    return print_in

test2 = print_out("test")

del print_out

test2()

print(print_out("test2"))
