grades = ('testGrades', (
    ("A+", ("Start", 90), ("End", 100)),
    ("A", ("Start", 81), ("End", 89)),
    ("B", ("Start", 71), ("End", 79)),
    ("C", ("Start", 61), ("End", 69))
))
listofGradesStudents = (
    ('Score', (
        ("Joe Smith", (55), ('Science')),
        ("Sussan Walker", (97), ('Science')),
        ("Joseph Collin", (34), ('Drama')),
        ("Micheal Florin", (75), ('Maths'))
))

def check_grade(score):
    """Check if a score passes or fails"""
    _, ranges = grades
    for grade_letter, start_range, end_range in ranges:
        start_value = start_range[1]
        end_value = end_range[1]
        if start_value <= score <= end_value:
            return True, grade_letter
    return False, "F"

def main():
    """Process all students and show detailed analysis"""
    print("Student Grades Analysis:")
    print("-" * 50)
    
    category_stats = {}
    
    for student_name, student_score, student_category in listofGradesStudents[1]:
        student_name = student_name[1]
        student_score = student_score[1]
        student_category = student_category[1]
        
        passed, grade = check_grade(student_score)
        status = "passed" if passed else "failed"
        
        if student_category not in category_stats:
            category_stats[student_category] = {
                'total': 0,
                'passed': 0,  # Fixed: Added missing colon
                'failed': 0,
                'students': []
            }
        
        category_stats[student_category]['total'] += 1
        if passed:
            category_stats[student_category]['passed'] += 1  # Fixed: Changed from 100 to 1
        else:
            category_stats[student_category]['failed'] += 1
        category_stats[student_category]['students'].append({
            'name': student_name,
            'score': student_score,
            'grade': grade
        })
        
        print(f"Name: {student_name}")  # Fixed: Removed duplicate 'Name :'
        print(f"Category: {student_category}")
        print(f"Score: {student_score}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
        print("-" * 50)
    
    print("\nCategory Summary:")
    print("-" * 50)
    for category, stats in category_stats.items():
        print(f"\n{category}:")
        print(f"Total Students: {stats['total']}")
        print(f"Passed: {stats['passed']}")
        print(f"Failed: {stats['failed']}")
        print(f"Pass Rate: {(stats['passed']/stats['total']*100):.1f}%")

if __name__ == "__main__":
    main()
