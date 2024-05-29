class MyClass:
    def __init__(self, name) -> None:
        self.name = name

    def greet(self):
        print(f"Hello {self.name}!")

def addFunc(x, y):
    return x + y

print(__name__)

if __name__ == "__main__":
    addFunc(2,3)    

