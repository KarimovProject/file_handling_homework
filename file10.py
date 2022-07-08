def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x = data.split('\n')
    s = []
    i = 0
    while i < len(x):
        s.append(len(x[i]))
        i += 1

    return max(s)
    
# Read data from file
f = open("txt_file/data10.txt").read()
print(main(f))