class Solution {
    private void zero(int[][] mat, int r, int c){
        //rows
        for(int i = 0; i < mat.length; i++){
            mat[i][c] = 0;
        }
        //columns
        for(int i = 0; i < mat[r].length; i++){
            mat[r][i] = 0;
        }
    }
    public void setZeroes(int[][] matrix) {
        //record is similar to a class in java but for storing records
        record Cell(int row, int col) {}

        List<Cell> zeros = new ArrayList<>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    zeros.add(new Cell(i, j));
                }
            }
        }
        for  (Cell cell : zeros) {
            zero(matrix, cell.row, cell.col);
        }
    }
}
