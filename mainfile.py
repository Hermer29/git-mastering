def add(a : int, b : int):
    return a+b
def add_str(a : str, b : str):
    return int(a) + int(b)

def sub(a : int, b : int):
    return a-b
def sub_str(a : str, b : str):
    return int(a)-int(b)

print(sub(add(5,add_str("7", "10")),sub_str("100","56"))
