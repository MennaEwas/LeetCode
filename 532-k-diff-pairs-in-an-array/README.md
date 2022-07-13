<h2><a href="https://leetcode.com/problems/k-diff-pairs-in-an-array/">532. K-diff Pairs in an Array</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of integers <code style="user-select: auto;">nums</code> and an integer <code style="user-select: auto;">k</code>, return <em style="user-select: auto;">the number of <b style="user-select: auto;">unique</b> k-diff pairs in the array</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">k-diff</strong> pair is an integer pair <code style="user-select: auto;">(nums[i], nums[j])</code>, where the following are true:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= i, j &lt; nums.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">i != j</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i] - nums[j] == k</code></li>
</ul>

<p style="user-select: auto;"><strong style="user-select: auto;">Notice</strong> that <code style="user-select: auto;">|val|</code> denotes the absolute value of <code style="user-select: auto;">val</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [3,1,4,1,5], k = 2
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of <strong style="user-select: auto;">unique</strong> pairs.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3,4,5], k = 1
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,3,1,5,4], k = 0
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> There is one 0-diff pair in the array, (1, 1).
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">7</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">7</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= k &lt;= 10<sup style="user-select: auto;">7</sup></code></li>
</ul>
</div>