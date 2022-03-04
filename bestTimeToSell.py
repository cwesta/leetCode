"""
you are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104


"""


"""
    Input: prices = [7,1,5,3,6,4]
    
    find lowest price first, then find highest price
    if price trends down return 0 since there is no max profit available
    
    
    [7,3,5,1,6,4]
      ^
        ^
      L R
      if the 
    


"""

    
def buyLowSellHigh(arr):
  
  l, r = 0, 1
  maxP = 0
  # Remeber this is to calculate the MAX Profit between two dates
  # L = buy low and R = Sell High
  # how do you calculate that? there is a function you can use native to python to find it
  while l < r:
    if arr[l] < arr[r]:
      pass
    else:
      pass
    
      
  return maxP




prices = [7,1,5,3,6,4]

buyLowSellHigh(prices)

