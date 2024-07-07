
def main():

    try:
        n = int(input("Enter a number: "))
    except:
        print("Invalid Input")
    if n < 0:
        print("Invalid Input")
        return

    c200 = 200
    c100 = 100
    c50 = 50
    c25 = 25
    c10 = 10
    c5 = 5
    c1 = 1
    output = []
    '''
    Pseudocode
    We get a value in. Then we find the largest denomination that fits.
    Example: 0 0 0 0 1 2 5
    We then start from the right and subtract one from the denomination until everything in that column
    has been turned into the right column. We then subtract from the next highest denomination
    and repeat the process over again
    '''



    print("Test")
    return
