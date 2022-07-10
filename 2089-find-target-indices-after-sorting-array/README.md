<h2><a href="https://leetcode.com/problems/find-target-indices-after-sorting-array/">2089. Find Target Indices After Sorting Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a <strong style="user-select: auto;">0-indexed</strong> integer array <code style="user-select: auto;">nums</code> and a target element <code style="user-select: auto;">target</code>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">target index</strong> is an index <code style="user-select: auto;">i</code> such that <code style="user-select: auto;">nums[i] == target</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">a list of the target indices of</em> <code style="user-select: auto;">nums</code> after<em style="user-select: auto;"> sorting </em><code style="user-select: auto;">nums</code><em style="user-select: auto;"> in <strong style="user-select: auto;">non-decreasing</strong> order</em>. If there are no target indices, return <em style="user-select: auto;">an <strong style="user-select: auto;">empty</strong> list</em>. The returned list must be sorted in <strong style="user-select: auto;">increasing</strong> order.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,5,2,3], target = 2
<strong style="user-select: auto;">Output:</strong> [1,2]
<strong style="user-select: auto;">Explanation:</strong> After sorting, nums is [1,<u style="user-select: auto;"><strong style="user-select: auto;">2</strong></u>,<u style="user-select: auto;"><strong style="user-select: auto;">2</strong></u>,3,5].
The indices where nums[i] == 2 are 1 and 2.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,5,2,3], target = 3
<strong style="user-select: auto;">Output:</strong> [3]
<strong style="user-select: auto;">Explanation:</strong> After sorting, nums is [1,2,2,<u style="user-select: auto;"><strong style="user-select: auto;">3</strong></u>,5].
The index where nums[i] == 3 is 3.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,5,2,3], target = 5
<strong style="user-select: auto;">Output:</strong> [4]
<strong style="user-select: auto;">Explanation:</strong> After sorting, nums is [1,2,2,3,<u style="user-select: auto;"><strong style="user-select: auto;">5</strong></u>].
The index where nums[i] == 5 is 4.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums[i], target &lt;= 100</code></li>
</ul>
</div>