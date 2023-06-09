import json
import sys
import board
import car


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board
        self.play()





    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to user_input, and what
                direction to user_input it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        print(board)
        user_input = input("what car you want user_input and where?")
        if user_input == "!":
            return "!"
        if self.__board.move_car(user_input[0],user_input[2]):
            if board.cell_content(board.target_location()) != None:
                return "win!"
            return 0
        else:
            return 0



    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        user_input = 0
        did_i_win = False
        while did_i_win != "!" and did_i_win != "win!":
            did_i_win = self.__single_turn()
        if did_i_win == "win!":
            print("YOU WON!")
        elif did_i_win == "!":
            print("LOSER!")





if __name__== "__main__":

    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.
    board = board.Board()
    car_dict = json.load(open(sys.argv[1]))
    car_lst = []
    for name, lst_attri in car_dict.items():
        if name in "YBOWGR":
            car_lst.append(car.Car(name, lst_attri[0], lst_attri[1], lst_attri[2]))
    for cor in car_lst:
        board.add_car(cor)
    Game(board)







    pass

