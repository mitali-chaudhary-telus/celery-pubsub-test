
from sample import add, hello

if __name__ == "__main__":
    # Sending here--- some tasks to the worker
    print("Sending task: add(2, 2)")
    add.delay(2, 2)
    
    print("Sending task: hello('World')")
    hello.delay("World")
    
    print("Tasks have been sent to the worker!")
    print("Check the worker terminal to see the results.")