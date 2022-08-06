<h2><a href="https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/">1557. Minimum Number of Vertices to Reach All Nodes</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a<strong style="user-select: auto;">&nbsp;directed acyclic graph</strong>,&nbsp;with&nbsp;<code style="user-select: auto;">n</code>&nbsp;vertices numbered from&nbsp;<code style="user-select: auto;">0</code>&nbsp;to&nbsp;<code style="user-select: auto;">n-1</code>,&nbsp;and an array&nbsp;<code style="user-select: auto;">edges</code>&nbsp;where&nbsp;<code style="user-select: auto;">edges[i] = [from<sub style="user-select: auto;">i</sub>, to<sub style="user-select: auto;">i</sub>]</code>&nbsp;represents a directed edge from node&nbsp;<code style="user-select: auto;">from<sub style="user-select: auto;">i</sub></code>&nbsp;to node&nbsp;<code style="user-select: auto;">to<sub style="user-select: auto;">i</sub></code>.</p>

<p style="user-select: auto;">Find <em style="user-select: auto;">the smallest set of vertices from which all nodes in the graph are reachable</em>. It's guaranteed that a unique solution exists.</p>

<p style="user-select: auto;">Notice that you can return the vertices in any order.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/07/07/untitled22.png" style="width: 231px; height: 181px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
<strong style="user-select: auto;">Output:</strong> [0,3]
<b style="user-select: auto;">Explanation: </b>It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<p style="user-select: auto;"><img alt="" src="https://assets.leetcode.com/uploads/2020/07/07/untitled.png" style="width: 201px; height: 201px; user-select: auto;"></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
<strong style="user-select: auto;">Output:</strong> [0,2,3]
<strong style="user-select: auto;">Explanation: </strong>Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= n &lt;= 10^5</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= edges.length &lt;= min(10^5, n * (n - 1) / 2)</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">edges[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= from<sub style="user-select: auto;">i,</sub>&nbsp;to<sub style="user-select: auto;">i</sub> &lt; n</code></li>
	<li style="user-select: auto;">All pairs <code style="user-select: auto;">(from<sub style="user-select: auto;">i</sub>, to<sub style="user-select: auto;">i</sub>)</code> are distinct.</li>
</ul></div>