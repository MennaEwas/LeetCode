<h2><a href="https://leetcode.com/problems/xor-operation-in-an-array/">1486. XOR Operation in an Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer <code style="user-select: auto;">n</code> and an integer <code style="user-select: auto;">start</code>.</p>

<p style="user-select: auto;">Define an array <code style="user-select: auto;">nums</code> where <code style="user-select: auto;">nums[i] = start + 2 * i</code> (<strong style="user-select: auto;">0-indexed</strong>) and <code style="user-select: auto;">n == nums.length</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the bitwise XOR of all elements of</em> <code style="user-select: auto;">nums</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 5, start = 0
<strong style="user-select: auto;">Output:</strong> 8
<strong style="user-select: auto;">Explanation:</strong> Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 4, start = 3
<strong style="user-select: auto;">Output:</strong> 8
<strong style="user-select: auto;">Explanation:</strong> Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= start &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == nums.length</code></li>
</ul>
</div>