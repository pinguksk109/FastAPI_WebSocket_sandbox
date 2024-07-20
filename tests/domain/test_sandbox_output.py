import unittest
from app.domain.sandbox_output import SandboxOutput
from app.domain.article import Article
from app.domain.organization import Organization

class TestSandboxOutput(unittest.TestCase):
    def setUp(self):
        self.output = SandboxOutput()
        self.organization = Organization(limit=100, count=10)
        self.article = Article(content="Test Article")

    def test_initial_state(self):
        self.assertIsNone(self.output.get_organization())
        self.assertIsNone(self.output.get_article())

    def test_set_and_get_organization(self):
        self.output.set_organization(self.organization)
        org = self.output.get_organization()
        self.assertIsNotNone(org)
        self.assertEqual(org.limit, 100)
        self.assertEqual(org.count, 10)

    def test_set_and_get_article(self):
        self.output.set_article(self.article)
        art = self.output.get_article()
        self.assertIsNotNone(art)
        self.assertEqual(art.content, "Test Article")

if __name__ == "__main__":
    unittest.main()
