from unittest.mock import patch
from main import get_top_vacancies, find_vacancies_by_keyword, user_interaction, Vacancy

def test_get_top_vacancies():
    vacancies_list = [
        Vacancy("Vacancy 1", "http://example.com", {"from": 2000}, ""),
        Vacancy("Vacancy 2", "http://example.com", {"from": 1000}, ""),
    ]
    top_vacancies = get_top_vacancies(vacancies_list, 1)
    assert len(top_vacancies) == 1
    assert top_vacancies[0].min_salary == 2000

def test_find_vacancies_by_keyword():
    vacancies_list = [
        Vacancy("Vacancy 1", "http://example.com", None, "We need Python developer"),
        Vacancy("Vacancy 2", "http://example.com", None, "Java position"),
    ]
    filtered_vacancies = find_vacancies_by_keyword(vacancies_list, "Python")
    assert len(filtered_vacancies) == 1
    assert "Python" in filtered_vacancies[0].description

@patch('builtins.input', side_effect=['Python developer', '2', 'Python', 'да'])
@patch('builtins.print')
@patch('your_script.JSONSaver.add_vacancy')
@patch('your_script.HeadHunterAPI.get_vacancies', return_value={"items": []})
def test_user_interaction(mock_get_vacancies, mock_add_vacancy, mock_print, mock_input):
    user_interaction()
    mock_get_vacancies.assert_called_once_with('Python developer')
    mock_add_vacancy.assert_called()  # Check if add_vacancy was called, indicating save attempt
