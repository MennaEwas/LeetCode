<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/">26. Remove Duplicates from Sorted Array</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code> sorted in <strong style="user-select: auto;">non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" style="user-select: auto;"><strong style="user-select: auto;">in-place</strong></a> such that each unique element appears only <strong style="user-select: auto;">once</strong>. The <strong style="user-select: auto;">relative order</strong> of the elements should be kept the <strong style="user-select: auto;">same</strong>.</p>

<p style="user-select: auto;">Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong style="user-select: auto;">first part</strong> of the array <code style="user-select: auto;">nums</code>. More formally, if there are <code style="user-select: auto;">k</code> elements after removing the duplicates, then the first <code style="user-select: auto;">k</code> elements of <code style="user-select: auto;">nums</code>&nbsp;should hold the final result. It does not matter what you leave beyond the first&nbsp;<code style="user-select: auto;">k</code>&nbsp;elements.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">k</code><em style="user-select: auto;"> after placing the final result in the first </em><code style="user-select: auto;">k</code><em style="user-select: auto;"> slots of </em><code style="user-select: auto;">nums</code>.</p>

<p style="user-select: auto;">Do <strong style="user-select: auto;">not</strong> allocate extra space for another array. You must do this by <strong style="user-select: auto;">modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" style="user-select: auto;">in-place</a></strong> with O(1) extra memory.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Custom Judge:</strong></p>

<p style="user-select: auto;">The judge will test your solution with the following code:</p>

<pre style="user-select: auto;">int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p style="user-select: auto;">If all assertions pass, then your solution will be <strong style="user-select: auto;">accepted</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,1,2]
<strong style="user-select: auto;">Output:</strong> 2, nums = [1,2,_]
<strong style="user-select: auto;">Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong style="user-select: auto;">Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong style="user-select: auto;">Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 3 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-100 &lt;= nums[i] &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums</code> is sorted in <strong style="user-select: auto;">non-decreasing</strong> order.</li>
</ul>
</div>