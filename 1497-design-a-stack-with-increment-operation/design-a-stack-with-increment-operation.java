// class CustomStack {
//     private int max;
//     private ArrayList<Integer> arr;

//     public CustomStack(int maxSize) {
//         arr = new ArrayList<>(maxSize);
//         max = maxSize;
//     }
    
//     public void push(int x) {
//         if (arr.size() < max) {
//             arr.add(x);
//         }
//     }
    
//     public int pop() {
//         if (arr.size() > 0) {
//             return arr.remove(arr.size() - 1);
//         } else {
//             return -1;
//         }
//     }
    
//     public void increment(int k, int val) {
//         int limit = Math.min(k, arr.size());
//         for (int i = 0; i < limit; i++) {
//             arr.set(i, arr.get(i) + val);
//         }
//     }
// }
class CustomStack {

    int maxSize;
    int[] stack;
    int top;

    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        this.stack = new int[maxSize];
        this.top = -1;
    }
    
    public void push(int x) {
        if (top < maxSize - 1) {
            top++;
            stack[top] = x;
        }
    }
    
    public int pop() {
        if (top == -1) {
            return -1;
        }
        int res = stack[top];
        top--;
        return res;
    }
    
    public void increment(int k, int val) {
        int n = Math.min(k, top + 1);
        for (int i = 0; i < n; i++) {
            stack[i] += val;
        }
    }
}
/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */