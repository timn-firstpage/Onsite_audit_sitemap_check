import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("validator", Path(__file__).parents[1] / "scripts" / "validate_findings.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def record():
    return {"site_name": "Example", "site_url": "https://example.com", "audit_date": "2026-10-06", "checks": [
        {"id": f"11.{n}", "item_name": f"Checklist question {n}", "result": "Human check", "urls": [], "finding": "SF export missing", "action": "Provide completed export", "coverage": "No SF export available", "evidence": [], "screenshots": []}
        for n in range(1, 10)]}


class Validation(unittest.TestCase):
    def test_complete_unresolved_delivery_is_valid(self):
        self.assertEqual(module.validate(record()), [])

    def test_checklist_name_is_required(self):
        for value in (None, "", "   "):
            data = record()
            data["checks"][0]["item_name"] = value
            self.assertTrue(any("item_name required" in e for e in module.validate(data)))

    def test_missing_duplicate_and_blank_results_are_rejected(self):
        for mutation in (lambda d: d["checks"].pop(), lambda d: d["checks"][0].update(id="11.2"), lambda d: d["checks"][0].update(result="")):
            data = record()
            mutation(data)
            self.assertTrue(module.validate(data))

    def test_failure_requires_action_and_urls_are_absolute(self):
        data = record()
        data["checks"][0].update(result="X", action="", urls=["/relative"])
        errors = module.validate(data)
        self.assertTrue(any("action required" in e for e in errors))
        self.assertTrue(any("absolute" in e for e in errors))

    def test_malformed_values_report_errors_without_crashing(self):
        for field, value in (("id", []), ("result", {}), ("urls", [None])):
            data = record()
            data["checks"][0][field] = value
            self.assertTrue(module.validate(data))
        self.assertTrue(module.validate([]))


if __name__ == "__main__":
    unittest.main()
