<h2><a href="https://leetcode.com/problems/sort-colors/">75. Sort Colors</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array <code style="user-select: auto;">nums</code> with <code style="user-select: auto;">n</code> objects colored red, white, or blue, sort <lclighter data-id="lgt257608694" data-bundle-id="0" style="background-image: linear-gradient(transparent 0%, transparent calc(50% - 4px), rgb(204, 242, 241) calc(50% - 4px), rgb(204, 242, 241) 100%); transition: background-position 120ms ease-in-out 0s, padding 120ms ease-in-out 0s; background-size: 100% 200%; background-position: initial; user-select: auto;">them </lclighter><strong style="user-select: auto;"><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank" style="user-select: auto;"><lclighter data-id="lgt257608694" data-bundle-id="0" style="background-image: linear-gradient(transparent 0%, transparent calc(50% - 4px), rgb(204, 242, 241) calc(50% - 4px), rgb(204, 242, 241) 100%); transition: background-position 120ms ease-in-out 0s, padding 120ms ease-in-out 0s; background-size: 100% 200%; background-position: initial; user-select: auto;">in-place</lclighter><div class="LinerThreadIcon LinerFirst " data-highlight-id="257608694" data-bundle-id="0" id="lgt257608694" style="background-image: url(&quot;https://profile.getliner.com/liner-service-bucket/user_photo_default/color-5/S.svg&quot;); user-select: auto;">
        <div class="LinerThreadIcon__dim" style="user-select: auto;"></div>
        <div class="LinerThreadIcon__mentioned" style="user-select: auto;">
          <div class="LinerThreadIcon__mentionedImg" style="user-select: auto;"></div>
        </div>
        <div class="LinerThreadIcon__onlyMe" style="user-select: auto;">
          <div class="LinerThreadIcon__onlyMeImg" style="user-select: auto;"></div>
        </div>
      </div></a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p style="user-select: auto;">We will use the integers <code style="user-select: auto;">0</code>, <code style="user-select: auto;">1</code>, and <code style="user-select: auto;">2</code> to represent the color red, white, and blue, respectively.</p>

<p style="user-select: auto;">You must solve this problem without using the library's sort function.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,0,2,1,1,0]
<strong style="user-select: auto;">Output:</strong> [0,0,1,1,2,2]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,0,1]
<strong style="user-select: auto;">Output:</strong> [0,1,2]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == nums.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 300</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i]</code> is either <code style="user-select: auto;">0</code>, <code style="user-select: auto;">1</code>, or <code style="user-select: auto;">2</code>.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong>&nbsp;Could you come up with a one-pass algorithm using only&nbsp;constant extra space?</p>
</div>