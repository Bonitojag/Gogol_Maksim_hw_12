def capitalize_string(input_string):
    """�������, ������� ��������� �� ���� ������ � ���������� �� �� ����� ���������� �������"""
    return input_string.upper()

def capitalize_first_letter(s):
    """�������, ������� ������ ���������� ������ ����� ������� ����� � ������, ����������� �� ���� �������."""
    return ' '.join(word.capitalize() for word in s.split())
