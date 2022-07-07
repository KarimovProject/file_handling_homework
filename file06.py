def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = []
    i = 0
    while i <len(data):
        if data[i].isdigit():
            x.append(int(data[i]))
        i+=1
    return x
# Read data from file
data = open('txt_file/data03.txt')
x = data.read()
print(main(x))