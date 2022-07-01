<h2><a href="https://leetcode.com/problems/linked-list-cycle-ii/">142. Linked List Cycle II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">head</code> of a linked list, return <em style="user-select: auto;">the node where the cycle begins. If there is no cycle, return </em><code style="user-select: auto;">null</code>.</p>

<p style="user-select: auto;">There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the <code style="user-select: auto;">next</code> pointer. Internally, <code style="user-select: auto;">pos</code> is used to denote the index of the node that tail's <code style="user-select: auto;">next</code> pointer is connected to (<strong style="user-select: auto;">0-indexed</strong>). It is <code style="user-select: auto;">-1</code> if there is no cycle. <strong style="user-select: auto;">Note that</strong> <code style="user-select: auto;">pos</code> <strong style="user-select: auto;">is not passed as a parameter</strong>.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Do not modify</strong> the linked list.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="height: 145px; width: 450px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [3,2,0,-4], pos = 1
<strong style="user-select: auto;">Output:</strong> tail connects to node index 1
<strong style="user-select: auto;">Explanation:</strong> There is a cycle in the linked list, where tail connects to the second node.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 105px; width: 201px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1,2], pos = 0
<strong style="user-select: auto;">Output:</strong> tail connects to node index 0
<strong style="user-select: auto;">Explanation:</strong> There is a cycle in the linked list, where tail connects to the first node.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 65px; width: 65px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [1], pos = -1
<strong style="user-select: auto;">Output:</strong> no cycle
<strong style="user-select: auto;">Explanation:</strong> There is no cycle in the linked list.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of the nodes in the list is in the range <code style="user-select: auto;">[0, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= Node.val &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">pos</code> is <code style="user-select: auto;">-1</code> or a <strong style="user-select: auto;">valid index</strong> in the linked-list.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Can you solve it using <code style="user-select: auto;">O(1)</code> (i.e. constant) memory?</p>
</div>