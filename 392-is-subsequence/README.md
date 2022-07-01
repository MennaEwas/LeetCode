<h2><a href="https://leetcode.com/problems/is-subsequence/">392. Is Subsequence</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two strings <code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if </em><code style="user-select: auto;">s</code><em style="user-select: auto;"> is a <strong style="user-select: auto;">subsequence</strong> of </em><code style="user-select: auto;">t</code><em style="user-select: auto;">, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> otherwise</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code style="user-select: auto;">"ace"</code> is a subsequence of <code style="user-select: auto;">"<u style="user-select: auto;">a</u>b<u style="user-select: auto;">c</u>d<u style="user-select: auto;">e</u>"</code> while <code style="user-select: auto;">"aec"</code> is not).</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abc", t = "ahbgdc"
<strong style="user-select: auto;">Output:</strong> true
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "axc", t = "ahbgdc"
<strong style="user-select: auto;">Output:</strong> false
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= s.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= t.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code> consist only of lowercase English letters.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow up:</strong> Suppose there are lots of incoming <code style="user-select: auto;">s</code>, say <code style="user-select: auto;">s<sub style="user-select: auto;">1</sub>, s<sub style="user-select: auto;">2</sub>, ..., s<sub style="user-select: auto;">k</sub></code> where <code style="user-select: auto;">k &gt;= 10<sup style="user-select: auto;">9</sup></code>, and you want to check one by one to see if <code style="user-select: auto;">t</code> has its subsequence. In this scenario, how would you change your code?</div>