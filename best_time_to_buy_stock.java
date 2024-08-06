class Solution {
    public int maxProfit(int[] prices) {
        int start = 0;
        int max = 0;
        int[] p = new int[prices.length];
        
        for (int i = 1; i < prices.length; ++i) { 
        	if (prices[i] - prices[start] > max) {
                p[i] = prices[i] - prices[start];
            }
        	start = prices[i] < prices[start]  ? i : start;
        }
        for (int x : p) {max = Math.max(max,  x);}
        return max;
    }
}