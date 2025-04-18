# -*- coding: utf-8 -*-
import random
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'minesweeper_secret_key'  # セッション用のシークレットキー

# Minesweeper Game Implementation
class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[" " for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self._initialize_game()
        self.game_over = False
        self.won = False

    # 1. ゲームの初期化
    def _initialize_game(self):
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mine_positions.add((r, c))

    def _calculate_numbers(self):
        for r, c in self.mine_positions:
            self.board[r][c] = "M"
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < self.rows
                        and 0 <= nc < self.cols
                        and self.board[nr][nc] != "M"
                    ):
                        if self.board[nr][nc] == " ":
                            self.board[nr][nc] = 1
                        else:
                            self.board[nr][nc] += 1

    # 3. ユーザーの入力を処理する
    def reveal_cell(self, row, col):
        if self.game_over or row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
            
        if (row, col) in self.mine_positions:
            self.game_over = True
            return "game_over"
            
        self._reveal_recursive(row, col)
        
        # 勝利条件をチェック：地雷以外のすべてのセルが開かれているか
        unopened = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.revealed[r][c] and (r, c) not in self.mine_positions:
                    unopened += 1
        
        if unopened == 0:
            self.won = True
            return "win"
            
        return "continue"

    def _reveal_recursive(self, row, col):
        if (
            not (0 <= row < self.rows and 0 <= col < self.cols)
            or self.revealed[row][col]
        ):
            return
        self.revealed[row][col] = True
        if self.board[row][col] == " ":
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    self._reveal_recursive(row + dr, col + dc)
    
    # ゲーム状態をセッション用に変換
    def to_dict(self):
        return {
            'rows': self.rows,
            'cols': self.cols,
            'mines': self.mines,
            'board': self.board,
            'revealed': self.revealed,
            'mine_positions': list(self.mine_positions),
            'game_over': self.game_over,
            'won': self.won
        }
    
    # セッションからゲーム状態を復元
    @classmethod
    def from_dict(cls, data):
        game = cls(data['rows'], data['cols'], data['mines'])
        game.board = data['board']
        game.revealed = data['revealed']
        game.mine_positions = set(tuple(pos) for pos in data['mine_positions'])
        game.game_over = data['game_over']
        game.won = data['won']
        return game

# Flaskルート
@app.route('/')
def index():
    # 新しいゲームを作成
    rows, cols, mines = 5, 5, 5
    game = Minesweeper(rows, cols, mines)
    session['game'] = game.to_dict()
    return render_template('index.html', rows=range(rows), cols=range(cols), 
                           game=game, message="New game started")

@app.route('/reveal', methods=['POST'])
def reveal():
    row = int(request.form.get('row'))
    col = int(request.form.get('col'))
    
    # セッションからゲーム状態を取得
    game_data = session.get('game')
    if not game_data:
        return jsonify({'error': 'Game not found'})
    
    game = Minesweeper.from_dict(game_data)
    result = game.reveal_cell(row, col)
    
    # 更新されたゲーム状態をセッションに保存
    session['game'] = game.to_dict()
    
    message = ""
    if result == "game_over":
        message = "Game Over! You hit a mine!"
    elif result == "win":
        message = "Congratulations! You won!"
    
    # 部分的なHTMLを返す
    return render_template('game_board_partial.html', rows=range(game.rows), cols=range(game.cols), 
                           game=game, message=message)

@app.route('/new_game', methods=['POST'])
def new_game():
    rows = int(request.form.get('rows', 5))
    cols = int(request.form.get('cols', 5))
    mines = int(request.form.get('mines', 5))
    
    game = Minesweeper(rows, cols, mines)
    session['game'] = game.to_dict()
    
    # 部分的なHTMLを返す
    return render_template('game_board_partial.html', rows=range(rows), cols=range(cols), 
                           game=game, message="New game started")

if __name__ == '__main__':
    app.run(debug=True)
