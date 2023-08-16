from django.test import TestCase
from .forms import PaperForm
from paper.models import Author

# Тестовые данные
authors = Author.objects.all()
valid_data = {
    "code": "КП 081/20",
    "title": "Холодно в лесу",
    "subtitle": "Как я замерз в лесу",
    "year_start": 1930,
    "url": "https://example.com",
    "authors": [authors[0].pk],
}


# Create your tests here.
class PaperFormTest(TestCase):
    fixtures = ["paper/fixtures/authors.json"]

    def test_valid_form(self):
        data = valid_data.copy()
        form = PaperForm(data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        data = valid_data.copy()
        data.pop("code")
        form = PaperForm(data)
        self.assertFalse(form.is_valid())

    def test_save_form(self):
        data = valid_data.copy()
        form = PaperForm(data)
        if not form.is_valid():
            print(form.errors)
        paper = form.save()
        self.assertEqual(paper.code, data["code"])
