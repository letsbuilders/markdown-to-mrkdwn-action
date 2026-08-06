from unittest import TestCase

from src.main import convert


class Test(TestCase):
    def test_convert(self):
        self.assertEqual(convert('### Test'), '*Test*')

    def test_remove_comment(self):
        test_text = '''<!-- Release notes generated using configuration in .github/release.yml at v2026.3.12-2 -->\r\n\r\n## What's Changed\r\n### Tech changes\r\n* inherit secrets by @PatTheSilent in https://github.com/letsbuilders/release-test/pull/4\r\n\r\n\r\n**Full Changelog**: https://github.com/letsbuilders/release-test/compare/v2026.3.12-1...v2026.3.12-2'''

        expected = '''\n\n*What's Changed*\n*Tech changes*\n• inherit secrets by @PatTheSilent in https://github.com/letsbuilders/release-test/pull/4\n\n\n*Full Changelog*: https://github.com/letsbuilders/release-test/compare/v2026.3.12-1...v2026.3.12-2'''
        self.assertEqual(convert(test_text), expected)

    def test_escape_double_quotes(self):
        test_text = '''Revert "XXXX-9999 - Sort projects by IsActive flag" by @xxx'''
        expected = r'''Revert \"XXXX-9999 - Sort projects by IsActive flag\" by @xxx'''
        self.assertEqual(convert(test_text), expected)
