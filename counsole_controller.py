from toah_model import TOAHModel, IllegalMoveError

def move(model, origin, dest):
    """ Apply move from origin to destination in model.
    May raise an IllegalMoveError.
    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.
        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.model = TOAHModel(number_of_stools)
        self.model.fill_first_stool(number_of_cheeses)

    def play_loop(self):
        """ Play Console-based game.
        @param ConsoleController self:
        @rtype: None
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """

        while True:
            play = input('Please enter move: ')

            if play == "q":
                return False
            result = play.split()
            from_ = int(result[0])
            to_ = int(result[1])

            try:
                if to_ > len(self.model._stools):
                    raise IllegalMoveError("Stool does not exist")
                else:
                    self.model.move(from_, to_)

            except IllegalMoveError as IE:
                print(IE)
                pass

            print(self.model)

if __name__ == '__main__':

    print("Instructions: "
          "\n\nThe number of stools and the number of cheeses must be intergers"
          "\n\nThe format is as follows:\n"
          "\tOrigin stool destination stool\n\n"
          "For example: 1 2 \nwould move the cheese "
          "from stool 1 to stool 2.\n\n"
          "To quit the game, simply enter the letter 'q' (without '')")
    num_stools = input("How many stools do you want to use?: ")
    num_cheese = input("How many cheeses do you want to use?: ")

    c = ConsoleController(int(num_cheese), int(num_stools))
    c.play_loop()