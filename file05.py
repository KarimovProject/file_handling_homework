from re import S


def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    c = 0
    s = 0
    l = [c,s]
    for i in data:
        if i.isdigit():
            c+=1
        elif not(i.isdigit()):
            s += 1
        l = [c,s]
    return l
    
# Read data from file
file = open('txt_file/data05.txt','r')
data = file.read()
print(main(data))