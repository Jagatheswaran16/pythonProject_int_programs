#Basically monkey patching is run time modification/dynamic modification
import monk


class A:
    def func(self):
        print("func() is being called")
def monkey_f(self):
	print ("monkey_f() is being called")


monk.A.func = monkey_f
obj = monk.A()


obj.func()
