from datetime import date

def calculate_age(birth_date_str):
    """
    Calculates the age in years given a birthdate string in 'YYYY-MM-DD' format.
    """
    try:
        birth_year, birth_month, birth_day = map(int, birth_date_str.split('-'))
        birth_date = date(birth_year, birth_month, birth_day)
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    today = date.today()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

# Example usage:
birth_date_input = "2006-03-07"
age_calculated = calculate_age(birth_date_input)
print(f"The age is: {age_calculated}")