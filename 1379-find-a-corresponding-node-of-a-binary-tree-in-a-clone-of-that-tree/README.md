<h2><a href="https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/">1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two binary trees <code style="user-select: auto;">original</code> and <code style="user-select: auto;">cloned</code> and given a reference to a node <code style="user-select: auto;">target</code> in the original tree.</p>

<p style="user-select: auto;">The <code style="user-select: auto;">cloned</code> tree is a <strong style="user-select: auto;">copy of</strong> the <code style="user-select: auto;">original</code> tree.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">a reference to the same node</em> in the <code style="user-select: auto;">cloned</code> tree.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Note</strong> that you are <strong style="user-select: auto;">not allowed</strong> to change any of the two trees or the <code style="user-select: auto;">target</code> node and the answer <strong style="user-select: auto;">must be</strong> a reference to a node in the <code style="user-select: auto;">cloned</code> tree.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e1.png" style="width: 544px; height: 426px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> tree = [7,4,3,null,null,6,19], target = 3
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e2.png" style="width: 221px; height: 159px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> tree = [7], target =  7
<strong style="user-select: auto;">Output:</strong> 7
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e3.png" style="width: 459px; height: 486px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
<strong style="user-select: auto;">Output:</strong> 4
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the <code style="user-select: auto;">tree</code> is in the range <code style="user-select: auto;">[1, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;">The values of the nodes of the <code style="user-select: auto;">tree</code> are unique.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">target</code> node is a node from the <code style="user-select: auto;">original</code> tree and is not <code style="user-select: auto;">null</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> Could you solve the problem if repeated values on the tree are allowed?</p>
</div>