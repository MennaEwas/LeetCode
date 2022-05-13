<h2><a href="https://leetcode.com/problems/rectangle-overlap/">836. Rectangle Overlap</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">An axis-aligned rectangle is represented as a list <code style="user-select: auto;">[x1, y1, x2, y2]</code>, where <code style="user-select: auto;">(x1, y1)</code> is the coordinate of its bottom-left corner, and <code style="user-select: auto;">(x2, y2)</code> is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.</p>

<p style="user-select: auto;">Two rectangles overlap if the area of their intersection is <strong style="user-select: auto;">positive</strong>. To be clear, two rectangles that only touch at the corner or edges do not overlap.</p>

<p style="user-select: auto;">Given two axis-aligned rectangles <code style="user-select: auto;">rec1</code> and <code style="user-select: auto;">rec2</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if they overlap, otherwise return </em><code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> rec1 = [0,0,2,2], rec2 = [1,1,3,3]
<strong style="user-select: auto;">Output:</strong> true
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> rec1 = [0,0,1,1], rec2 = [1,0,2,1]
<strong style="user-select: auto;">Output:</strong> false
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> rec1 = [0,0,1,1], rec2 = [2,2,3,3]
<strong style="user-select: auto;">Output:</strong> false
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">rect1.length == 4</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">rect2.length == 4</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= rec1[i], rec2[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">rec1</code> and <code style="user-select: auto;">rec2</code> represent a valid rectangle with a non-zero area.</li>
</ul>
</div>