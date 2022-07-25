class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (wordList == null || beginWord == endWord)
            return 0;
        if (!wordList.contains(endWord))
            return 0;

        wordList.add(beginWord);
        final int N = wordList.size();
        
        int distance[] = new int[N];
        
        bfs(N - 1, wordList, distance);

        for (int i = 0; i < N; i++)
            if (wordList.get(i).equals(endWord) && distance[i] != Integer.MAX_VALUE)
                return distance[i] + 1;

        return 0;
    }
    private void bfs(int startNode, List<String> words, int distance[]) {
        final int INF = Integer.MAX_VALUE;
        Arrays.fill(distance, INF);

        Queue<Integer> queue = new LinkedList<>();
        distance[startNode] = 0;
        queue.add(startNode);

        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            for (int neighbour = 0; neighbour < words.size(); neighbour++)
                if (distance[neighbour] == INF && oneTransformationAway(words.get(node), words.get(neighbour))) {
                    distance[neighbour] = distance[node] + 1;
                    queue.add(neighbour);
                }
        }
    }
    private boolean oneTransformationAway(String source, String destination) {
        if (source == null || destination == null)
            return source == null && destination == null;
        if (source.length() != destination.length())
            return false;

        int transformations = 0;
        for (int i = 0; i < source.length(); i++)
            if (source.charAt(i) != destination.charAt(i))
                transformations++;

        return transformations == 1;
    }
}