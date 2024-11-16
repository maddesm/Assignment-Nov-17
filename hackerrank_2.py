# Hackkerrank 2 : Mark and Toys
#Each toy can be purchased only once.
# Sort the list of toy prices.

def maximumToys(prices, k):
    prices.sort() 
    count = 0
    
    for price in prices:
        if k >= price:
            k -= price
            count += 1
        else:
            break
            
    return count

if __name__ == "__main__":
    _, k = map(int, input().split())
    prices = list(map(int, input().split()))
    print(maximumToys(prices, k))
