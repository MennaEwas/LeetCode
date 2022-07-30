<h2><a href="https://leetcode.com/problems/course-schedule/">207. Course Schedule</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are a total of <code style="user-select: auto;">numCourses</code> courses you have to take, labeled from <code style="user-select: auto;">0</code> to <code style="user-select: auto;">numCourses - 1</code>. You are given an array <code style="user-select: auto;">prerequisites</code> where <code style="user-select: auto;">prerequisites[i] = [a<sub style="user-select: auto;">i</sub>, b<sub style="user-select: auto;">i</sub>]</code> indicates that you <strong style="user-select: auto;">must</strong> take course <code style="user-select: auto;">b<sub style="user-select: auto;">i</sub></code> first if you want to take course <code style="user-select: auto;">a<sub style="user-select: auto;">i</sub></code>.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, the pair <code style="user-select: auto;">[0, 1]</code>, indicates that to take course <code style="user-select: auto;">0</code> you have to first take course <code style="user-select: auto;">1</code>.</li>
</ul>

<p style="user-select: auto;">Return <code style="user-select: auto;">true</code> if you can finish all courses. Otherwise, return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= numCourses &lt;= 2000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">prerequisites[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= a<sub style="user-select: auto;">i</sub>, b<sub style="user-select: auto;">i</sub> &lt; numCourses</code></li>
	<li style="user-select: auto;">All the pairs prerequisites[i] are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>