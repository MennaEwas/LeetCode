<h2><a href="https://leetcode.com/problems/isomorphic-strings/">205. Isomorphic Strings</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two strings <code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code>, <em style="user-select: auto;">determine if they are isomorphic</em>.</p>

<p style="user-select: auto;">Two strings <code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code> are isomorphic if the characters in <code style="user-select: auto;">s</code> can be replaced to get <code style="user-select: auto;">t</code>.</p>

<p style="user-select: auto;">All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "egg", t = "add"
<strong style="user-select: auto;">Output:</strong> true
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "foo", t = "bar"
<strong style="user-select: auto;">Output:</strong> false
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "paper", t = "title"
<strong style="user-select: auto;">Output:</strong> true
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 5 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">t.length == s.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code> consist of any valid ascii character.</li>
</ul>
</div>