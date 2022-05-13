<h2><a href="https://leetcode.com/problems/add-two-numbers/">2. Add Two Numbers</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given two <strong style="user-select: auto;">non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong style="user-select: auto;">reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p style="user-select: auto;">You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong style="user-select: auto;">Output:</strong> [7,0,8]
<strong style="user-select: auto;">Explanation:</strong> 342 + 465 = 807.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> l1 = [0], l2 = [0]
<strong style="user-select: auto;">Output:</strong> [0]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong style="user-select: auto;">Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in each linked list is in the range <code style="user-select: auto;">[1, 100]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= Node.val &lt;= 9</code></li>
	<li style="user-select: auto;">It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>
</div>