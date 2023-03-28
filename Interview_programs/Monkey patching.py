#Basically monkey patching is run time modification/dynamic modification
import monk


class A:
    def func(self):
        print("func() is being called")


import monk


def monkey_f(self):
    print("monkey_f() is being called")


# replacing address of "func" with "monkey_f"
monk.A.func = monkey_f
obj = monk.A()

# calling function "func" whose address got replaced
# with function "monkey_f()"
obj.func()


