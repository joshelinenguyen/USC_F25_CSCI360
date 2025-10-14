# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque
import numpy as np

class TextbookStack(object):
    """ A class that tracks the """
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
        self.orientations[:position] = np.abs(self.orientations[:position] - 1)[::-1]

    def check_ordered(self):
        for idx, front_matter in enumerate(self.orientations):
            if (idx != self.order[idx]) or (front_matter != 1):
                return False

        return True

    def copy(self):
        return TextbookStack(self.order, self.orientations)
    
    def __eq__(self, other):
        assert isinstance(other, TextbookStack), "equality comparison can only ba made with other __TextbookStacks__"
        return all(self.order == other.order) and all(self.orientations == other.orientations)

    def __str__(self):
        return f"TextbookStack:\n\torder: {self.order}\n\torientations:{self.orientations}"


def apply_sequence(stack, sequence):
    new_stack = stack.copy()
    for flip in sequence:
        new_stack.flip_stack(flip)
    return new_stack

def breadth_first_search(stack):
    flip_sequence = []
    
    visited = set()
    queue = deque([(stack.copy(), [])])

    while queue:
        current_stack, sequence_so_far = queue.popleft()

        # check if goal reached
        if current_stack.check_ordered():
            return sequence_so_far

        # mark as visited
        state_id = (tuple(current_stack.order), tuple(current_stack.orientations))
        if state_id in visited:
            continue
        visited.add(state_id)

        # generate next states by flipping 
        for pos in range(1, current_stack.num_books + 1):
            new_stack = current_stack.copy()
            new_stack.flip_stack(pos)
            new_seq = sequence_so_far + [pos]
            queue.append((new_stack, new_seq))
            
    return flip_sequence
    # ---------------------------- #


def depth_first_search(stack):
    flip_sequence = []

    visited = set()
    stack_container = [(stack.copy(), [])] 

    while stack_container:
        current_stack, sequence_so_far = stack_container.pop()

        # check if goal reached
        if current_stack.check_ordered():
            return sequence_so_far

        # mark as visited
        state_id = (tuple(current_stack.order), tuple(current_stack.orientations))
        if state_id in visited:
            continue
        visited.add(state_id)

        # generate next states by flipping 
        for pos in range(1, current_stack.num_books + 1):
            new_stack = current_stack.copy()
            new_stack.flip_stack(pos)
            new_seq = sequence_so_far + [pos]
            stack_container.append((new_stack, new_seq))

    return flip_sequence
    # ---------------------------- #