# Reflection

## 1. What did you learn about static code analysis?

Static analysis tools inspect source code for potential problems without running the program. Pylint checks code quality and common mistakes, Bandit looks for security risks, and Flake8 checks style and formatting. I learned to review the findings and fix the underlying issues instead of just hiding warnings.

## 2. Which issue was most important to fix, and why?

The shell command injection issue was the most serious because supplier input was added to a command run by the operating system. Removing the shell command prevented that input from being interpreted as executable shell syntax. Parameterized SQL also protects database queries from injected input.

## 3. What changed after you fixed the issues?

The code became easier to read and safer to maintain. The final checks reported a Pylint score of 10.00/10, no Bandit issues, and no Flake8 issues. The program still ran and displayed the expected order summary.

## 4. How will you use static analysis in future projects?

I will run static analysis early and again after making changes. I will review each finding, fix valid issues, and keep the reports with the project so the results can be checked later.