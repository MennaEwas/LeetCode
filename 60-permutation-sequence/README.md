<h2><a href="https://leetcode.com/problems/permutation-sequence/">60. Permutation Sequence</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">The set <code style="user-select: auto;">[1, 2, 3, ...,&nbsp;n]</code> contains a total of <code style="user-select: auto;">n!</code> unique permutations.</p>

<p style="user-select: auto;">By listing and labeling all of the permutations in order, we get the following sequence for <code style="user-select: auto;">n = 3</code>:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">"123"</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">"132"</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">"213"</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">"231"</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">"312"</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">"321"</code></li>
</ol>

<p style="user-select: auto;">Given <code style="user-select: auto;">n</code> and <code style="user-select: auto;">k</code>, return the <code style="user-select: auto;">k<sup style="user-select: auto;">th</sup></code> permutation sequence.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 3, k = 3
<strong style="user-select: auto;">Output:</strong> "213"
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 4, k = 9
<strong style="user-select: auto;">Output:</strong> "2314"
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 3, k = 1
<strong style="user-select: auto;">Output:</strong> "123"
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 9</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= n!</code></li>
</ul>
</div>