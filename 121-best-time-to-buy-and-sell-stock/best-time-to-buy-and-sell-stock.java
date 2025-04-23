class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buy = prices[0];
        for(int price: prices){
            int sell = price;
            if(sell > buy) {
                profit = Math.max(profit,sell-buy);
            }
            else{
                buy = sell;
            }
        }
        return profit;
    }
}