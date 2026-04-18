'''Build a game leaderboard:

add_score(board, name, score) → adds player score
get_rank(board, name) → returns rank of a player
show_leaderboard(board) → prints top players sorted by score
board = {}
board = add_score(board, "Alice", 950)
board = add_score(board, "Bob", 750)
board = add_score(board, "Charlie", 870)
board = add_score(board, "Diana", 990)
show_leaderboard(board)
# 1. Diana  — 990
# 2. Alice  — 950
# 3. Charlie — 870
# 4. Bob    — 750
print(get_rank(board, "Alice"))   # Rank 2
'''

board={}

def add_score(board, name, score):
    board[name]=score
    return board
def get_rank(board, name):
    sorted_board = sorted(board.items(), key=lambda x:x[1], reverse=True)
    for rank,(player,score) in enumerate(sorted_board, start=1):
        if player==name:
            return f"Rank is {rank}"
    return "Player not found"
def show_leaderboard(board):
    sorted_board = sorted(board.items(), key= lambda x :x[1], reverse=True)
    for rank,(player,score) in enumerate(sorted_board,start=1):
        print(rank," ",player, ":", score)
print(add_score(board,"kaif",550))
print(add_score(board,"suhib",950))
print(get_rank(board, "suhib"))
show_leaderboard(board)