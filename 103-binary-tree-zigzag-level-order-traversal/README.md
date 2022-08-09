<h2><a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/">103. Binary Tree Zigzag Level Order Traversal</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">root</code> of a binary tree, return <em style="user-select: auto;">the zigzag level order traversal of its nodes' values</em>. (i.e., from left to right, then right to left for the next level and alternate between).</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [3,9,20,null,null,15,7]
<strong style="user-select: auto;">Output:</strong> [[3],[20,9],[15,7]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1]
<strong style="user-select: auto;">Output:</strong> [[1]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = []
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[0, 2000]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-100 &lt;= Node.val &lt;= 100</code></li>
</ul>
</div>