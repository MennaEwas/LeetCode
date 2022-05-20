<h2><a href="https://leetcode.com/problems/valid-parentheses/">20. Valid Parentheses</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code> containing just the characters <code style="user-select: auto;">'('</code>, <code style="user-select: auto;">')'</code>, <code style="user-select: auto;">'{'</code>, <code style="user-select: auto;">'}'</code>, <code style="user-select: auto;">'['</code> and <code style="user-select: auto;">']'</code>, determine if the input string is valid.</p>

<p style="user-select: auto;">An input string is valid if:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">Open brackets must be closed by the same type of brackets.</li>
	<li style="user-select: auto;">Open brackets must be closed in the correct order.</li>
</ol>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "()"
<strong style="user-select: auto;">Output:</strong> true
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "()[]{}"
<strong style="user-select: auto;">Output:</strong> true
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "(]"
<strong style="user-select: auto;">Output:</strong> false
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of parentheses only <code style="user-select: auto;">'()[]{}'</code>.</li>
</ul>
</div>