<h2><a href="https://leetcode.com/problems/min-stack/">155. Min Stack</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">MinStack</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">MinStack()</code> initializes the stack object.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">void push(int val)</code> pushes the element <code style="user-select: auto;">val</code> onto the stack.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">void pop()</code> removes the element on the top of the stack.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int top()</code> gets the top element of the stack.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int getMin()</code> retrieves the minimum element in the stack.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input</strong>
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

<strong style="user-select: auto;">Output</strong>
[null,null,null,null,-3,null,0,-2]

<strong style="user-select: auto;">Explanation</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">-2<sup style="user-select: auto;">31</sup> &lt;= val &lt;= 2<sup style="user-select: auto;">31</sup> - 1</code></li>
	<li style="user-select: auto;">Methods <code style="user-select: auto;">pop</code>, <code style="user-select: auto;">top</code> and <code style="user-select: auto;">getMin</code> operations will always be called on <strong style="user-select: auto;">non-empty</strong> stacks.</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">3 * 10<sup style="user-select: auto;">4</sup></code> calls will be made to <code style="user-select: auto;">push</code>, <code style="user-select: auto;">pop</code>, <code style="user-select: auto;">top</code>, and <code style="user-select: auto;">getMin</code>.</li>
</ul>
</div>