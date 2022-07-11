<h2><a href="https://leetcode.com/problems/maximum-69-number/">1323. Maximum 69 Number</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a positive integer <code style="user-select: auto;">num</code> consisting only of digits <code style="user-select: auto;">6</code> and <code style="user-select: auto;">9</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the maximum number you can get by changing <strong style="user-select: auto;">at most</strong> one digit (</em><code style="user-select: auto;">6</code><em style="user-select: auto;"> becomes </em><code style="user-select: auto;">9</code><em style="user-select: auto;">, and </em><code style="user-select: auto;">9</code><em style="user-select: auto;"> becomes </em><code style="user-select: auto;">6</code><em style="user-select: auto;">)</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> num = 9669
<strong style="user-select: auto;">Output:</strong> 9969
<strong style="user-select: auto;">Explanation:</strong> 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> num = 9996
<strong style="user-select: auto;">Output:</strong> 9999
<strong style="user-select: auto;">Explanation:</strong> Changing the last digit 6 to 9 results in the maximum number.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> num = 9999
<strong style="user-select: auto;">Output:</strong> 9999
<strong style="user-select: auto;">Explanation:</strong> It is better not to apply any change.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= num &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">num</code>&nbsp;consists of only <code style="user-select: auto;">6</code> and <code style="user-select: auto;">9</code> digits.</li>
</ul>
</div>