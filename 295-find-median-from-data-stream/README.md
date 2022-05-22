<h2><a href="https://leetcode.com/problems/find-median-from-data-stream/">295. Find Median from Data Stream</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">The <strong style="user-select: auto;">median</strong> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, for <code style="user-select: auto;">arr = [2,3,4]</code>, the median is <code style="user-select: auto;">3</code>.</li>
	<li style="user-select: auto;">For example, for <code style="user-select: auto;">arr = [2,3]</code>, the median is <code style="user-select: auto;">(2 + 3) / 2 = 2.5</code>.</li>
</ul>

<p style="user-select: auto;">Implement the MedianFinder class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">MedianFinder()</code> initializes the <code style="user-select: auto;">MedianFinder</code> object.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">void addNum(int num)</code> adds the integer <code style="user-select: auto;">num</code> from the data stream to the data structure.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">double findMedian()</code> returns the median of all elements so far. Answers within <code style="user-select: auto;">10<sup style="user-select: auto;">-5</sup></code> of the actual answer will be accepted.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
<strong style="user-select: auto;">Output</strong>
[null, null, null, 1.5, null, 2.0]

<strong style="user-select: auto;">Explanation</strong>
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= num &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;">There will be at least one element in the data structure before calling <code style="user-select: auto;">findMedian</code>.</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">5 * 10<sup style="user-select: auto;">4</sup></code> calls will be made to <code style="user-select: auto;">addNum</code> and <code style="user-select: auto;">findMedian</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">If all integer numbers from the stream are in the range <code style="user-select: auto;">[0, 100]</code>, how would you optimize your solution?</li>
	<li style="user-select: auto;">If <code style="user-select: auto;">99%</code> of all integer numbers from the stream are in the range <code style="user-select: auto;">[0, 100]</code>, how would you optimize your solution?</li>
</ul>
</div>