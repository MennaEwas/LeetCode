<h2><a href="https://leetcode.com/problems/range-sum-query-immutable/">303. Range Sum Query - Immutable</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code>, handle multiple queries of the following type:</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">Calculate the <strong style="user-select: auto;">sum</strong> of the elements of <code style="user-select: auto;">nums</code> between indices <code style="user-select: auto;">left</code> and <code style="user-select: auto;">right</code> <strong style="user-select: auto;">inclusive</strong> where <code style="user-select: auto;">left &lt;= right</code>.</li>
</ol>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">NumArray</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">NumArray(int[] nums)</code> Initializes the object with the integer array <code style="user-select: auto;">nums</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int sumRange(int left, int right)</code> Returns the <strong style="user-select: auto;">sum</strong> of the elements of <code style="user-select: auto;">nums</code> between indices <code style="user-select: auto;">left</code> and <code style="user-select: auto;">right</code> <strong style="user-select: auto;">inclusive</strong> (i.e. <code style="user-select: auto;">nums[left] + nums[left + 1] + ... + nums[right]</code>).</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input</strong>
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
<strong style="user-select: auto;">Output</strong>
[null, 1, -1, -3]

<strong style="user-select: auto;">Explanation</strong>
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= left &lt;= right &lt; nums.length</code></li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">10<sup style="user-select: auto;">4</sup></code> calls will be made to <code style="user-select: auto;">sumRange</code>.</li>
</ul>
</div>