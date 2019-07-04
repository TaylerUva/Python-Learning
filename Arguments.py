def fun_no_star(var1, var2, var3):
    print("\nReg test")
    print(var1)
    print(var2)
    print(var3)


def fun_one_star(*test):
    print("\n* test")
    print(test)


def fun_two_star(**kwargs):
    print("\n** test")
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


fun_two_star(test=1, test2="nothing")
fun_one_star("test=1", "test=2")
vars = ["yay", "this", "cool"]
fun_no_star(*vars)
