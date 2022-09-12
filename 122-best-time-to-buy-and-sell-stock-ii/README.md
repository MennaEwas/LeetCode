<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/">122. Best Time to Buy and Sell Stock II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">prices</code> where <code style="user-select: auto;">prices[i]</code> is the price of a given stock on the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> day.</p>

<p style="user-select: auto;">On each day, you may decide to buy and/or sell the stock. You can only hold <strong style="user-select: auto;">at most one</strong> share of the stock at any time. However, you can buy it then immediately sell it on the <strong style="user-select: auto;">same day</strong>.</p>

<p style="user-select: auto;">Find and return <em style="user-select: auto;">the <strong style="user-select: auto;">maximum</strong> profit you can achieve</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> prices = [7,1,5,3,6,4]
<strong style="user-select: auto;">Output:</strong> 7
<strong style="user-select: auto;">Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> prices = [1,2,3,4,5]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> prices = [7,6,4,3,1]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= prices.length &lt;= 3 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= prices[i] &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>