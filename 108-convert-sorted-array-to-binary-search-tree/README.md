<h2><a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/">108. Convert Sorted Array to Binary Search Tree</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code> where the elements are sorted in <strong style="user-select: auto;">ascending order</strong>, convert <em style="user-select: auto;">it to a <strong style="user-select: auto;">height-balanced</strong> binary search tree</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">height-balanced</strong> binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [-10,-3,0,5,9]
<strong style="user-select: auto;">Output:</strong> [0,-3,9,-10,null,5]
<strong style="user-select: auto;">Explanation:</strong> [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px; user-select: auto;">
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,3]
<strong style="user-select: auto;">Output:</strong> [3,1]
<strong style="user-select: auto;">Explanation:</strong> [1,null,3] and [3,1] are both height-balanced BSTs.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">4</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums</code> is sorted in a <strong style="user-select: auto;">strictly increasing</strong> order.</li>
</ul>
</div>