def letter_grade(num):
    if num < 0 or num > 100:
        return 'Invalid grade'
    else:
        if num < 60:
            return 'F'
        elif num >= 60 and num <= 62:
            return 'D-'
        elif num >= 63 and num <= 66:
            return 'D'
        elif num >= 67 and num <= 69:
            return 'D+'
        elif num >= 70 and num <= 72:
            return 'C-'
        elif num >= 73 and num <= 76:
            return 'C'
        elif num >= 77 and num <= 79:
            return 'C+'
        elif num >= 80 and num <= 82:
            return 'B-'
        elif num >= 83 and num <= 86:
            return 'B'
        elif num >= 87 and num <= 89:
            return 'B+'
        elif num >= 90 and num <= 92:
            return 'A-'
        elif num >= 93 and num <= 96:
            return 'A'
        else:
            return 'A+'

grade_num = float(input('Numeric Grade: '))
print('Letter Grade:',letter_grade(grade_num))