<h2><a href="https://leetcode.com/problems/maximum-average-subarray-i/">643. Maximum Average Subarray I</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array <code style="user-select: auto;">nums</code> consisting of <code style="user-select: auto;">n</code> elements, and an integer <code style="user-select: auto;">k</code>.</p>

<p style="user-select: auto;">Find a contiguous subarray whose <strong style="user-select: auto;">length is equal to</strong> <code style="user-select: auto;">k</code> that has the maximum average value and return <em style="user-select: auto;">this value</em>. Any answer with a calculation error less than <code style="user-select: auto;">10<sup style="user-select: auto;">-5</sup></code> will be accepted.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,12,-5,-6,50,3], k = 4
<strong style="user-select: auto;">Output:</strong> 12.75000
<strong style="user-select: auto;">Explanation:</strong> Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [5], k = 1
<strong style="user-select: auto;">Output:</strong> 5.00000
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == nums.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= n &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">4</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>