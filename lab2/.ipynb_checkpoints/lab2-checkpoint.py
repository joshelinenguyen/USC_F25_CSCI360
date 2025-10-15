# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque
from heapq import heappush, heappop

import numpy as np


class TextbookStack(object):
    """A class that tracks the"""

    def __init__(self, initial_order, initial_orientations):
        assert len(initial_order) == len(initial_orientations)
        self.num_books = len(initial_order)

        for i, a in enumerate(initial_orientations):
            assert i in initial_order
            assert a == 1 or a == 0

        self.order = np.array(initial_order)
        self.orientations = np.array(initial_orientations)

    def flip_stack(self, position):
        assert position <= self.num_books

        self.order[:position] = self.order[:position][::-1]
        self.orientations[:position] = np.abs(self.orientations[:position] - 1)[
            ::-1
        ]

    def check_ordered(self):
        for idx, front_matter in enumerate(self.orientations):
            if (idx != self.order[idx]) or (front_matter != 1):
                return False

        return True

    def copy(self):
        return TextbookStack(self.order, self.orientations)

    def __eq__(self, other):
        assert isinstance(
            other, TextbookStack
        ), "equality comparison can only ba made with other __TextbookStacks__"
        return all(self.order == other.order) and all(
            self.orientations == other.orientations
        )

    def __str__(self):
        return f"TextbookStack:\n\torder: {self.order}\n\torientations:{self.orientations}"


def apply_sequence(stack, sequence):
    new_stack = stack.copy()
    for flip in sequence:
        new_stack.flip_stack(flip)
    return new_stack

# added in heuristic function 
def heuristic(stack: TextbookStack):
    # h = heuristic counter
    h = 0

    # n = reads in the number of textbooks from the stack
    n = stack.num_books

    # iterate through to compare books on the stack (i, j) = (x, y)
    for i in range(n):
        for j in range(i + 1, n):
            
            # get the pair and their orientations (1 (face-up) or 0 (face-down))
            x, y = stack.order[i], stack.order[j]
            face_x, face_y = stack.orientations[i], stack.orientations[j]

            # 1st check is whether or not the 2 books are sequential
            check_1 = abs(x - y) != 1

            # 2nd check is whether or not their orienations are different
            check_2 = face_x != face_y                       

            # 3rd check checks if order is wrong but both orientation is upright
            check_3 = (x > y) and (face_x == face_y == 1)
            
            # 4th check checks if order is right but both orientation is face-down
            check_4 = (x < y) and (face_x == face_y == 0) 

            # if any of the above are true, then it's considered a "bad path"
            if check_1 or check_2 or check_3 or check_4:
                h += 1
    return h


# f = g + h
def a_star_search(stack):
    flip_sequence = []
    n = stack.num_books

    # create a priority queue with the help of the heuristic function
    cost = heuristic(stack)
    heap = []
    heappush(heap, (cost, 0, stack, [])) 

    # keeps track of visited pairs
    visited = set()
    visited.add((tuple(stack.order), tuple(stack.orientations)))

    while heap:
        # pops the pair with the lowest value from the heap
        estimated_cost, actual_cost, current, path = heappop(heap)

        # if the stack is already in order and all face up then store the path 
        if current.check_ordered():
            flip_sequence = path  
            break  

        # flip the top "books" until it hits n + 1
        for books in range(1, n + 1):
            # COPY THE STACK SO YOU DONT MODIFY THE OG WHEN SEARCHING!!!
            temp_stack = current.copy()
            temp_stack.flip_stack(books)

            # save the new stack
            sequence = (tuple(temp_stack.order), tuple(temp_stack.orientations))

            # continue if the sequence has already been visited
            if sequence in visited:
                continue

            # add the sequence to visited
            visited.add(sequence)

            # combine the new cost and heuristic to get total estimated cost
            g = actual_cost + 1                  
            h = heuristic(temp_stack)
            f = g + h

            # update priority queue
            heappush(heap, (f, g, temp_stack, path + [books]))
            
    return flip_sequence
    
    # ---------------------------- #

#extra credit
def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []
    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #


if __name__ == "__main__":
    test = TextbookStack(initial_order=[3, 2, 1, 0], initial_orientations=[0, 0, 0, 0])
    output_sequence = a_star_search(test)
    correct_sequence = int(output_sequence == [4])

    new_stack = apply_sequence(test, output_sequence)
    stack_ordered = new_stack.check_ordered()

    print(f"Stack is {'' if stack_ordered else 'not '}ordered")
    print(f"Comparing output to expected traces  - \t{'PASSED' if correct_sequence else 'FAILED'}")
