def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_lines = []
    bottom_lines = []
    dash_lines = []
    result_lines = []
    
    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(operand1), len(operand2)) + 2
        top_line = operand1.rjust(width)
        bottom_line = operator + ' ' + operand2.rjust(width - 2)
        dash_line = '-' * width
        
        top_lines.append(top_line)
        bottom_lines.append(bottom_line)
        dash_lines.append(dash_line)
        
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            result_line = result.rjust(width)
            result_lines.append(result_line)
    
    arranged_problems = []
    arranged_problems.append("    ".join(top_lines))
    arranged_problems.append("    ".join(bottom_lines))
    arranged_problems.append("    ".join(dash_lines))
    
    if show_answers:
        arranged_problems.append("    ".join(result_lines))
    
    return "\n".join(arranged_problems)