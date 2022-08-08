<h2><a href="https://leetcode.com/problems/minimum-operations-to-convert-number/">2059. Minimum Operations to Convert Number</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a <strong style="user-select: auto;">0-indexed</strong> integer array <code style="user-select: auto;">nums</code> containing <strong style="user-select: auto;">distinct</strong> numbers, an integer <code style="user-select: auto;">start</code>, and an integer <code style="user-select: auto;">goal</code>. There is an integer <code style="user-select: auto;">x</code> that is initially set to <code style="user-select: auto;">start</code>, and you want to perform operations on <code style="user-select: auto;">x</code> such that it is converted to <code style="user-select: auto;">goal</code>. You can perform the following operation repeatedly on the number <code style="user-select: auto;">x</code>:</p>

<p style="user-select: auto;">If <code style="user-select: auto;">0 &lt;= x &lt;= 1000</code>, then for any index <code style="user-select: auto;">i</code> in the array (<code style="user-select: auto;">0 &lt;= i &lt; nums.length</code>), you can set <code style="user-select: auto;">x</code> to any of the following:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">x + nums[i]</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">x - nums[i]</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">x ^ nums[i]</code> (bitwise-XOR)</li>
</ul>

<p style="user-select: auto;">Note that you can use each <code style="user-select: auto;">nums[i]</code> any number of times in any order. Operations that set <code style="user-select: auto;">x</code> to be out of the range <code style="user-select: auto;">0 &lt;= x &lt;= 1000</code> are valid, but no more operations can be done afterward.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">minimum</strong> number of operations needed to convert </em><code style="user-select: auto;">x = start</code><em style="user-select: auto;"> into </em><code style="user-select: auto;">goal</code><em style="user-select: auto;">, and </em><code style="user-select: auto;">-1</code><em style="user-select: auto;"> if it is not possible</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,4,12], start = 2, goal = 12
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> We can go from 2 → 14 → 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [3,5,7], start = 0, goal = -4
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> We can go from 0 → 3 → -4 with the following 2 operations. 
- 0 + 3 = 3
- 3 - 7 = -4
Note that the last operation sets x out of the range 0 &lt;= x &lt;= 1000, which is valid.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,8,16], start = 0, goal = 1
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong> There is no way to convert 0 into 1.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= nums[i], goal &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= start &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">start != goal</code></li>
	<li style="user-select: auto;">All the integers in <code style="user-select: auto;">nums</code> are distinct.</li>
</ul>
</div>