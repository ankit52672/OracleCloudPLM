import unittest

from oracle_cloud_plm_mcp.server import build_resource_url


class BuildResourceUrlTests(unittest.TestCase):
    def test_builds_url_with_query_parameters(self) -> None:
        url = build_resource_url(
            "https://tenant.example.com",
            "fscmRestApi/resources/latest/items",
            {"q": "ItemNumber=100"},
        )

        self.assertEqual(
            url,
            "https://tenant.example.com/fscmRestApi/resources/latest/items?q=ItemNumber%3D100",
        )

    def test_rejects_non_https_or_pathful_base_url(self) -> None:
        for base_url in (
            "http://tenant.example.com",
            "https://tenant.example.com/api",
            "https://user:password@tenant.example.com",
        ):
            with self.subTest(base_url=base_url):
                with self.assertRaises(ValueError):
                    build_resource_url(base_url, "fscmRestApi/resources/latest/items")

    def test_rejects_absolute_and_traversal_resource_paths(self) -> None:
        for resource_path in (
            "https://other.example.com/data",
            "../admin",
            "fscmRestApi/../admin",
            "/fscmRestApi/resources/latest/items",
        ):
            with self.subTest(resource_path=resource_path):
                with self.assertRaises(ValueError):
                    build_resource_url("https://tenant.example.com", resource_path)


if __name__ == "__main__":
    unittest.main()

