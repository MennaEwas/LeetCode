<h2><a href="https://leetcode.com/problems/island-perimeter/">463. Island Perimeter</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given <code style="user-select: auto;">row x col</code> <code style="user-select: auto;">grid</code> representing a map where <code style="user-select: auto;">grid[i][j] = 1</code> represents&nbsp;land and <code style="user-select: auto;">grid[i][j] = 0</code> represents water.</p>

<p style="user-select: auto;">Grid cells are connected <strong style="user-select: auto;">horizontally/vertically</strong> (not diagonally). The <code style="user-select: auto;">grid</code> is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p style="user-select: auto;">The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
<strong style="user-select: auto;">Output:</strong> 16
<strong style="user-select: auto;">Explanation:</strong> The perimeter is the 16 yellow stripes in the image above.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1]]
<strong style="user-select: auto;">Output:</strong> 4
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> grid = [[1,0]]
<strong style="user-select: auto;">Output:</strong> 4
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">row == grid.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">col == grid[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= row, col &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">grid[i][j]</code> is <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
	<li style="user-select: auto;">There is exactly one island in <code style="user-select: auto;">grid</code>.</li>
</ul>
</div>