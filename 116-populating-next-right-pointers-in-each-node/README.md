<h2><a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node/">116. Populating Next Right Pointers in Each Node</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a <strong style="user-select: auto;"><lclighter data-id="lgt261103097" data-bundle-id="0" style="background-image: linear-gradient(transparent 0%, transparent calc(50% - 4px), rgb(204, 242, 241) calc(50% - 4px), rgb(204, 242, 241) 100%); transition: background-position 120ms ease-in-out 0s, padding 120ms ease-in-out 0s; background-size: 100% 200%; background-position: initial; user-select: auto;">perfect binary tree</lclighter><div class="LinerThreadIcon LinerFirst " data-highlight-id="261103097" data-bundle-id="0" id="lgt261103097" style="background-image: url(&quot;https://photo.getliner.com/liner-service-bucket/user_photo_default/color-4/R.svg&quot;); user-select: auto;">
        <div class="LinerThreadIcon__dim" style="user-select: auto;"></div>
        <div class="LinerThreadIcon__mentioned" style="user-select: auto;">
          <div class="LinerThreadIcon__mentionedImg" style="user-select: auto;"></div>
        </div>
        <div class="LinerThreadIcon__onlyMe" style="user-select: auto;">
          <div class="LinerThreadIcon__onlyMeImg" style="user-select: auto;"></div>
        </div>
      </div></strong> where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:</p>

<pre style="user-select: auto;">struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
</pre>

<p style="user-select: auto;">Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code style="user-select: auto;">NULL</code>.</p>

<p style="user-select: auto;">Initially, all next pointers are set to <code style="user-select: auto;">NULL</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png" style="width: 500px; height: 171px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,2,3,4,5,6,7]
<strong style="user-select: auto;">Output:</strong> [1,#,2,3,#,4,5,6,7,#]
<strong style="user-select: auto;">Explanation: </strong>Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = []
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[0, 2<sup style="user-select: auto;">12</sup> - 1]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow-up:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">You may only use constant extra space.</li>
	<li style="user-select: auto;">The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.</li>
</ul>
</div>