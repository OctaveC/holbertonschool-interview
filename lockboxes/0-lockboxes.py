#!/usr/bin/python3
"""
Method that determines if all the boxes in this puzzle can be opened
"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes
    in this puzzle can be opened

    boxes is a list of lists

    Return True if all boxes can be opened,
    else return False
    """

    # Make a set containing all our current available keys
    keys = set(boxes[0])

    # Make a set containing all the currently locked boxes
    locked_boxes = set(range(1, len(boxes)))

    # Variable indicating the current box we're looking at
    current = 1

    while current < len(boxes):

        # If our current box is locked and we have the key...
        if current in keys and current in locked_boxes:

            # We remove the current box from our locked set
            locked_boxes.remove(current)

            # And we add the keys inside the opened box to our set
            keys.update(boxes[current])

            # check if one the keys in the current boxes
            # can unlock one of the locked boxes
            Intersection = set(boxes[current]).intersection(locked_boxes)

            # If our the smallest-numbered usable key is of a number lower
            # than the current box we're looking at...
            if Intersection and min(Intersection) < current:

                # We set the current box we're looking at as the one with the
                # number of the smallest-numbered key in the current box
                # that's still locked
                current = min(set(boxes[current]).intersection(locked_boxes))

            # Else we look at the next box
            else:
                current += 1
        # Else we look at the next box
        else:
            current += 1
    if locked_boxes:
        return False
    else:
        return True
