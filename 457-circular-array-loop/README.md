<h2><a href="https://leetcode.com/problems/circular-array-loop/">457. Circular Array Loop</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are playing a game involving a <strong style="user-select: auto;">circular</strong> array of non-zero integers <code style="user-select: auto;">nums</code>. Each <code style="user-select: auto;">nums[i]</code> denotes the number of indices forward/backward you must move if you are located at index <code style="user-select: auto;">i</code>:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">If <code style="user-select: auto;">nums[i]</code> is positive, move <code style="user-select: auto;">nums[i]</code> steps <strong style="user-select: auto;">forward</strong>, and</li>
	<li style="user-select: auto;">If <code style="user-select: auto;">nums[i]</code> is negative, move <code style="user-select: auto;">nums[i]</code> steps <strong style="user-select: auto;">backward</strong>.</li>
</ul>

<p style="user-select: auto;">Since the array is <strong style="user-select: auto;">circular</strong>, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">cycle</strong> in the array consists of a sequence of indices <code style="user-select: auto;">seq</code> of length <code style="user-select: auto;">k</code> where:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Following the movement rules above results in the repeating index sequence <code style="user-select: auto;">seq[0] -&gt; seq[1] -&gt; ... -&gt; seq[k - 1] -&gt; seq[0] -&gt; ...</code></li>
	<li style="user-select: auto;">Every <code style="user-select: auto;">nums[seq[j]]</code> is either <strong style="user-select: auto;">all positive</strong> or <strong style="user-select: auto;">all negative</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">k &gt; 1</code></li>
</ul>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if there is a <strong style="user-select: auto;">cycle</strong> in </em><code style="user-select: auto;">nums</code><em style="user-select: auto;">, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> otherwise</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/01/img1.jpg" style="width: 402px; height: 289px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,-1,1,2,2]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --&gt; 2 --&gt; 3 --&gt; 0 --&gt; ..., and all of its nodes are white (jumping in the same direction).
</pre>

<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/01/img2.jpg" style="width: 402px; height: 390px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [-1,-2,-3,-4,-5,6]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
The only cycle is of size 1, so we return false.
</pre>

<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/01/img3.jpg" style="width: 497px; height: 242px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,-1,5,1,4]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --&gt; 1 --&gt; 0 --&gt; ..., and while it is of size &gt; 1, it has a node jumping forward and a node jumping backward, so <strong style="user-select: auto;">it is not a cycle</strong>.
We can see the cycle 3 --&gt; 4 --&gt; 3 --&gt; ..., and all of its nodes are white (jumping in the same direction).
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i] != 0</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Could you solve it in <code style="user-select: auto;">O(n)</code> time complexity and <code style="user-select: auto;">O(1)</code> extra space complexity?</p>
</div>