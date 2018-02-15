"""
functions to run TOAH tours.
"""
import time
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.
    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        _stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    if animate is True:
        solve1(model.num_cheese, model)
    else:
        solve(model.num_cheese, model)


def solve(cheese, model, original=0, helper1=1, helper2=2, destination=3):
    """
    Solve Reve's puzzle with 4 stools without animation
    # REFERENCE:
    http://codereview.stackexchange.com/questions/42524/solving-the-reves-puzzle
    @type cheese: int
    @type model: TOAHModel
    @type original: int
    @type helper1: int
    @type helper2: int
    @type destination: int
    @rtype: None
    """

    # solve the model if there is only 1 cheese
    # if model only has 1 cheese then move it from stool 0 to stool 3
    if cheese == 1:
        model.move(original, destination)
    # solve the mdoel with a set of steps when there are 2 cheeses
    elif cheese == 2:
        model.move(original, helper1)
        model.move(original, destination)
        model.move(helper1, destination)
    # solve the model if there is more than 2 cheeses
    # 1. first move all but 2 cheeses to stool 2 using stool 1 and stool 3
    # as helper tools
    # 2. Then use predefined steps to move the 2 cheeses from stool 0 to stool 3
    # 3. Then move all the cheeses that were left on stool 2 from step 1 to
    # stool 3 using stool 0 and stool 1 as helper stools
    else:
        solve(cheese - 2, model, original, helper1, destination, helper2)
        model.move(original, helper1)
        model.move(original, destination)
        model.move(helper1, destination)
        solve(cheese - 2, model, helper2, original, helper1, destination)


def solve1(cheese, model, original=0, helper1=1, helper2=2, destination=3):
    """
    Solve Reve's puzzle with 4 stools and animate it
    # REFERENCE:
    http://codereview.stackexchange.com/questions/42524/solving-the-reves-puzzle
    @type cheese: int
    @type model: TOAHModel
    @type original: int
    @type helper1: int
    @type helper2: int
    @type destination: int
    @rtype: None
    """

    # solve the model if there is only 1 cheese
    # if model only has 1 cheese then move it from stool 0 to stool 3
    if cheese == 1:
        model.move(original, destination)
        print(model)
        time.sleep(delay_between_moves)
    # solve the mdoel with a set of steps when there are 2 cheeses
    elif cheese == 2:
        model.move(original, helper1)
        print(model)
        time.sleep(delay_between_moves)
        model.move(original, destination)
        print(model)
        time.sleep(delay_between_moves)
        model.move(helper1, destination)
        print(model)
        time.sleep(delay_between_moves)
    # solve the model if there is more than 2 cheeses
    # 1. first move all but 2 cheeses to stool 2 using stool 1 and stool 3
    # as helper tools
    # 2. Then use predefined steps to move the 2 cheeses from stool 0 to stool 3
    # 3. Then move all the cheeses that were left on stool 2 from step 1 to
    # stool 3 using stool 0 and stool 1 as helper stools
    else:
        solve1(cheese - 2, model, original, helper1, destination, helper2)
        model.move(original, helper1)
        print(model)
        time.sleep(delay_between_moves)
        model.move(original, destination)
        print(model)
        time.sleep(delay_between_moves)
        model.move(helper1, destination)
        print(model)
        time.sleep(delay_between_moves)
        solve1(cheese - 2, model, helper2, original, helper1, destination)


if __name__ == '__main__':
    num_cheeses = 16
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())