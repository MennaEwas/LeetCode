<h2><a href="https://leetcode.com/problems/clone-graph/">133. Clone Graph</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a reference of a node in a <strong style="user-select: auto;"><a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank" style="user-select: auto;">connected</a></strong> undirected graph.</p>

<p style="user-select: auto;">Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank" style="user-select: auto;"><strong style="user-select: auto;">deep copy</strong></a> (clone) of the graph.</p>

<p style="user-select: auto;">Each node in the graph contains a value (<code style="user-select: auto;">int</code>) and a list (<code style="user-select: auto;">List[Node]</code>) of its neighbors.</p>

<pre style="user-select: auto;">class Node {
    public int val;
    public List&lt;Node&gt; neighbors;
}
</pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Test case format:</strong></p>

<p style="user-select: auto;">For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with <code style="user-select: auto;">val == 1</code>, the second node with <code style="user-select: auto;">val == 2</code>, and so on. The graph is represented in the test case using an adjacency list.</p>

<p style="user-select: auto;"><b style="user-select: auto;">An adjacency list</b> is a collection of unordered <b style="user-select: auto;">lists</b> used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.</p>

<p style="user-select: auto;">The given node will always be the first node with <code style="user-select: auto;">val = 1</code>. You must return the <strong style="user-select: auto;">copy of the given node</strong> as a reference to the cloned graph.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png" style="width: 454px; height: 500px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> adjList = [[2,4],[1,3],[2,4],[1,3]]
<strong style="user-select: auto;">Output:</strong> [[2,4],[1,3],[2,4],[1,3]]
<strong style="user-select: auto;">Explanation:</strong> There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/07/graph.png" style="width: 163px; height: 148px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> adjList = [[]]
<strong style="user-select: auto;">Output:</strong> [[]]
<strong style="user-select: auto;">Explanation:</strong> Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> adjList = []
<strong style="user-select: auto;">Output:</strong> []
<strong style="user-select: auto;">Explanation:</strong> This an empty graph, it does not have any nodes.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the graph is in the range <code style="user-select: auto;">[0, 100]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= Node.val &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">Node.val</code> is unique for each node.</li>
	<li style="user-select: auto;">There are no repeated edges and no self-loops in the graph.</li>
	<li style="user-select: auto;">The Graph is connected and all nodes can be visited starting from the given node.</li>
</ul>
</div>