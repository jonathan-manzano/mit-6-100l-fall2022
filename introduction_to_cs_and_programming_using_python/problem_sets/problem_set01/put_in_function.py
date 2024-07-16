#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:55:06 2017

Author: lauragustafson, knjohnso, carlosh
"""


def put_in_functions_a():
    try:
        function_name = "part_a"
        function_header = (
            f"def {function_name}(yearly_salary, portion_saved, " "cost_of_dream_home):"
        )
        student_file_name = "ps1a.py"
        return_variable = "months"
        return_statement = f"\treturn {return_variable}"
        new_file_name = "ps1a_in_function.py"
        start_line = (
            "## Initialize other variables you need (if any) for your program below ##"
        )

        new_lines = []
        lines = [line.rstrip("\n") for line in open("ps1a.py")]
        start_index = [line.startswith(start_line) for line in lines].index(True)
        lines = lines[start_index + 1 :]

        new_lines.append(function_header)
        for line in lines:
            new_lines.append("\t" + line)
        new_lines.append(return_statement)

        with open(new_file_name, "w") as new_file:
            new_file.write("\n".join(new_lines))
    except Exception as e:
        print(
            "[PART A] Did you keep all the original comments the file came with? "
            "Did you initialize variables at the right places?"
        )
        print(f"Error: {e}")


def put_in_functions_b():
    try:
        function_name = "part_b"
        function_header = (
            f"def {function_name}(yearly_salary, portion_saved, cost_of_dream_home, "
            "semi_annual_raise):"
        )
        student_file_name = "ps1b.py"
        return_variable = "months"
        return_statement = f"\treturn {return_variable}"
        new_file_name = "ps1b_in_function.py"
        start_line = (
            "## Initialize other variables you need (if any) for your program below ##"
        )

        new_lines = []
        lines = [line.rstrip("\n") for line in open("ps1b.py")]
        start_index = [line.startswith(start_line) for line in lines].index(True)
        lines = lines[start_index + 1 :]

        new_lines.append(function_header)
        for line in lines:
            new_lines.append("\t" + line)
        new_lines.append(return_statement)

        with open(new_file_name, "w") as new_file:
            new_file.write("\n".join(new_lines))
    except Exception as e:
        print(
            "[PART B] Did you keep all the original comments the file came with? "
            "Did you initialize variables at the right places?"
        )
        print(f"Error: {e}")


def put_in_functions_c():
    try:
        function_name = "part_c"
        function_header = f"def {function_name}(initial_deposit):"
        student_file_name = "ps1c.py"
        return_variable = "r, steps"
        return_statement = f"\treturn {return_variable}"
        new_file_name = "ps1c_in_function.py"
        start_line = (
            "## Initialize other variables you need (if any) for your program below ##"
        )

        new_lines = []
        lines = [line.rstrip("\n") for line in open("ps1c.py")]
        start_index = [line.startswith(start_line) for line in lines].index(True)
        lines = lines[start_index + 1 :]

        new_lines.append(function_header)
        for line in lines:
            new_lines.append("\t" + line)
        new_lines.append(return_statement)

        with open(new_file_name, "w") as new_file:
            new_file.write("\n".join(new_lines))
    except Exception as e:
        print(
            "[PART C] Did you keep all the original comments the file came with? "
            "Did you initialize variables at the right places?"
        )
        print(f"Error: {e}")


put_in_functions_a()
put_in_functions_b()
put_in_functions_c()
