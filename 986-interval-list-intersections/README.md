<h2><a href="https://leetcode.com/problems/interval-list-intersections/">986. Interval List Intersections</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given two lists of closed intervals, <code style="user-select: auto;">firstList</code> and <code style="user-select: auto;">secondList</code>, where <code style="user-select: auto;">firstList[i] = [start<sub style="user-select: auto;">i</sub>, end<sub style="user-select: auto;">i</sub>]</code> and <code style="user-select: auto;">secondList[j] = [start<sub style="user-select: auto;">j</sub>, end<sub style="user-select: auto;">j</sub>]</code>. Each list of intervals is pairwise <strong style="user-select: auto;">disjoint</strong> and in <strong style="user-select: auto;">sorted order</strong>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the intersection of these two interval lists</em>.</p>

<p style="user-select: auto;">A <strong style="user-select: auto;">closed interval</strong> <code style="user-select: auto;">[a, b]</code> (with <code style="user-select: auto;">a &lt;= b</code>) denotes the set of real numbers <code style="user-select: auto;">x</code> with <code style="user-select: auto;">a &lt;= x &lt;= b</code>.</p>

<p style="user-select: auto;">The <strong style="user-select: auto;">intersection</strong> of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of <code style="user-select: auto;">[1, 3]</code> and <code style="user-select: auto;">[2, 4]</code> is <code style="user-select: auto;">[2, 3]</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png" style="width: 700px; height: 194px; user-select: auto;">
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
<strong style="user-select: auto;">Output:</strong> [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> firstList = [[1,3],[5,9]], secondList = []
<strong style="user-select: auto;">Output:</strong> []
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= firstList.length, secondList.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">firstList.length + secondList.length &gt;= 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= start<sub style="user-select: auto;">i</sub> &lt; end<sub style="user-select: auto;">i</sub> &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">end<sub style="user-select: auto;">i</sub> &lt; start<sub style="user-select: auto;">i+1</sub></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= start<sub style="user-select: auto;">j</sub> &lt; end<sub style="user-select: auto;">j</sub> &lt;= 10<sup style="user-select: auto;">9</sup> </code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">end<sub style="user-select: auto;">j</sub> &lt; start<sub style="user-select: auto;">j+1</sub></code></li>
</ul>
</div>