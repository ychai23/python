#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(prices):
    """ returns the average price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    sum1 = 0
    for i in range(len(prices)):
        sum1 += prices[i]
    return sum1 / len(prices)

def std_dev(prices):
    """ returns the standard deviation price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    din = 0
    for i in range(len(prices)):
        din += (prices[i] - avg_price(prices)) ** 2
    return (din / len(prices)) ** 0.5

def max_day(prices):
    """ returns the day with the maximum price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    maxday = 0
    for i in range(len(prices)):
        if prices[maxday] < prices[i]:
            maxday = i
    return maxday

def any_below(prices, threshold):
    """ determine if there are any prices below that threshold.
        input prices: prices is a list of 1 or more numbers.
        input threthold: the threshold price
    """
    for i in range(len(prices)):
        if prices[i] < threshold:
            return True
    return False


                
def find_plan(prices):
    """ find the best days on which to buy and sell the stock whose prices are given in the list of prices and return the buy day, sell day and the profit it earns.
        input: prices is a list of 1 or more numbers.
    """
    diff = prices[1] - prices[0]
    for i in range(len(prices)):
        for n in range(i,len(prices)):
            if diff < prices[n] - prices[i]:
                diff = prices[n] - prices[i]
                pos1 = i
                pos2 = n
    return [pos1, pos2, diff]
        
def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            stdev = std_dev(prices)
            print('The standard deviation is', stdev)
        elif choice == 5:
            maxday = max_day(prices)
            print('The max price is', str(prices[maxday]), 'on day', str(maxday))
        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            bol = any_below(prices, threshold)
            if bol == True:
                print("There is at least one price below", threshold)
            else:
                print("There are no prices below", threshold)
        elif choice == 7:
            final = find_plan(prices)
            print("Buy on day", final[0], "at price", prices[final[0]])
            print("Sell on day", final[1], "at price", prices[final[1]])
            print("Total profit:", final[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
