class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int p = 0;
        for(int i = 0; i < arr2.length; i++){
            for(int j =0; j < arr1.length; j++){
                if(arr2[i] == arr1[j]) {
                        if(p != j) {int temp = arr1[p];
                        arr1[p] = arr1[j];
                        arr1[j] = temp;}
                        p++;

                }
            }
        }
    Arrays.sort(arr1, p, arr1.length);
    return arr1;
    }
}