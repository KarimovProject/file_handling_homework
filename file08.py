def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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
    return max(x)
# Read data from file
data = open('txt_file/data08.txt')
x = data.read()
print(main(x))