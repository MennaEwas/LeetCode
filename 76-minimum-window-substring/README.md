<h2><a href="https://leetcode.com/problems/minimum-window-substring/">76. Minimum Window Substring</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two strings <code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code> of lengths <code style="user-select: auto;">m</code> and <code style="user-select: auto;">n</code> respectively, return <em style="user-select: auto;">the <strong style="user-select: auto;">minimum window substring</strong> of </em><code style="user-select: auto;">s</code><em style="user-select: auto;"> such that every character in </em><code style="user-select: auto;">t</code><em style="user-select: auto;"> (<strong style="user-select: auto;">including duplicates</strong>) is included in the window. If there is no such substring</em><em style="user-select: auto;">, return the empty string </em><code style="user-select: auto;">""</code><em style="user-select: auto;">.</em></p>

<p style="user-select: auto;">The testcases will be generated such that the answer is <strong style="user-select: auto;">unique</strong>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">substring</strong> is a contiguous sequence of characters within the string.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "ADOBECODEBANC", t = "ABC"
<strong style="user-select: auto;">Output:</strong> "BANC"
<strong style="user-select: auto;">Explanation:</strong> The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "a", t = "a"
<strong style="user-select: auto;">Output:</strong> "a"
<strong style="user-select: auto;">Explanation:</strong> The entire string s is the minimum window.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "a", t = "aa"
<strong style="user-select: auto;">Output:</strong> ""
<strong style="user-select: auto;">Explanation:</strong> Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == s.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == t.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n&nbsp;&lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code> consist of uppercase and lowercase English letters.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow up:</strong> Could you find an algorithm that runs in <code style="user-select: auto;">O(m + n)</code> time?</div>