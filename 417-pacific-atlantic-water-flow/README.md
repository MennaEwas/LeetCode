<h2><a href="https://leetcode.com/problems/pacific-atlantic-water-flow/">417. Pacific Atlantic Water Flow</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is an <code style="user-select: auto;">m x n</code> rectangular island that borders both the <strong style="user-select: auto;">Pacific Ocean</strong> and <strong style="user-select: auto;">Atlantic Ocean</strong>. The <strong style="user-select: auto;">Pacific Ocean</strong> touches the island's left and top edges, and the <strong style="user-select: auto;">Atlantic Ocean</strong> touches the island's right and bottom edges.</p>

<p style="user-select: auto;">The island is partitioned into a grid of square cells. You are given an <code style="user-select: auto;">m x n</code> integer matrix <code style="user-select: auto;">heights</code> where <code style="user-select: auto;">heights[r][c]</code> represents the <strong style="user-select: auto;">height above sea level</strong> of the cell at coordinate <code style="user-select: auto;">(r, c)</code>.</p>

<p style="user-select: auto;">The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is <strong style="user-select: auto;">less than or equal to</strong> the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">a <strong style="user-select: auto;">2D list</strong> of grid coordinates </em><code style="user-select: auto;">result</code><em style="user-select: auto;"> where </em><code style="user-select: auto;">result[i] = [r<sub style="user-select: auto;">i</sub>, c<sub style="user-select: auto;">i</sub>]</code><em style="user-select: auto;"> denotes that rain water can flow from cell </em><code style="user-select: auto;">(r<sub style="user-select: auto;">i</sub>, c<sub style="user-select: auto;">i</sub>)</code><em style="user-select: auto;"> to <strong style="user-select: auto;">both</strong> the Pacific and Atlantic oceans</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" style="width: 573px; height: 573px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
<strong style="user-select: auto;">Output:</strong> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> heights = [[2,1],[1,2]]
<strong style="user-select: auto;">Output:</strong> [[0,0],[0,1],[1,0],[1,1]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">m == heights.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == heights[r].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= heights[r][c] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>