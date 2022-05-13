<h2><a href="https://leetcode.com/problems/palindrome-number/">9. Palindrome Number</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer <code style="user-select: auto;">x</code>, return <code style="user-select: auto;">true</code> if <code style="user-select: auto;">x</code> is palindrome integer.</p>

<p style="user-select: auto;">An integer is a <strong style="user-select: auto;">palindrome</strong> when it reads the same backward as forward.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, <code style="user-select: auto;">121</code> is a palindrome while <code style="user-select: auto;">123</code> is not.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> x = 121
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> x = -121
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> x = 10
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">-2<sup style="user-select: auto;">31</sup>&nbsp;&lt;= x &lt;= 2<sup style="user-select: auto;">31</sup>&nbsp;- 1</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow up:</strong> Could you solve it without converting the integer to a string?</div>