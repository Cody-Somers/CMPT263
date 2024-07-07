import math

def main():
    # Check that the input from the user is a valid positive integer number.
    try:
        #n = int(input("Enter a number: "))
        n = 236 # Testing purposes. TODO: REMOVE THIS LINE
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
    print(output)  # First combination
    if output[0] != 0:
        twohundredCents(output)
    elif output[1] != 0:
        hundredCents(output)
    elif output[2] != 0:
        fiftyCents(output)
    elif output[3] != 0:
        twentyfiveCents(output)
    elif output[4] != 0:
        tenCents(output)
    else:
        fiveCents(output)
    print("Test")
    return


def fiveCents(output):
    for i in range(output[5]):
        output[5] = output[5] - 1  # Reduce the number of five cent coins
        output[6] = output[6] + 5  # add five since 1+1+1+1+1
        print(output)

def tenCents(output):
    temp = output.copy()  # Used to reset the array back
    fiveCents(output)
    output = temp.copy()  # Return the coins from their 1 cent current state
    for j in range(output[4]):
        output[4] = output[4] - 1  # Reduce ten cent coins
        output[5] = output[5] + 2  # add two since 5+5
        print(output)
        temp = output.copy()  # Used to reset the array back
        fiveCents(output)
        output = temp.copy()  # Return the coins from their 1 cent current state

def twentyfiveCents(output):
    temp = output.copy()  # Used to reset the array back
    tenCents(output)
    output = temp.copy()  # Return the coins from their 1 cent current state
    for k in range(output[3]):
        output[3] = output[3] - 1  # Reduce twenty-five cent coins
        output[4] = output[4] + 2  # add two since 25 = 10+10 + (5)
        output[5] = output[5] + 1  # add one since 25 = (10+10) + 5
        print(output)
        temp = output.copy()  # Used to reset the array back
        tenCents(output)
        output = temp.copy()  # Return the coins from their 1 cent current state

def fiftyCents(output):
    temp = output.copy()  # Used to reset the array back
    twentyfiveCents(output)
    output = temp.copy()  # Return the coins from their 1 cent current state
    for m in range(output[2]):
        output[2] = output[2] - 1  # Reduce the fifty cent coins
        output[3] = output[3] + 2  # add two since 50 = 25+25
        print(output)
        temp = output.copy()  # Used to reset the array back
        twentyfiveCents(output)
        output = temp.copy()  # Return the coins from their 1 cent current state

def hundredCents(output):
    temp = output.copy()  # Used to reset the array back
    fiftyCents(output)
    output = temp.copy()  # Return the coins from their 1 cent current state
    for n in range(output[1]):
        output[1] = output[1] - 1  # Reduce the hundred cent coins
        output[2] = output[2] + 2  # add two since 100 = 50+50
        print(output)
        temp = output.copy()  # Used to reset the array back
        fiftyCents(output)
        output = temp.copy()  # Return the coins from their 1 cent current state

def twohundredCents(output):
    temp = output.copy()  # Used to reset the array back
    hundredCents(output)
    output = temp.copy()  # Return the coins from their 1 cent current state
    for p in range(output[0]):
        output[0] = output[0] - 1  # Reduce the two-hundred cent coins
        output[1] = output[1] + 2  # add two since 200 = 100+100
        print(output)
        temp = output.copy()  # Used to reset the array back
        hundredCents(output)
        output = temp.copy()  # Return the coins from their 1 cent current state

main()