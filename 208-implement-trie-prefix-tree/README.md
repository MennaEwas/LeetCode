<h2><a href="https://leetcode.com/problems/implement-trie-prefix-tree/">208. Implement Trie (Prefix Tree)</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank" style="user-select: auto;"><strong style="user-select: auto;">trie</strong></a> (pronounced as "try") or <strong style="user-select: auto;">prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.</p>

<p style="user-select: auto;">Implement the Trie class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">Trie()</code> Initializes the trie object.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">void insert(String word)</code> Inserts the string <code style="user-select: auto;">word</code> into the trie.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean search(String word)</code> Returns <code style="user-select: auto;">true</code> if the string <code style="user-select: auto;">word</code> is in the trie (i.e., was inserted before), and <code style="user-select: auto;">false</code> otherwise.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean startsWith(String prefix)</code> Returns <code style="user-select: auto;">true</code> if there is a previously inserted string <code style="user-select: auto;">word</code> that has the prefix <code style="user-select: auto;">prefix</code>, and <code style="user-select: auto;">false</code> otherwise.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
<strong style="user-select: auto;">Output</strong>
[null, null, true, false, true, null, true]

<strong style="user-select: auto;">Explanation</strong>
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">word</code> and <code style="user-select: auto;">prefix</code> consist only of lowercase English letters.</li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">3 * 10<sup style="user-select: auto;">4</sup></code> calls <strong style="user-select: auto;">in total</strong> will be made to <code style="user-select: auto;">insert</code>, <code style="user-select: auto;">search</code>, and <code style="user-select: auto;">startsWith</code>.</li>
</ul>
</div>