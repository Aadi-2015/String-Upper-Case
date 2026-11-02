# Create a class
class IOSstring:
    # Create functions
    def __init__(self):
        self.str1 = ''
    def get_string(self):
        self.str1 = input('Enter a string: ')
    def print_string(self):
        print('Result is: ',self.str1.upper())
# Create an object
str1 = IOSstring()

# Call functions
str1.get_string()
str1.print_string()