<h2><a href="https://leetcode.com/problems/final-value-of-variable-after-performing-operations/">2011. Final Value of Variable After Performing Operations</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is a programming language with only <strong style="user-select: auto;">four</strong> operations and <strong style="user-select: auto;">one</strong> variable <code style="user-select: auto;">X</code>:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">++X</code> and <code style="user-select: auto;">X++</code> <strong style="user-select: auto;">increments</strong> the value of the variable <code style="user-select: auto;">X</code> by <code style="user-select: auto;">1</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">--X</code> and <code style="user-select: auto;">X--</code> <strong style="user-select: auto;">decrements</strong> the value of the variable <code style="user-select: auto;">X</code> by <code style="user-select: auto;">1</code>.</li>
</ul>

<p style="user-select: auto;">Initially, the value of <code style="user-select: auto;">X</code> is <code style="user-select: auto;">0</code>.</p>

<p style="user-select: auto;">Given an array of strings <code style="user-select: auto;">operations</code> containing a list of operations, return <em style="user-select: auto;">the <strong style="user-select: auto;">final </strong>value of </em><code style="user-select: auto;">X</code> <em style="user-select: auto;">after performing all the operations</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> operations = ["--X","X++","X++"]
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong>&nbsp;The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> operations = ["++X","++X","X++"]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation: </strong>The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> operations = ["X++","++X","--X","X--"]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong>&nbsp;The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= operations.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">operations[i]</code> will be either <code style="user-select: auto;">"++X"</code>, <code style="user-select: auto;">"X++"</code>, <code style="user-select: auto;">"--X"</code>, or <code style="user-select: auto;">"X--"</code>.</li>
</ul>
</div>