def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for i in data.split(','):
        ans.append(int(i))
    return ans