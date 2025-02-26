import  test_extract_vowels2


def extract_vowels(s):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return ''.join([char for char in s if char in vowels])

class TestExtractVowels(test_extract_vowels2.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_vowels(""), "")

    def test_no_vowels(self):
        self.assertEqual(extract_vowels("бвгджзйклмнпрстфхцчшщ"), "")

    def test_all_vowels(self):
        self.assertEqual(extract_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ"), "аеёиоуыэюяАЕЁИОУЫЭЮЯ")

    def test_mixed_case(self):
        self.assertEqual(extract_vowels("пРиВеТ МиР"), "иеи")

    def test_with_spaces(self):
        self.assertEqual(extract_vowels("здра вствуйте"), "аууе")

    def test_with_numbers_and_symbols(self):
        self.assertEqual(extract_vowels("ч1т0 д3л@ешь?"), "еа")


if __name__ == '__main__':
    extract_vowels.main()
