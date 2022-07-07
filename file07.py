def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x = []
    i = 0
    while i <len(data):
        if data[i].isdigit():
            x.append(int(data[i]))
        i+=1
    return sum(x)
# Read data from file
data = open('txt_file/data07.txt')
x = data.read()
print(main(x))