import test_remove_duplicates


def remove_duplicates(s):
    return "".join(sorted(set(s), key=s.index))


class TestRemoveDuplicates(remove_duplicates.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_duplicates(""), "")

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates("abcdefg"), "abcdefg")

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates("aaaaaaa"), "a")

    def test_leading_duplicates(self):
        self.assertEqual(remove_duplicates("aaabbc"), "abc")

    def test_trailing_duplicates(self):
        self.assertEqual(remove_duplicates("abccc"), "abc")

    def test_mixed_duplicates(self):
        self.assertEqual(remove_duplicates("abacabadabacabae"), "abce")

    def test_with_spaces(self):
        self.assertEqual(remove_duplicates("hello world hello"),"helo wrd")

    def test_numbers_and_symbols(self):
        self.assertEqual(remove_duplicates("123!@#123"), "123!@#")


if __name__ == '__main__':
   remove_duplicates.main()

