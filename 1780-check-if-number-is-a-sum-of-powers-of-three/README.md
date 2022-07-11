<h2><a href="https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/">1780. Check if Number is a Sum of Powers of Three</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer <code style="user-select: auto;">n</code>, return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if it is possible to represent </em><code style="user-select: auto;">n</code><em style="user-select: auto;"> as the sum of distinct powers of three.</em> Otherwise, return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">An integer <code style="user-select: auto;">y</code> is a power of three if there exists an integer <code style="user-select: auto;">x</code> such that <code style="user-select: auto;">y == 3<sup style="user-select: auto;">x</sup></code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 12
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> 12 = 3<sup style="user-select: auto;">1</sup> + 3<sup style="user-select: auto;">2</sup>
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 91
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> 91 = 3<sup style="user-select: auto;">0</sup> + 3<sup style="user-select: auto;">2</sup> + 3<sup style="user-select: auto;">4</sup>
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 21
<strong style="user-select: auto;">Output:</strong> false
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">7</sup></code></li>
</ul>
</div>