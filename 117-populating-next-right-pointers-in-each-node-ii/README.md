<h2><a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/">117. Populating Next Right Pointers in Each Node II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a binary tree</p>

<pre style="user-select: auto;">struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
</pre>

<p style="user-select: auto;">Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code style="user-select: auto;">NULL</code>.</p>

<p style="user-select: auto;">Initially, all next pointers are set to <code style="user-select: auto;">NULL</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" style="width: 500px; height: 171px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,2,3,4,5,null,7]
<strong style="user-select: auto;">Output:</strong> [1,#,2,3,#,4,5,7,#]
<strong style="user-select: auto;">Explanation: </strong>Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = []
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[0, 6000]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow-up:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">You may only use constant extra space.</li>
	<li style="user-select: auto;">The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.</li>
</ul>
</div>