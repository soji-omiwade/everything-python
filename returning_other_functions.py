def is_called(n):
    """closure functions"""
    def is_returned():
        print("Hello", n)
    return is_returned

new = is_called(42)
#Outputs "Hello"
new()


