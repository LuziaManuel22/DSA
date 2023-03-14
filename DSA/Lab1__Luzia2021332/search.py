
def searchKey(arr, key):
    row = 0
    col = len(arr[row]) - 1

    while (row < len(arr) and col >= 0):

        if (arr[row][col] == key):

            return True
 
        if (arr[row][col] < key):

            row += 1
        else:

            col -= 1
    return False 
if __name__ == '__main__':
    arr = [[1, 3, 5],["ancvd", "ancr", "vd"]]
    ans = searchKey(arr, 5)
    print(ans)
 
