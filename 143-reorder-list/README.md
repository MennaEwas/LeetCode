<h2><a href="https://leetcode.com/problems/reorder-list/">143. Reorder List</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given the head of a singly linked-list. The list can be represented as:</p>

<pre style="user-select: auto;">L<sub style="user-select: auto;">0</sub> → L<sub style="user-select: auto;">1</sub> → … → L<sub style="user-select: auto;">n - 1</sub> → L<sub style="user-select: auto;">n</sub>
</pre>

<p style="user-select: auto;"><em style="user-select: auto;">Reorder the list to be on the following form:</em></p>

<pre style="user-select: auto;">L<sub style="user-select: auto;">0</sub> → L<sub style="user-select: auto;">n</sub> → L<sub style="user-select: auto;">1</sub> → L<sub style="user-select: auto;">n - 1</sub> → L<sub style="user-select: auto;">2</sub> → L<sub style="user-select: auto;">n - 2</sub> → …
</pre>

<p style="user-select: auto;">You may not modify the values in the list's nodes. Only nodes themselves may be changed.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 422px; height: 222px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1,2,3,4]
<strong style="user-select: auto;">Output:</strong> [1,4,2,3]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 542px; height: 222px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1,2,3,4,5]
<strong style="user-select: auto;">Output:</strong> [1,5,2,4,3]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the list is in the range <code style="user-select: auto;">[1, 5 * 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= Node.val &lt;= 1000</code></li>
</ul>
</div>