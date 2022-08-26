<h2><a href="https://leetcode.com/problems/gas-station/">134. Gas Station</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are <code style="user-select: auto;">n</code> gas stations along a circular route, where the amount of gas at the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> station is <code style="user-select: auto;">gas[i]</code>.</p>

<p style="user-select: auto;">You have a car with an unlimited gas tank and it costs <code style="user-select: auto;">cost[i]</code> of gas to travel from the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> station to its next <code style="user-select: auto;">(i + 1)<sup style="user-select: auto;">th</sup></code> station. You begin the journey with an empty tank at one of the gas stations.</p>

<p style="user-select: auto;">Given two integer arrays <code style="user-select: auto;">gas</code> and <code style="user-select: auto;">cost</code>, return <em style="user-select: auto;">the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return</em> <code style="user-select: auto;">-1</code>. If there exists a solution, it is <strong style="user-select: auto;">guaranteed</strong> to be <strong style="user-select: auto;">unique</strong></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> gas = [1,2,3,4,5], cost = [3,4,5,1,2]
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong>
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> gas = [2,3,4], cost = [3,4,3]
<strong style="user-select: auto;">Output:</strong> -1
<strong style="user-select: auto;">Explanation:</strong>
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == gas.length == cost.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= gas[i], cost[i] &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
</ul>
</div>