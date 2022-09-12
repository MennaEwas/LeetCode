<h2><a href="https://leetcode.com/problems/shortest-unsorted-continuous-subarray/">581. Shortest Unsorted Continuous Subarray</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code>, you need to find one <b style="user-select: auto;">continuous subarray</b> that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the shortest such subarray and output its length</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,6,4,8,10,9,15]
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation:</strong> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3,4]
<strong style="user-select: auto;">Output:</strong> 0
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1]
<strong style="user-select: auto;">Output:</strong> 0
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow up:</strong> Can you solve it in <code style="user-select: auto;">O(n)</code> time complexity?</div>