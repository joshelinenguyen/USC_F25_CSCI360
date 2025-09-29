# Lab 1 (CSCI 360 - Introduction to Artificial Intelligence)

Lab instruction: [`lab1.pdf`](lab1.pdf). Due on Sep 26th, 2025, EOD PT.

**Submission**: Submit your lab1.py to Gradescope. Please keep the file name as **lab1.py** or else the autograder will fail.

Extra credit instruction: Submit a separate pdf `lab1-extra-credit.pdf` with your analysis, figures, code to generate the figures, etc. Note that extra credits **do not** overflow, meaning a final score >60pts will be treated as 60pts. Check [`lab1_extra_credits_rubrics.pdf`](lab1_extra_credits_rubrics.pdf) for details on extra credits grading.

## Setting up the environment

Follow the command line instruction below to initialize your repository
locally. 

```
git clone <YOUR-GITHUB-REPO-HERE>
cd <YOUR-GITHUB-REPO-HERE>
conda create -n <env-name> python=3.9
conda activate <env-name>
pip install -r requirements.txt
```

## Writing Your Code:

All of the code that will be evaluated and graded will live in
[`lab1.py`](lab1.py).

You can use any Python package that is installed by `pip` or `conda`
when you create the environment.

You are provided with the `TextbookStack` class. The constructor for this class expects two
lists that represent the order. The first list `initial_order` is a
list of length `n` that expects each integer `[0, n-1]` to be present
once, the second list `initial_orientation` should be a list of length
`n` of exclusively `0`s and `1`s, representing whether each Textbook is 
facing up.

```
# Construct a stack of books in reverse order
>>> stack = TextbookStack(initial_order=[2, 1, 0], initial_orientations=[0, 0, 0])
>>> print(stack)
TextbookStack:
 	 order: [2 1 0]
	 orientations:[0 0 0]
```


You can access the current order and orientation of the books by
accessing the attributes `TextbookStack.order` and
`TextbookStack.orientations` respectively.

```
>>> stack.order
array([2, 1, 0])
>>> stack.orientations
array([0, 0, 0])
```

Calling the command `flip_stack(position)` will flip the books up to the
`position`. For example, if you want to flip the top book of your `stack`
you should call `stack.flip_stack(1)`.

```
>>> stack.flip_stack(2)
>>> stack.order
array([1, 2, 0])
>>> stack.orientations
array([1, 1, 0])
```

You can make a copy of a stack by invoking the `.copy()`. This will
create a new object with the same current order and orientations as the
stack from which you invoked the method. You can use `==` to compare the
equivalence of two stacks.

```
>>> new_stack = stack.copy()
>>> new_stack == stack
True
>>> new_stack.flip_stack(3)
>>> new_stack == stack
False
```


Finally, you can check if the stack is ordered by invoking the
`check_ordered`

```
>>> stack.check_ordered()
False
>>> stack.flip_stack(2)
>>> stack.flip_stack(3)
>>> stack.check_ordered()
True
```

## A Simple Test Case:
```
test = TextbookStack(initial_order=[3, 2, 1, 0], initial_orientations=[0, 0, 0, 0])
output_sequence = breadth_first_search(test)
print(output_sequence) # Should give you [4]


new_stack = apply_sequence(test, output_sequence)
stack_ordered = new_stack.check_ordered()
print(stack_ordered) # Should give you True
```

For DFS, there are two potential results:

```
dfs_expected_sequence_1 = [4]
dfs_expected_sequence_2 = [
        1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1,
        2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2,
        1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1,
        3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2,
        1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1,
        2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2,
        1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1,
        2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3,
        1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1,
        2, 1, 4, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2,
        1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1
]
```

All of your algorithm should be contained in the designated blocks
inside of `breadth_first_search` and `depth_first_search` and should
return the sequence of flips that your search algorithms find. Have fun!
