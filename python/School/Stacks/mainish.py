from _pytest.compat import num_mock_patch_args
from stack import Stack

ALL_OPERATORS = {"+": 0, "-": 0, "/": 1, "*": 1, "^": 2}

def eval_postfix(expr):
    """
    1. Initialize a stack
    2. if next input is a number:
            Read the next input and push it onto the stack   
       else:         
            Read the next character, which is an operator symbol         
            Use top and pop to get the two numbers off the top of the stack         
            Combine these two numbers with the operation         
            Push the result onto the stack
    3. goto #2 while there is more of the expression to read
    4. there should be one element on the stack, which is the result 
        Return this
    """
    working_stack = Stack()
    tight_expr = expr.replace(" ", "")
    for char in tight_expr:
        if char in ALL_OPERATORS:
            sum = 0.0
            if char == "^":
                op_b = working_stack.pop()
                op_a = working_stack.pop()
                sum += op_a ^ op_b
            elif char == "/":
                op_b = working_stack.pop()
                op_a = working_stack.pop()
                sum += op_a / op_b
            elif char == "*":
                op_b = working_stack.pop()
                op_a = working_stack.pop()
                sum += op_a * op_b
            elif char == "-":
                op_b = working_stack.pop()
                op_a = working_stack.pop()
                sum += op_a - op_b
            elif char == "+":
                op_b = working_stack.pop()
                op_a = working_stack.pop()
                sum += op_a + op_b
            working_stack.push(sum)
        else:
            try:
                working_stack.push(float(char))
            except:
                raise SyntaxError(f"expression {expr} contains invalid characters")
        
    return working_stack.pop()
            
            

def in2post(expr: str):
    """
    1.  initialize stack to hold operation symbols and parenthesis
    2.  if the next input is a left parenthesis:
            Read the left parenthesis and push it onto the stack   
        else if the next input is a number or operand:
            Read the operand (or number) and write it to the output   
        else if the next input is an operator:
            while (stack is not empty AND               
                stack's top is not left parenthesis AND               
                stack's top is an operation with equal or higher precedence than the next input symbol):            
                    Print the stack's top
                    Pop the stack's top
            Push the next operation symbol onto the stack
        else:
            Read and discard the next input symbol (should be a right parenthesis)
            Print the top operation and pop it
            while stack's top is not a left parenthesis:
                Print next symbol on stack and pop stack
            Pop and discard the last left parenthesis
    3.  Goto #2 while there is more of the expression to read
    4.  Print and pop any remaining operations on the stack
            There should be no remaining left parentheses
    """
    if type(expr) != str:
        raise ValueError("expression must be a string")
    if expr.count("(") != expr.count(")"):
        raise SyntaxError(f"expression {expr} is not valid")
    parens_and_ops = Stack()
    postfix = ""
    for char in expr:
        if char == "(":
            parens_and_ops.push(char)
        elif char in ALL_OPERATORS:
            while ((parens_and_ops.size() > 0) and
                    (parens_and_ops.top() != "(") and
                    (ALL_OPERATORS[parens_and_ops.top()] >= ALL_OPERATORS[char])):
                postfix += f" {parens_and_ops.pop()}"
            parens_and_ops.push(char)
        elif (type(char) == float) or (type(char) == int):
            postfix += f" {char}"
        elif char == ")":
            postfix += f" {parens_and_ops.pop()}"
            while ((parens_and_ops.size() > 0) and
                    (parens_and_ops.top() != "(")):
                    postfix += f" {parens_and_ops.pop()}"
            parens_and_ops.pop()
        else:
            operand = ""
            try:
                operand = int(char)
                postfix += f" {operand}"
            except:
                try:
                    operand = float(char)
                    postfix += f" {operand}"
                except:
                    pass
    while parens_and_ops.size() > 0:
        symbol = parens_and_ops.pop()
        if symbol in ALL_OPERATORS:
            postfix += f" {symbol}"
    return postfix


def lint_check():
    from pylint.lint import Run
    results = Run(['stack.py'], exit=False)
    print(results)

def main():
    """"
    1.open file data.txt
    2.read an infix expression from the file
    3.display the infix expression
    4.call function in2post(expr) which you write 
        in2post() takes an infix expression as an input and returns an equivalent postfix expression as a string
        If the expression is not valid, raise a SyntaxError
        If the parameter expr is not a string, raise a ValueError
    5.display the postfix expression
    6.call function eval_postfix(expr) which you write 
        eval_postfix() takes a postfix string as input and returns a number
        If the expression is not valid, raise a SyntaxError 
    7.display the result of eval_postfix()
    """
    pass

def scratch():
    print(eval_postfix("5 7 +"))

if __name__ == "__main__":
    scratch()