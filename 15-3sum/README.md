<h2><a href="https://leetcode.com/problems/3sum/">15. 3Sum</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array nums, return all the triplets <code style="user-select: auto;">[nums[i], nums[j], nums[k]]</code> such that <code style="user-select: auto;">i != j</code>, <code style="user-select: auto;">i != k</code>, and <code style="user-select: auto;">j != k</code>, and <code style="user-select: auto;">nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p style="user-select: auto;">Notice that the solution set must not contain duplicate triplets.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong style="user-select: auto;">Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong style="user-select: auto;">Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [0,1,1]
<strong style="user-select: auto;">Output:</strong> []
<strong style="user-select: auto;">Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [0,0,0]
<strong style="user-select: auto;">Output:</strong> [[0,0,0]]
<strong style="user-select: auto;">Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">3 &lt;= nums.length &lt;= 3000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>