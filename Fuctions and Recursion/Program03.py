# Default parameter value

def greet(name='Stranger'):
    gr =print("Hello, " + name)
    return gr

greet('Sahil')  # name will be 'Sahil' in the function body(passed)
greet()   # # name will be 'Stranger' in the function body(default)