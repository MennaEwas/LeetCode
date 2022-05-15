<h2><a href="https://leetcode.com/problems/remove-element/">27. Remove Element</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code> and an integer <code style="user-select: auto;">val</code>, remove all occurrences of <code style="user-select: auto;">val</code> in <code style="user-select: auto;">nums</code> <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" style="user-select: auto;"><strong style="user-select: auto;">in-place</strong></a>. The relative order of the elements may be changed.</p>

<p style="user-select: auto;">Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong style="user-select: auto;">first part</strong> of the array <code style="user-select: auto;">nums</code>. More formally, if there are <code style="user-select: auto;">k</code> elements after removing the duplicates, then the first <code style="user-select: auto;">k</code> elements of <code style="user-select: auto;">nums</code> should hold the final result. It does not matter what you leave beyond the first <code style="user-select: auto;">k</code> elements.</p>

<p style="user-select: auto;">Return <code style="user-select: auto;">k</code><em style="user-select: auto;"> after placing the final result in the first </em><code style="user-select: auto;">k</code><em style="user-select: auto;"> slots of </em><code style="user-select: auto;">nums</code>.</p>

<p style="user-select: auto;">Do <strong style="user-select: auto;">not</strong> allocate extra space for another array. You must do this by <strong style="user-select: auto;">modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" style="user-select: auto;">in-place</a></strong> with O(1) extra memory.</p>

<p style="user-select: auto;"><strong style="user-select: auto;">Custom Judge:</strong></p>

<p style="user-select: auto;">The judge will test your solution with the following code:</p>

<pre style="position: relative; user-select: auto;">int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i &lt; actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">If all assertions pass, then your solution will be <strong style="user-select: auto;">accepted</strong>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [3,2,2,3], val = 3
<strong style="user-select: auto;">Output:</strong> 2, nums = [2,2,_,_]
<strong style="user-select: auto;">Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong style="user-select: auto;">Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong style="user-select: auto;">Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums.length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= nums[i] &lt;= 50</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= val &lt;= 100</code></li>
</ul>
</div>