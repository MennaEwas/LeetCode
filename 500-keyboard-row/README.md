<h2><a href="https://leetcode.com/problems/keyboard-row/">500. Keyboard Row</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of strings <code style="user-select: auto;">words</code>, return <em style="user-select: auto;">the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below</em>.</p>

<p style="user-select: auto;">In the <strong style="user-select: auto;">American keyboard</strong>:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">the first row consists of the characters <code style="user-select: auto;">"qwertyuiop"</code>,</li>
	<li style="user-select: auto;">the second row consists of the characters <code style="user-select: auto;">"asdfghjkl"</code>, and</li>
	<li style="user-select: auto;">the third row consists of the characters <code style="user-select: auto;">"zxcvbnm"</code>.</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/keyboard.png" style="width: 800px; max-width: 600px; height: 267px; user-select: auto;">
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> words = ["Hello","Alaska","Dad","Peace"]
<strong style="user-select: auto;">Output:</strong> ["Alaska","Dad"]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> words = ["omk"]
<strong style="user-select: auto;">Output:</strong> []
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> words = ["adsdf","sfd"]
<strong style="user-select: auto;">Output:</strong> ["adsdf","sfd"]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words.length &lt;= 20</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= words[i].length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">words[i]</code> consists of English letters (both lowercase and uppercase).&nbsp;</li>
</ul>
</div>