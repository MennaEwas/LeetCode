<h2><a href="https://leetcode.com/problems/word-ladder/">127. Word Ladder</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;">transformation sequence</strong> from word <code style="user-select: auto;">beginWord</code> to word <code style="user-select: auto;">endWord</code> using a dictionary <code style="user-select: auto;">wordList</code> is a sequence of words <code style="user-select: auto;">beginWord -&gt; s<sub style="user-select: auto;">1</sub> -&gt; s<sub style="user-select: auto;">2</sub> -&gt; ... -&gt; s<sub style="user-select: auto;">k</sub></code> such that:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">Every adjacent pair of words differs by a single letter.</li>
	<li style="user-select: auto;">Every <code style="user-select: auto;">s<sub style="user-select: auto;">i</sub></code> for <code style="user-select: auto;">1 &lt;= i &lt;= k</code> is in <code style="user-select: auto;">wordList</code>. Note that <code style="user-select: auto;">beginWord</code> does not need to be in <code style="user-select: auto;">wordList</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s<sub style="user-select: auto;">k</sub> == endWord</code></li>
</ul>

<p style="user-select: auto;">Given two words, <code style="user-select: auto;">beginWord</code> and <code style="user-select: auto;">endWord</code>, and a dictionary <code style="user-select: auto;">wordList</code>, return <em style="user-select: auto;">the <strong style="user-select: auto;">number of words</strong> in the <strong style="user-select: auto;">shortest transformation sequence</strong> from</em> <code style="user-select: auto;">beginWord</code> <em style="user-select: auto;">to</em> <code style="user-select: auto;">endWord</code><em style="user-select: auto;">, or </em><code style="user-select: auto;">0</code><em style="user-select: auto;"> if no such sequence exists.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation:</strong> One shortest transformation sequence is "hit" -&gt; "hot" -&gt; "dot" -&gt; "dog" -&gt; cog", which is 5 words long.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= beginWord.length &lt;= 10</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">endWord.length == beginWord.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= wordList.length &lt;= 5000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">wordList[i].length == beginWord.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">beginWord</code>, <code style="user-select: auto;">endWord</code>, and <code style="user-select: auto;">wordList[i]</code> consist of lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">beginWord != endWord</code></li>
	<li style="user-select: auto;">All the words in <code style="user-select: auto;">wordList</code> are <strong style="user-select: auto;">unique</strong>.</li>
</ul>
</div>