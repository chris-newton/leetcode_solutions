class Solution {
    public int uniquePaths(int m, int n) {
        int degree = m + n - 2;
        int k = Math.min(m, n) - 1;
        double num = 1;
        
        for (int i = 1; i <= k; i++, degree--) {
            num = num * (degree) / i;
        }
       
        return (int) num;
    }
}