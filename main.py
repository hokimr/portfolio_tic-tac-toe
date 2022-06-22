from art import logo


board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


board_table=(
     "ㅣ"f"{board[1]}""ㅣ"f"{board[2]}""ㅣ"f"{board[3]}""ㅣ\n"
     "ㅣ"f"{board[4]}""ㅣ"f"{board[5]}""ㅣ"f"{board[6]}""ㅣ\n"
     "ㅣ"f"{board[7]}""ㅣ"f"{board[8]}""ㅣ"f"{board[9]}""ㅣ\n")

def score():
     if board[1] == "X" and board[2] == "X" and board[3] == "X" or \
             board[4] == "X" and board[5] == "X" and board[6] == "X" or\
             board[7] == "X" and board[8] == "X" and board[9] == "X" or \
             board[1] == "X" and board[4] == "X" and board[7] == "X" or \
             board[2] == "X" and board[5] == "X" and board[8] == "X" or \
             board[3] == "X" and board[6] == "X" and board[9] == "X" or \
             board[1] == "X" and board[5] == "X" and board[9] == "X" or \
             board[7] == "X" and board[5] == "X" and board[3] == "X":
          print("player1 승리!")
          return True
     elif board[1] == "O" and board[2] == "O" and board[3] == "O" or \
             board[4] == "O" and board[5] == "O" and board[6] == "O" or \
             board[7] == "O" and board[8] == "O" and board[9] == "O" or \
             board[1] == "O" and board[4] == "O" and board[7] == "O" or \
             board[2] == "O" and board[5] == "O" and board[8] == "O" or \
             board[3] == "O" and board[6] == "O" and board[9] == "O" or \
             board[1] == "O" and board[5] == "O" and board[9] == "O" or \
             board[7] == "O" and board[5] == "O" and board[3] == "O":
               print("player2 승리!")
               return True

print(logo)
print(board_table)
ON = True
while ON:

     if score():
          ON = False
          break
     player1 = int(input("player1 차례 입니다. 원하는 곳을 숫자로 입력해주세요\n"))

     if board[player1] == player1:
          board[player1] = "X"

     elif board[player1] == "X":
          print("중복된 위치입니다. 다시 시도해주세요.")
          player1 = int(input("player1 차례 입니다. 원하는 곳을 숫자로 입력해주세요"))
          board[player1] = "X"

     else:
          print("선택할수 없는 위치 입니다.")
          player1 = int(input("player1 차례 입니다. 원하는 곳을 숫자로 입력해주세요"))
          if board[player1] == player1:
               board[player1] = "X"

     print(
     "ㅣ"f"{board[1]}""ㅣ"f"{board[2]}""ㅣ"f"{board[3]}""ㅣ\n"
     "ㅣ"f"{board[4]}""ㅣ"f"{board[5]}""ㅣ"f"{board[6]}""ㅣ\n"
     "ㅣ"f"{board[7]}""ㅣ"f"{board[8]}""ㅣ"f"{board[9]}""ㅣ\n")



     if score():
          ON = False
          break

     player2 = int(input("player2 차례 입니다. 원하는 곳을 숫자로 입력해주세요"))

     if board[player2] == player2:
          board[player2] = "O"

     elif board[player2] == "O":
          print("중복된 위치 입니다. 다시 시도해주세요.")
          player2 = int(input("player2 차례 입니다. 원하는 곳을 숫자로 입력해주세요"))
          board[player2] = "O"

     else:
          print("선택할수 없는 위치 입니다.")
          player2 = int(input("player2 차례 입니다. 원하는 곳을 숫자로 입력해주세요"))
          if board[player2] == player2:
               board[player2] = "O"

     print(
     "ㅣ"f"{board[1]}""ㅣ"f"{board[2]}""ㅣ"f"{board[3]}""ㅣ\n"
     "ㅣ"f"{board[4]}""ㅣ"f"{board[5]}""ㅣ"f"{board[6]}""ㅣ\n"
     "ㅣ"f"{board[7]}""ㅣ"f"{board[8]}""ㅣ"f"{board[9]}""ㅣ\n")
