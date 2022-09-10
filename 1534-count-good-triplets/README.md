<h2><a href="https://leetcode.com/problems/count-good-triplets/">1534. Count Good Triplets</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of integers <code style="user-select: auto;">arr</code>, and three integers&nbsp;<code style="user-select: auto;">a</code>,&nbsp;<code style="user-select: auto;">b</code>&nbsp;and&nbsp;<code style="user-select: auto;">c</code>. You need to find the number of good triplets.</p>

<p style="user-select: auto;">A triplet <code style="user-select: auto;">(arr[i], arr[j], arr[k])</code>&nbsp;is <strong style="user-select: auto;">good</strong> if the following conditions are true:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= i &lt; j &lt; k &lt;&nbsp;arr.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">|arr[i] - arr[j]| &lt;= a</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">|arr[j] - arr[k]| &lt;= b</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">|arr[i] - arr[k]| &lt;= c</code></li>
</ul>

<p style="user-select: auto;">Where <code style="user-select: auto;">|x|</code> denotes the absolute value of <code style="user-select: auto;">x</code>.</p>

<p style="user-select: auto;">Return<em style="user-select: auto;"> the number of good triplets</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong>&nbsp;There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,1,2,2,3], a = 0, b = 0, c = 1
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation: </strong>No triplet satisfies all conditions.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">3 &lt;= arr.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= arr[i] &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= a, b, c &lt;= 1000</code></li>
</ul></div>