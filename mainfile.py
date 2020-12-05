def add(a : int, b : int):
    return str(a+b)
def add_str(a : str, b : str):
    return str(int(a) + int(b))

def sub(a : int, b : int):
    return str(a-b)
def sub_str(a : str, b : str):
    return str(int(a)-int(b))

print(add(5,5)+add_str("66"+"1000"))
