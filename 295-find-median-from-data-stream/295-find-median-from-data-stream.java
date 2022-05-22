class MedianFinder {
    
    private PriorityQueue<Integer> firstHalf;
    private PriorityQueue<Integer> secondHalf;

    public MedianFinder() {
        firstHalf = new PriorityQueue<Integer>((a, b) -> b - a);
        secondHalf = new PriorityQueue<Integer>();
    }
    
    public void addNum(int num) {
      if (firstHalf.size() == 0 || num <= firstHalf.peek()) {
        firstHalf.add(num);
        if (firstHalf.size() > secondHalf.size() + 1)
            secondHalf.add(firstHalf.poll());
      } else {
          secondHalf.add(num);
          if (secondHalf.size() > firstHalf.size())
              firstHalf.add(secondHalf.poll());
      }
    }
    
    public double findMedian() {
        if (firstHalf.size() > secondHalf.size()) {
            return 1.0 * firstHalf.peek();
        } else {
            double sum = firstHalf.peek() + secondHalf.peek();
            return sum / 2;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */