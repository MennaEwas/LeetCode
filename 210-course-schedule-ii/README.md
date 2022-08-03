<h2><a href="https://leetcode.com/problems/course-schedule-ii/">210. Course Schedule II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are a total of <code style="user-select: auto;">numCourses</code> courses you have to take, labeled from <code style="user-select: auto;">0</code> to <code style="user-select: auto;">numCourses - 1</code>. You are given an array <code style="user-select: auto;">prerequisites</code> where <code style="user-select: auto;">prerequisites[i] = [a<sub style="user-select: auto;">i</sub>, b<sub style="user-select: auto;">i</sub>]</code> indicates that you <strong style="user-select: auto;">must</strong> take course <code style="user-select: auto;">b<sub style="user-select: auto;">i</sub></code> first if you want to take course <code style="user-select: auto;">a<sub style="user-select: auto;">i</sub></code>.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, the pair <code style="user-select: auto;">[0, 1]</code>, indicates that to take course <code style="user-select: auto;">0</code> you have to first take course <code style="user-select: auto;">1</code>.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the ordering of courses you should take to finish all courses</em>. If there are many valid answers, return <strong style="user-select: auto;">any</strong> of them. If it is impossible to finish all courses, return <strong style="user-select: auto;">an empty array</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong style="user-select: auto;">Output:</strong> [0,1]
<strong style="user-select: auto;">Explanation:</strong> There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong style="user-select: auto;">Output:</strong> [0,2,1,3]
<strong style="user-select: auto;">Explanation:</strong> There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> numCourses = 1, prerequisites = []
<strong style="user-select: auto;">Output:</strong> [0]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= numCourses &lt;= 2000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= prerequisites.length &lt;= numCourses * (numCourses - 1)</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">prerequisites[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= a<sub style="user-select: auto;">i</sub>, b<sub style="user-select: auto;">i</sub> &lt; numCourses</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">a<sub style="user-select: auto;">i</sub> != b<sub style="user-select: auto;">i</sub></code></li>
	<li style="user-select: auto;">All the pairs <code style="user-select: auto;">[a<sub style="user-select: auto;">i</sub>, b<sub style="user-select: auto;">i</sub>]</code> are <strong style="user-select: auto;">distinct</strong>.</li>
</ul>
</div>