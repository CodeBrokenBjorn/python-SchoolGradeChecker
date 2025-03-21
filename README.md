# python-SchoolGradeChecker
A simple Python program that checks student grades and shows pass/fail status.

## Features
- Check grades against A+ through F ranges
- Track student scores by category
- Show pass/fail status
- Calculate category statistics

## How to Use
```python
from grade_checker import check_grade

# Check a single score
score = 85
passed, grade = check_grade(score)
print(f"Score: {score}, Grade: {grade}, Status: {'Passed' if passed else 'Failed'}")
```

## Project Structure
```markdown
grade-checker/
├── main.py           # Main program
├── grade_checker.py  # Grade checking logic
└── examples/        # Example usage
```

## License
MIT License
