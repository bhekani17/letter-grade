def letter_grade(mark: int) -> str:
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

