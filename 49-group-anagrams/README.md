<h2><a href="https://leetcode.com/problems/group-anagrams/">49. Group Anagrams</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of strings <code style="user-select: auto;">strs</code>, group <strong style="user-select: auto;">the anagrams</strong> together. You can return the answer in <strong style="user-select: auto;">any order</strong>.</p>

<p style="user-select: auto;">An <strong style="user-select: auto;">Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong style="user-select: auto;">Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> strs = [""]
<strong style="user-select: auto;">Output:</strong> [[""]]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> strs = ["a"]
<strong style="user-select: auto;">Output:</strong> [["a"]]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= strs.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= strs[i].length &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">strs[i]</code> consists of lowercase English letters.</li>
</ul>
</div>