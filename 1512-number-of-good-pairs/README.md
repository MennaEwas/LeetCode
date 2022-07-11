<h2><a href="https://leetcode.com/problems/number-of-good-pairs/">1512. Number of Good Pairs</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of integers <code style="user-select: auto;">nums</code>, return <em style="user-select: auto;">the number of <strong style="user-select: auto;">good pairs</strong></em>.</p>

<p style="user-select: auto;">A pair <code style="user-select: auto;">(i, j)</code> is called <em style="user-select: auto;">good</em> if <code style="user-select: auto;">nums[i] == nums[j]</code> and <code style="user-select: auto;">i</code> &lt; <code style="user-select: auto;">j</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3,1,1,3]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,1,1,1]
<strong style="user-select: auto;">Output:</strong> 6
<strong style="user-select: auto;">Explanation:</strong> Each pair in the array are <em style="user-select: auto;">good</em>.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3]
<strong style="user-select: auto;">Output:</strong> 0
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums[i] &lt;= 100</code></li>
</ul>
</div>