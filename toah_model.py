"""
TOAHModel:  Model a game of Tour of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Tour of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""

class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.
    Model _stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty _stools
        to hold _stools of cheese.
        @param TOAHModel self:
        @param int number_of_stools:
        @rtype: None
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        self.num_stools = number_of_stools
        self._stools = []
        self._move_seq = MoveSequence([])
        self.num_cheese = 0
        # Add new stool to list of _stools
        for _ in range(number_of_stools):
            self._stools.append([])

    def fill_first_stool(self, num_cheese):
        """
        Add num_cheese number of num_cheese to the first stool.
        @type self: TOAHModel
        @type num_cheese: int
        @rtype: None
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        self.num_cheese = num_cheese
        for i in reversed(range(num_cheese)):
            # add a new cheese to the first stool(stack)
            self._stools[0].append(Cheese(i + 1))

    def get_number_of_stools(self):
        """
        Return number of _stools in TOAH model
        @type self: TOAHModel
        @rtype: int
        >>> M = TOAHModel(4)
        >>> M.get_number_of_stools()
        4
        """
        return self.num_stools

    def number_of_moves(self):
        """
        Return number of moves.
        @type self: TOAHModel
        @rtype: int
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.number_of_moves()
        0
        """
        return self._move_seq.length()

    def get_number_of_cheeses(self):
        """
        Return number of cheeses
        @type self: TOAHModel
        @rtype: int
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.get_number_of_cheeses()
        5
        """
        return self.num_cheese

    def get_move_seq(self):
        """ Return the move sequence
        @type self: TOAHModel
        @rtype: MoveSequence
        """
        return self._move_seq

    def _cheese_at(self, stool_index, stool_height):
        """ Return (stool_height)th from stool_index stool, if possible.
        @type self: TOAHModel
        @type stool_index: int
        @type stool_height: int
        @rtype: Cheese | None
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        if 0 <= stool_height < len(self._stools[stool_index]):
            return self._stools[stool_index][stool_height]
        else:
            return None

    def move(self, original_stool, destination_stool):
        """
        Move cheese from original_stool to destination_stool.
        @type self: TOAHModel
        @type original_stool: int
        @type destination_stool: int
        @rtype: None
        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        # Make sure there's a cheese on the origin stool
        if len(self._stools[original_stool]) == 0:
            raise IllegalMoveError("There's no cheese.")
        # If there's a cheese on dest stool, make sure it's larger than the
        # one you're moving
        if len(self._stools[destination_stool]) > 0:
            top_cheese_origin = self.get_top_cheese(original_stool)
            top_cheese_dest = self.get_top_cheese(destination_stool)
            if top_cheese_origin.size > top_cheese_dest.size:
                raise IllegalMoveError("The cheese you're trying to move "
                                       "is too large")
            else:
                self._stools[destination_stool].append(
                    self._stools[original_stool].pop())
                self._move_seq.add_move(original_stool, destination_stool)

        else:
            self._stools[destination_stool].append(
                self._stools[original_stool].pop())
            self._move_seq.add_move(original_stool, destination_stool)

    def add(self, cheese, stool):
        """
        Add a cheese to a stool
        @type self: TOAHModel
        @type cheese: Cheese
        @type stool: int
        @rtype: None
        """
        self._stools[stool].append(cheese)

    def get_cheese_location(self, cheese):
        """
        Return index location of a cheese
        @type self: TOAHModel
        @type cheese: Cheese
        @rtype: int
        # >>> m = TOAHModel(4)
        # >>> m.fill_first_stool(5)
        # >>>
        """
        for stool in self._stools:
            for i in stool:
                if i == cheese:
                    return self._stools.index(stool)
        return -1

    def get_top_cheese(self, index):
        """
        Get the top Cheese
        @type self: TOAHModel
        @type index: int
        @rtype: Cheese
        """
        if len(self._stools[index]) > 0:
            return self._stools[index][-1]

    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.
        Two TOAHModels are equivalent if their current
        configurations of cheeses on _stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other
        @type self: TOAHModel
        @type other: TOAHModel
        @rtype: bool
        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        for i in range(len(self._stools) - 1):
            for c in range(len(self._stools[i]) - 1):
                if self._stools[i][c] != other._stools[i][c]:
                    return False
        return True


    def __str__(self):
        """
        Depicts only the current state of the _stools and cheese.
        @param TOAHModel self:
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines


class Cheese:
    """ A cheese for stacking in a TOAHModel
    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.
        @param Cheese self:
        @param int size:
        @rtype: None
        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __eq__(self, other):
        """ Is self equivalent to other?
        We say they are if they're the same
        size.
        @param Cheese self:
        @param Cheese|Any other:
        @rtype: bool
        """
        return (type(self) == type(other)) and (self.size == other.size)


class IllegalMoveError(Exception):
    """ Exception indicating move that violate TOAHModel
    """
    pass


class MoveSequence(object):
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.
        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def get_move(self, i):
        """ Return the move at position i in self
        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]
        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.
        @param MoveSequence self:
        @param int src_stool:
        @param int dest_stool:
        @rtype: None
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.
        @param MoveSequence self:
        @rtype: int
        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
         after moves in self.
        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.
        @param MoveSequence self:
        @param int number_of_stools:
        @param int number_of_cheeses:
        @rtype: TOAHModel
        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)