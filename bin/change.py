import math

def main():
    # Check that the input from the user is a valid positive integer number.
    try:
        n = int(input("Enter a number: "))
    except:
        print("Invalid Input")
        return
    if n < 0:
        print("Invalid Input")
        return

    # Set the denominations of the coins
    c200 = 200
    c100 = 100
    c50 = 50
    c25 = 25
    c10 = 10
    c5 = 5
    c1 = 1
    output = [0, 0, 0, 0, 0, 0, 0]  # Empty array set. First column is 200, second 100, etc.
    '''
    Pseudocode
    We get a value in. Then we find the largest denomination that fits.
    Example: 0 0 0 0 1 2 5
    We then start from the right and subtract one from the denomination until everything in that column
    has been turned into the right column. We then subtract from the next highest denomination
    and repeat the process over again
    '''

    # Initialize the input array
    x = n/c200  # Check if greater that 200 cents
    if x >= 1:
        x = math.floor(x)  # Round down
        output[0] = x  # Set first index of array to number of 200 cent coins
        n = n - x * c200  # Subtract the total amount by the number of 200 cent coins that fit

    # Repeat the process with the remaining coins
    x = n / c100  # Check if greater that 100 cents
    if x >= 1:
        x = math.floor(x)  # Round down
        output[1] = x  # Set second index of array to number of 100 cent coins
        n = n - x * c100  # Subtract the total amount by the number of 100 cent coins that fit

    x = n / c50  # Check if greater that 50 cents
    if x >= 1:
        x = math.floor(x)  # Round down
        output[2] = x  # Set third index of array to number of 50 cent coins
        n = n - x * c50  # Subtract the total amount by the number of 50 cent coins that fit

    x = n / c25  # Check if greater that 25 cents
    if x >= 1:
        x = math.floor(x)  # Round down
        output[3] = x  # Set fourth index of array to number of 25 cent coins
        n = n - x * c25  # Subtract the total amount by the number of 25 cent coins that fit

    x = n / c10  # Check if greater that 10 cents
    if x >= 1:
        x = math.floor(x)  # Round down
        output[4] = x  # Set fifth index of array to number of 10 cent coins
        n = n - x * c10  # Subtract the total amount by the number of 10 cent coins that fit

    x = n / c5  # Check if greater that 5 cents
    if x >= 1:
        x = math.floor(x)  # Round down
        output[5] = x  # Set sixth index of array to number of 5 cent coins
        n = n - x * c5  # Subtract the total amount by the number of 5 cent coins that fit

    x = n  # The remaining coins are converted to 1 cent coins
    if x >= 1:
        output[6] = x  # Set seventh index of array to number of 1 cent coins
        n = n - x * c1  # Subtract the total amount by the number of 1 cent coins that fit
        if n != 0:
            print("Error with array initialization")
    print("Test")
    print(output)
    return

main()