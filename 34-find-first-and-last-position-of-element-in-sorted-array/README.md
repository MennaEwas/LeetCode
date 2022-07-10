<h2><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/">34. Find First and Last Position of Element in Sorted Array</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of integers <code style="user-select: auto;">nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code style="user-select: auto;">target</code> value.</p>

<p style="user-select: auto;">If <code style="user-select: auto;">target</code> is not found in the array, return <code style="user-select: auto;">[-1, -1]</code>.</p>

<p style="user-select: auto;">You must&nbsp;write an algorithm with&nbsp;<code style="user-select: auto;">O(log n)</code> runtime complexity.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong style="user-select: auto;">Output:</strong> [3,4]
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong style="user-select: auto;">Output:</strong> [-1,-1]
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [], target = 0
<strong style="user-select: auto;">Output:</strong> [-1,-1]
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums</code> is a non-decreasing array.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>