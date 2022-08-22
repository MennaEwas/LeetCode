<h2><a href="https://leetcode.com/problems/sum-root-to-leaf-numbers/">129. Sum Root to Leaf Numbers</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given the <code style="user-select: auto;">root</code> of a binary tree containing digits from <code style="user-select: auto;">0</code> to <code style="user-select: auto;">9</code> only.</p>

<p style="user-select: auto;">Each root-to-leaf path in the tree represents a number.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, the root-to-leaf path <code style="user-select: auto;">1 -&gt; 2 -&gt; 3</code> represents the number <code style="user-select: auto;">123</code>.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the total sum of all root-to-leaf numbers</em>. Test cases are generated so that the answer will fit in a <strong style="user-select: auto;">32-bit</strong> integer.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">leaf</strong> node is a node with no children.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg" style="width: 212px; height: 182px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,2,3]
<strong style="user-select: auto;">Output:</strong> 25
<strong style="user-select: auto;">Explanation:</strong>
The root-to-leaf path <code style="user-select: auto;">1-&gt;2</code> represents the number <code style="user-select: auto;">12</code>.
The root-to-leaf path <code style="user-select: auto;">1-&gt;3</code> represents the number <code style="user-select: auto;">13</code>.
Therefore, sum = 12 + 13 = <code style="user-select: auto;">25</code>.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg" style="width: 292px; height: 302px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [4,9,0,5,1]
<strong style="user-select: auto;">Output:</strong> 1026
<strong style="user-select: auto;">Explanation:</strong>
The root-to-leaf path <code style="user-select: auto;">4-&gt;9-&gt;5</code> represents the number 495.
The root-to-leaf path <code style="user-select: auto;">4-&gt;9-&gt;1</code> represents the number 491.
The root-to-leaf path <code style="user-select: auto;">4-&gt;0</code> represents the number 40.
Therefore, sum = 495 + 491 + 40 = <code style="user-select: auto;">1026</code>.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[1, 1000]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= Node.val &lt;= 9</code></li>
	<li style="user-select: auto;">The depth of the tree will not exceed <code style="user-select: auto;">10</code>.</li>
</ul>
</div>