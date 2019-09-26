package n_queens;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> results = new ArrayList<>();
        if (n <= 0)
            return results;
        List<Integer> colums = new ArrayList<>();
        search(results, colums, n);
        return results;
    }

    /*
     * results store all of the chessboards
     * cols store the column indices for each row
     */
    private void search(List<List<String>> results,
                        List<Integer> cols,
                        int n) {
        if (cols.size() == n) {
            results.add(drawChessboard(cols));
            return;
        }
        for(int colIndex = 0; colIndex < n; colIndex++){
            if(!isValid(cols, colIndex))
                continue;

            cols.add(colIndex);
            search(results, cols, n);
            cols.remove(cols.size()-1); // remove the lastest colIndex to try next colums
        }
    }
    private List<String> drawChessboard(List<Integer> cols) {
        int n = cols.size();
        List<String> chessBoard = new ArrayList<>();
        for(int i = 0; i < n; i++){
            StringBuilder sb = new StringBuilder();
            for(int j=0; j < n; j++){
                sb.append(cols.get(i) == j ? 'Q':'.');
            }
            chessBoard.add(sb.toString());
        }
        return chessBoard;
    }

    private boolean isValid(List<Integer> cols, int column) {
        int row = cols.size();
        for(int rowIndex = 0; rowIndex < row; rowIndex++) {
            if (cols.get(rowIndex) == column)
                return false;
            if (cols.get(rowIndex) + rowIndex == column + row)
                return false;
            if (cols.get(rowIndex) - rowIndex == column - row)
                return false;
        }
        return true;
    }
}