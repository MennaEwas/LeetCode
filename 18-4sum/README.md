<h2><a href="https://leetcode.com/problems/4sum/">18. 4Sum</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array <code style="user-select: auto;">nums</code> of <code style="user-select: auto;">n</code> integers, return <em style="user-select: auto;">an array of all the <strong style="user-select: auto;">unique</strong> quadruplets</em> <code style="user-select: auto;">[nums[a], nums[b], nums[c], nums[d]]</code> such that:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= a, b, c, d&nbsp;&lt; n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">a</code>, <code style="user-select: auto;">b</code>, <code style="user-select: auto;">c</code>, and <code style="user-select: auto;">d</code> are <strong style="user-select: auto;">distinct</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[a] + nums[b] + nums[c] + nums[d] == target</code></li>
</ul>

<p style="user-select: auto;">You may return the answer in <strong style="user-select: auto;">any order</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,0,-1,0,-2,2], target = 0
<strong style="user-select: auto;">Output:</strong> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,2,2,2,2], target = 8
<strong style="user-select: auto;">Output:</strong> [[2,2,2,2]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= target &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>