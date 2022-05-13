<h2><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/">33. Search in Rotated Sorted Array</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is an integer array <code style="user-select: auto;">nums</code> sorted in ascending order (with <strong style="user-select: auto;">distinct</strong> values).</p>

<p style="user-select: auto;">Prior to being passed to your function, <code style="user-select: auto;">nums</code> is <strong style="user-select: auto;">possibly rotated</strong> at an unknown pivot index <code style="user-select: auto;">k</code> (<code style="user-select: auto;">1 &lt;= k &lt; nums.length</code>) such that the resulting array is <code style="user-select: auto;">[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong style="user-select: auto;">0-indexed</strong>). For example, <code style="user-select: auto;">[0,1,2,4,5,6,7]</code> might be rotated at pivot index <code style="user-select: auto;">3</code> and become <code style="user-select: auto;">[4,5,6,7,0,1,2]</code>.</p>

<p style="user-select: auto;">Given the array <code style="user-select: auto;">nums</code> <strong style="user-select: auto;">after</strong> the possible rotation and an integer <code style="user-select: auto;">target</code>, return <em style="user-select: auto;">the index of </em><code style="user-select: auto;">target</code><em style="user-select: auto;"> if it is in </em><code style="user-select: auto;">nums</code><em style="user-select: auto;">, or </em><code style="user-select: auto;">-1</code><em style="user-select: auto;"> if it is not in </em><code style="user-select: auto;">nums</code>.</p>

<p style="user-select: auto;">You must write an algorithm with <code style="user-select: auto;">O(log n)</code> runtime complexity.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong style="user-select: auto;">Output:</strong> 4
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong style="user-select: auto;">Output:</strong> -1
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1], target = 0
<strong style="user-select: auto;">Output:</strong> -1
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">4</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;">All values of <code style="user-select: auto;">nums</code> are <strong style="user-select: auto;">unique</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums</code> is an ascending array that is possibly rotated.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">4</sup> &lt;= target &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>