<h2><a href="https://leetcode.com/problems/set-matrix-zeroes/">73. Set Matrix Zeroes</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an <code style="user-select: auto;">m x n</code> integer matrix <code style="user-select: auto;">matrix</code>, if an element is <code style="user-select: auto;">0</code>, set its entire row and column to <code style="user-select: auto;">0</code>'s.</p>

<p style="user-select: auto;">You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" style="user-select: auto;">in place</a>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" style="width: 450px; height: 169px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> matrix = [[1,1,1],[1,0,1],[1,1,1]]
<strong style="user-select: auto;">Output:</strong> [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" style="width: 450px; height: 137px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
<strong style="user-select: auto;">Output:</strong> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == matrix.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == matrix[0].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-2<sup style="user-select: auto;">31</sup> &lt;= matrix[i][j] &lt;= 2<sup style="user-select: auto;">31</sup> - 1</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">A straightforward solution using <code style="user-select: auto;">O(mn)</code> space is probably a bad idea.</li>
	<li style="user-select: auto;">A simple improvement uses <code style="user-select: auto;">O(m + n)</code> space, but still not the best solution.</li>
	<li style="user-select: auto;">Could you devise a constant space solution?</li>
</ul>
</div>