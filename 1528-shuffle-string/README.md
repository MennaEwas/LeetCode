<h2><a href="https://leetcode.com/problems/shuffle-string/">1528. Shuffle String</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a string <code style="user-select: auto;">s</code> and an integer array <code style="user-select: auto;">indices</code> of the <strong style="user-select: auto;">same length</strong>. The string <code style="user-select: auto;">s</code> will be shuffled such that the character at the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> position moves to <code style="user-select: auto;">indices[i]</code> in the shuffled string.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the shuffled string</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/q1.jpg" style="width: 321px; height: 243px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "codeleet", <code style="user-select: auto;">indices</code> = [4,5,6,7,0,2,1,3]
<strong style="user-select: auto;">Output:</strong> "leetcode"
<strong style="user-select: auto;">Explanation:</strong> As shown, "codeleet" becomes "leetcode" after shuffling.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "abc", <code style="user-select: auto;">indices</code> = [0,1,2]
<strong style="user-select: auto;">Output:</strong> "abc"
<strong style="user-select: auto;">Explanation:</strong> After shuffling, each character remains in its position.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">s.length == indices.length == n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of only lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= indices[i] &lt; n</code></li>
	<li style="user-select: auto;">All values of <code style="user-select: auto;">indices</code> are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>