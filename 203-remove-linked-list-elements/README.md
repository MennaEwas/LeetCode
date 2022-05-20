<h2><a href="https://leetcode.com/problems/remove-linked-list-elements/">203. Remove Linked List Elements</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">head</code> of a linked list and an integer <code style="user-select: auto;">val</code>, remove all the nodes of the linked list that has <code style="user-select: auto;">Node.val == val</code>, and return <em style="user-select: auto;">the new head</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1,2,6,3,4,5,6], val = 6
<strong style="user-select: auto;">Output:</strong> [1,2,3,4,5]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [], val = 1
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [7,7,7,7], val = 7
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the list is in the range <code style="user-select: auto;">[0, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= Node.val &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= val &lt;= 50</code></li>
</ul>
</div>