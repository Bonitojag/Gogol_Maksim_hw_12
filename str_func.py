def capitalize_string(input_string):
    """Функцию, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return input_string.upper()

def capitalize_first_letter(s):
    """Функцию, которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции."""
    return ' '.join(word.capitalize() for word in s.split())
