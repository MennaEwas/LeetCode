<h2><a href="https://leetcode.com/problems/h-index-ii/">275. H-Index II</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of integers <code style="user-select: auto;">citations</code> where <code style="user-select: auto;">citations[i]</code> is the number of citations a researcher received for their <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> paper and <code style="user-select: auto;">citations</code>&nbsp;is sorted in an <strong style="user-select: auto;">ascending order</strong>, return compute the researcher's <code style="user-select: auto;">h</code><strong style="user-select: auto;">-index</strong>.</p>

<p style="user-select: auto;">According to the <a href="https://en.wikipedia.org/wiki/H-index" target="_blank" style="user-select: auto;">definition of h-index on Wikipedia</a>: A scientist has an index <code style="user-select: auto;">h</code> if <code style="user-select: auto;">h</code> of their <code style="user-select: auto;">n</code> papers have at least <code style="user-select: auto;">h</code> citations each, and the other <code style="user-select: auto;">n − h</code> papers have no more than <code style="user-select: auto;">h</code> citations each.</p>

<p style="user-select: auto;">If there are several possible values for <code style="user-select: auto;">h</code>, the maximum one is taken as the <code style="user-select: auto;">h</code><strong style="user-select: auto;">-index</strong>.</p>

<p style="user-select: auto;">You must write an algorithm that runs in logarithmic time.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> citations = [0,1,3,5,6]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> citations = [1,2,100]
<strong style="user-select: auto;">Output:</strong> 2
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == citations.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= citations[i] &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">citations</code> is sorted in <strong style="user-select: auto;">ascending order</strong>.</li>
</ul>
</div>