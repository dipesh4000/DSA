import java.util.Stack;

public class MinStack {

    private Stack<Long> stack;
    private long min;

    public MinStack() {
        stack = new Stack<>();
    }

    public void push(long x) {
        if (stack.isEmpty()) {
            stack.push(x);
            min = x;
        } 
        else if (x >= min) {
            stack.push(x);
        } 
        else {
            // encoded value
            stack.push(2 * x - min);
            min = x;
        }
    }

    public void pop() {
        if (stack.isEmpty()) return;

        long top = stack.pop();

        if (top < min) {
            // decode previous min
            min = 2 * min - top;
        }
    }

    public long top() {
        long top = stack.peek();

        if (top < min) {
            return min;
        }
        return top;
    }

    public long getMin() {
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */