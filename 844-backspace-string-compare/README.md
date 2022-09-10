<h2><a href="https://leetcode.com/problems/backspace-string-compare/">844. Backspace String Compare</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two strings <code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code>, return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if they are equal when both are typed into empty text editors</em>. <code style="user-select: auto;">'#'</code> means a backspace character.</p>

<p style="user-select: auto;">Note that after backspacing an empty text, the text will continue empty.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "ab#c", t = "ad#c"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Both s and t become "ac".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "ab##", t = "c#d#"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> Both s and t become "".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "a#c", t = "b"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> s becomes "c" while t becomes "b".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;"><span style="user-select: auto;">1 &lt;= s.length, t.length &lt;= 200</span></code></li>
	<li style="user-select: auto;"><span style="user-select: auto;"><code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code> only contain lowercase letters and <code style="user-select: auto;">'#'</code> characters.</span></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Can you solve it in <code style="user-select: auto;">O(n)</code> time and <code style="user-select: auto;">O(1)</code> space?</p>
</div>