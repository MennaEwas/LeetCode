<h2><a href="https://leetcode.com/problems/determine-color-of-a-chessboard-square/">1812. Determine Color of a Chessboard Square</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given <code style="user-select: auto;">coordinates</code>, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.</p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/screenshot-2021-02-20-at-22159-pm.png" style="width: 400px; height: 396px; user-select: auto;"></p>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if the square is white, and </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> if the square is black</em>.</p>

<p style="user-select: auto;">The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> coordinates = "a1"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> From the chessboard above, the square with coordinates "a1" is black, so return false.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> coordinates = "h3"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> From the chessboard above, the square with coordinates "h3" is white, so return true.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> coordinates = "c7"
<strong style="user-select: auto;">Output:</strong> false
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">coordinates.length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">'a' &lt;= coordinates[0] &lt;= 'h'</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">'1' &lt;= coordinates[1] &lt;= '8'</code></li>
</ul>
</div>