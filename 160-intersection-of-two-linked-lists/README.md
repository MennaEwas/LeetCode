<h2><a href="https://leetcode.com/problems/intersection-of-two-linked-lists/">160. Intersection of Two Linked Lists</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the heads of two singly linked-lists <code style="user-select: auto;">headA</code> and <code style="user-select: auto;">headB</code>, return <em style="user-select: auto;">the node at which the two lists intersect</em>. If the two linked lists have no intersection at all, return <code style="user-select: auto;">null</code>.</p>

<p style="user-select: auto;">For example, the following two linked lists begin to intersect at node <code style="user-select: auto;">c1</code>:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_statement.png" style="width: 500px; height: 162px; user-select: auto;">
<p style="user-select: auto;">The test cases are generated such that there are no cycles anywhere in the entire linked structure.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Note</strong> that the linked lists must <strong style="user-select: auto;">retain their original structure</strong> after the function returns.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Custom Judge:</strong></p>

<p style="user-select: auto;">The inputs to the <strong style="user-select: auto;">judge</strong> are given as follows (your program is <strong style="user-select: auto;">not</strong> given these inputs):</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">intersectVal</code> - The value of the node where the intersection occurs. This is <code style="user-select: auto;">0</code> if there is no intersected node.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">listA</code> - The first linked list.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">listB</code> - The second linked list.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">skipA</code> - The number of nodes to skip ahead in <code style="user-select: auto;">listA</code> (starting from the head) to get to the intersected node.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">skipB</code> - The number of nodes to skip ahead in <code style="user-select: auto;">listB</code> (starting from the head) to get to the intersected node.</li>
</ul>

<p style="user-select: auto;">The judge will then create the linked structure based on these inputs and pass the two heads, <code style="user-select: auto;">headA</code> and <code style="user-select: auto;">headB</code>&nbsp;to your program. If you correctly return the intersected node, then your solution will be <strong style="user-select: auto;">accepted</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" style="width: 500px; height: 162px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
<strong style="user-select: auto;">Output:</strong> Intersected at '8'
<strong style="user-select: auto;">Explanation:</strong> The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" style="width: 500px; height: 194px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
<strong style="user-select: auto;">Output:</strong> Intersected at '2'
<strong style="user-select: auto;">Explanation:</strong> The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png" style="width: 300px; height: 189px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
<strong style="user-select: auto;">Output:</strong> No intersection
<strong style="user-select: auto;">Explanation:</strong> From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes of <code style="user-select: auto;">listA</code> is in the <code style="user-select: auto;">m</code>.</li>
	<li style="user-select: auto;">The number of nodes of <code style="user-select: auto;">listB</code> is in the <code style="user-select: auto;">n</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 3 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= Node.val &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= skipA &lt;&nbsp;m</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= skipB &lt;&nbsp;n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">intersectVal</code> is <code style="user-select: auto;">0</code> if <code style="user-select: auto;">listA</code> and <code style="user-select: auto;">listB</code> do not intersect.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">intersectVal == listA[skipA] == listB[skipB]</code> if <code style="user-select: auto;">listA</code> and <code style="user-select: auto;">listB</code> intersect.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow up:</strong> Could you write a solution that runs in <code style="user-select: auto;">O(m + n)</code> time and use only <code style="user-select: auto;">O(1)</code> memory?</div>