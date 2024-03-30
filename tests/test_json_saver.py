import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from json_saver import JSONSaver


class TestJSONSaver(TestCase):

    @patch("os.makedirs")
    def test_init_creates_directory(self, mock_makedirs):
        JSONSaver("some/directory/vacancies.json")
        mock_makedirs.assert_called_once_with("some/directory", exist_ok=True)

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.makedirs")
    def test_add_vacancy_saves_data(self, mock_makedirs, mock_file):
        saver = JSONSaver("vacancies.json")
        vacancy = {"title": "Software Engineer", "company": "Test Company"}  # Пример объекта вакансии
        saver.add_vacancy(vacancy)

        # Проверяем, был ли файл открыт для записи
        mock_file.assert_called_once_with("vacancies.json", "w")
        # Проверяем, что в файл были записаны корректные данные
        handle = mock_file()
        handle.write.assert_called_once()
        written_data = json.loads(handle.write.call_args[0][0])
        self.assertEqual(written_data, [vacancy])

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.makedirs")
    def test_load_vacancies_returns_empty_list_on_new_file(self, mock_makedirs, mock_file):
        saver = JSONSaver("vacancies.json")
        vacancies = saver._load_vacancies()
        self.assertEqual(vacancies, [])
