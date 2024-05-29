class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def hello(self):
        return self.i

instance = Complex("hello", 22)
print("インスタンス", instance.hello())
