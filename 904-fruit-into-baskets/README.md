<h2><a href="https://leetcode.com/problems/fruit-into-baskets/">904. Fruit Into Baskets</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array <code style="user-select: auto;">fruits</code> where <code style="user-select: auto;">fruits[i]</code> is the <strong style="user-select: auto;">type</strong> of fruit the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> tree produces.</p>

<p style="user-select: auto;">You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">You only have <strong style="user-select: auto;">two</strong> baskets, and each basket can only hold a <strong style="user-select: auto;">single type</strong> of fruit. There is no limit on the amount of fruit each basket can hold.</li>
	<li style="user-select: auto;">Starting from any tree of your choice, you must pick <strong style="user-select: auto;">exactly one fruit</strong> from <strong style="user-select: auto;">every</strong> tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.</li>
	<li style="user-select: auto;">Once you reach a tree with fruit that cannot fit in your baskets, you must stop.</li>
</ul>

<p style="user-select: auto;">Given the integer array <code style="user-select: auto;">fruits</code>, return <em style="user-select: auto;">the <strong style="user-select: auto;">maximum</strong> number of fruits you can pick</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> fruits = [<u style="user-select: auto;">1,2,1</u>]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> We can pick from all 3 trees.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> fruits = [0,<u style="user-select: auto;">1,2,2</u>]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong> We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> fruits = [1,<u style="user-select: auto;">2,3,2,2</u>]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= fruits.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= fruits[i] &lt; fruits.length</code></li>
</ul>
</div>