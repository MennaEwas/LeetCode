<h2><a href="https://leetcode.com/problems/network-delay-time/">743. Network Delay Time</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a network of <code style="user-select: auto;">n</code> nodes, labeled from <code style="user-select: auto;">1</code> to <code style="user-select: auto;">n</code>. You are also given <code style="user-select: auto;">times</code>, a list of travel times as directed edges <code style="user-select: auto;">times[i] = (u<sub style="user-select: auto;">i</sub>, v<sub style="user-select: auto;">i</sub>, w<sub style="user-select: auto;">i</sub>)</code>, where <code style="user-select: auto;">u<sub style="user-select: auto;">i</sub></code> is the source node, <code style="user-select: auto;">v<sub style="user-select: auto;">i</sub></code> is the target node, and <code style="user-select: auto;">w<sub style="user-select: auto;">i</sub></code> is the time it takes for a signal to travel from source to target.</p>

<p style="user-select: auto;">We will send a signal from a given node <code style="user-select: auto;">k</code>. Return <em style="user-select: auto;">the <strong style="user-select: auto;">minimum</strong> time it takes for all the</em> <code style="user-select: auto;">n</code> <em style="user-select: auto;">nodes to receive the signal</em>. If it is impossible for all the <code style="user-select: auto;">n</code> nodes to receive the signal, return <code style="user-select: auto;">-1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="width: 217px; height: 239px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong style="user-select: auto;">Output:</strong> 2
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong style="user-select: auto;">Output:</strong> 1
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong style="user-select: auto;">Output:</strong> -1
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= times.length &lt;= 6000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">times[i].length == 3</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= u<sub style="user-select: auto;">i</sub>, v<sub style="user-select: auto;">i</sub> &lt;= n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">u<sub style="user-select: auto;">i</sub> != v<sub style="user-select: auto;">i</sub></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= w<sub style="user-select: auto;">i</sub> &lt;= 100</code></li>
	<li style="user-select: auto;">All the pairs <code style="user-select: auto;">(u<sub style="user-select: auto;">i</sub>, v<sub style="user-select: auto;">i</sub>)</code> are <strong style="user-select: auto;">unique</strong>. (i.e., no multiple edges.)</li>
</ul>
</div>