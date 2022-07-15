<h2><a href="https://leetcode.com/problems/number-of-provinces/">547. Number of Provinces</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are <code style="user-select: auto;">n</code> cities. Some of them are connected, while some are not. If city <code style="user-select: auto;">a</code> is connected directly with city <code style="user-select: auto;">b</code>, and city <code style="user-select: auto;">b</code> is connected directly with city <code style="user-select: auto;">c</code>, then city <code style="user-select: auto;">a</code> is connected indirectly with city <code style="user-select: auto;">c</code>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">province</strong> is a group of <lighter data-id="lgt3461406842193977" data-bundle-id="0" data-slot-id="0" style="background-color: rgb(255, 255, 131); user-select: auto;">directly or indirectly</lighter><div class="LinerThreadIcon LinerFirst LinerOwnerThread" data-highlight-id="261968200" data-bundle-id="0" id="lgt261968200" style="background-image: url(&quot;https://profile.getliner.com/liner-service-bucket/user_photo_default/color-9/M.svg&quot;); user-select: auto;">
        <div class="LinerThreadIcon__dim" style="user-select: auto;"></div>
        <div class="LinerThreadIcon__mentioned" style="user-select: auto;">
          <div class="LinerThreadIcon__mentionedImg" style="user-select: auto;"></div>
        </div>
        <div class="LinerThreadIcon__onlyMe" style="user-select: auto;">
          <div class="LinerThreadIcon__onlyMeImg" style="user-select: auto;"></div>
        </div>
      </div> connected cities and no other cities outside of the group.</p>

<p style="user-select: auto;">You are given an <code style="user-select: auto;">n x n</code> matrix <code style="user-select: auto;">isConnected</code> where <code style="user-select: auto;">isConnected[i][j] = 1</code> if the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> city and the <code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code> city are directly connected, and <code style="user-select: auto;">isConnected[i][j] = 0</code> otherwise.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the total number of <strong style="user-select: auto;">provinces</strong></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> isConnected = [[1,1,0],[1,1,0],[0,0,1]]
<strong style="user-select: auto;">Output:</strong> 2
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> isConnected = [[1,0,0],[0,1,0],[0,0,1]]
<strong style="user-select: auto;">Output:</strong> 3
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == isConnected.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">n == isConnected[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">isConnected[i][j]</code> is <code style="user-select: auto;">1</code> or <code style="user-select: auto;">0</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">isConnected[i][i] == 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">isConnected[i][j] == isConnected[j][i]</code></li>
</ul>
</div>