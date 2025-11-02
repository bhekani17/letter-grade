def letter_grade(mark: int) -> str:

# Write a function called letter_grade(mark:int) -> str that returns a 
# letter a student got: 
# ○ A = 80–100 
# ○ B = 70–79 
# ○ C = 60–69 
# ○ D = 50–59 
# ○ F = below 50 
# Write unit tests to test if the function returns the expected. 
# the file structure of the program must be 
# letter.py 
# test_letter.py

    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100")
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"
print(letter_grade(60))

