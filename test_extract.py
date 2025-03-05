import test_extract_vowels

def extract_vowels(s):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return ''.join([char for char in s if char in vowels])

class TestExtractVowels(test_extract_vowels.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_vowels(""), "")

    def test_no_vowels(self):
        self.assertEqual(extract_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), "")

    def test_all_vowels(self):
        self.assertEqual(extract_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ"), "аеёиоуыэюяАЕЁИОУЫЭЮЯ")

    def test_mixed_case(self):
        self.assertEqual(extract_vowels("Hello, World!"), "ео")

    def test_russian_text(self):
        self.assertEqual(extract_vowels("Привет, мир!"), "иеи")

    def test_with_punctuation(self):
        self.assertEqual(extract_vowels("Это строка с запятыми, точками. и вопросительными знаками?"), "ороаеи")


if __name__ == '__main__':
    test_extract_vowels.main()
