from collections import defaultdict

def isValidSudoku(self, board: List[List[str]]) -> bool:
    """
    My original way of solving it
    
    go through all 9 row rows
    first round:
    0:3
    2nd round
    3:6
    3rd round
    6:9
    """
    start, end = 0, 3
    slice_start, slice_end = 0, 3
    columns = defaultdict(list)

    while (end <= 9):
        sub_nums = []
        for i in range(start, end, 1):
            sliced_board = board[i][slice_start:slice_end]

            for j in range(len(sliced_board)):
                if sliced_board[j] in sub_nums and sliced_board[j] != ".":
                    return False

                if sliced_board[j] in columns[slice_start + j] and sliced_board[j] != ".": # check if the column dont contain number
                    return False

                if board[i].count(sliced_board[j]) > 1 and sliced_board[j] != ".":
                    return False
                
                sub_nums.append(sliced_board[j])
                columns[slice_start + j].append(sliced_board[j])

        if len(sub_nums) < 9:
            return False

        if slice_end < 9:
            slice_start = slice_end
            slice_end += 3
        else:
            start = end
            end += 3
            slice_start, slice_end = 0, 3
    return True

def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    columns = defaultdict(set)
    sub_boxes = defaultdict(set)

    for i in range(9): #row iteration
        for j in range(9): #column iteration
            
            # skip if our board val is a "."
            if board[i][j] == ".":
                continue

            # check if our board value has not been found in rows, column, and sub boxes
            if (board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in sub_boxes[(i // 3, j // 3)]):
                return False

            rows[i].add(board[i][j])
            columns[j].add(board[i][j])
            
            """
            The reason why this works is because by using floor divison we can 
            calculate the indice of sub box by floor diving our row and column indice by 3
            e.g.
            row: 4, column: 1 -> 4 // 3, 1 // 3 will give us our sub box indicies of (1, 0)
            """
            sub_boxes[(i // 3, j // 3)].add(board[i][j])
    return True


def isValidSudoku(self, board: List[List[str]]) -> bool:
    columns = defaultdict(set)
    rows = defaultdict(set)

    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            sub_nums = set()  # Track numbers in the current 3x3 subgrid

            for i in range(3):
                for j in range(3):
                    row = block_row + i
                    col = block_col + j
                    num = board[row][col]

                    if num == ".":
                        continue

                    if num in rows[row]:
                        return False

                    if num in columns[col]:
                        return False

                    if num in sub_nums:
                        return False

                    sub_nums.add(num)
                    rows[row].add(num)
                    columns[col].add(num)
    return True