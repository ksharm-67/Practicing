#include <iostream>
#include <vector>

using namespace std;

//Given an array prices where prices[i] is the price of a given stock on the ith day, 
//you want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell 

//Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

int maxProfit(vector<int>& prices) {
    int minPrice = prices[0];
    int profit = 0;

    for(int i = 1; i < prices.size(); i++){             //Checks min value
        
        if(prices[i] < minPrice){
            minPrice = prices[i];                       //Sets the value you should buy for
        }

        if(prices[i] - minPrice > profit){              //Checks if profit if we sold today is greater than previous profit
            profit = prices[i] - minPrice;
        }
    }
    return profit;
}

int main(){
    
    //Change prices to prices of a stock 
    vector<int> prices = {7,1,5,3,6,4};
   
    cout << "Maximum profit you can achieve is: " << maxProfit(prices) << endl;

    return 0;
}
