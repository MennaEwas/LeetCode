<h2><a href="https://leetcode.com/problems/valid-palindrome/">125. Valid Palindrome</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A phrase is a <strong style="user-select: auto;">palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if it is a <strong style="user-select: auto;">palindrome</strong>, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> otherwise</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "A man, a plan, a canal: Panama"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> "amanaplanacanalpanama" is a palindrome.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "race a car"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> "raceacar" is not a palindrome.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = " "
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 2 * 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists only of printable ASCII characters.</li>
</ul>
</div>