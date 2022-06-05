<h2><a href="https://leetcode.com/problems/sort-characters-by-frequency/">451. Sort Characters By Frequency</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, sort it in <strong style="user-select: auto;">decreasing order</strong> based on the <strong style="user-select: auto;">frequency</strong> of the characters. The <strong style="user-select: auto;">frequency</strong> of a character is the number of times it appears in the string.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the sorted string</em>. If there are multiple answers, return <em style="user-select: auto;">any of them</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "tree"
<strong style="user-select: auto;">Output:</strong> "eert"
<strong style="user-select: auto;">Explanation:</strong> 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "cccaaa"
<strong style="user-select: auto;">Output:</strong> "aaaccc"
<strong style="user-select: auto;">Explanation:</strong> Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "Aabb"
<strong style="user-select: auto;">Output:</strong> "bbAa"
<strong style="user-select: auto;">Explanation:</strong> "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 5 * 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of uppercase and lowercase English letters and digits.</li>
</ul>
</div>