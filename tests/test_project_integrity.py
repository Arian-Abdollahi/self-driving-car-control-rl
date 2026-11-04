"""Dependency-free tests for the preserved Webots research source tree."""
from __future__ import annotations

import ast
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProjectIntegrityTests(unittest.TestCase):
    def test_core_phase_entry_points_exist(self):
        paths = [
            "phase1_CNN.py",
            "phase1_Resnet/vehicle_driver.py",
            "phase2_CNN/train.py",
            "phase2_CNN/test.py",
            "phase2_Resnet/vehicle_driver.py",
            "phase3_Resnet/controllers/highway_overtake/highway_overtake.py",
        ]
        for name in paths:
            with self.subTest(source=name):
                self.assertTrue((ROOT / name).is_file(), name)

    def test_python_files_are_parseable(self):
        files = sorted(ROOT.rglob("*.py"))
        self.assertGreaterEqual(len(files), 10)
        for path in files:
            with self.subTest(source=path.relative_to(ROOT).as_posix()):
                ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))

    def test_notebooks_are_valid_json(self):
        notebooks = sorted(ROOT.rglob("*.ipynb"))
        self.assertTrue(notebooks)
        for notebook in notebooks:
            with self.subTest(source=notebook.name):
                data = json.loads(notebook.read_text(encoding="utf-8"))
                self.assertIn("cells", data)
                self.assertIsInstance(data["cells"], list)

    def test_webots_sumo_assets_exist(self):
        paths = [
            "phase3_Resnet/worlds/highway_overtake.wbt",
            "phase3_Resnet/worlds/highway_overtake_net/sumo.net.xml",
            "phase3_Resnet/worlds/highway_overtake_net/sumo.rou.xml",
            "phase3_Resnet/controllers/sumo_supervisor/sumo_supervisor.py",
        ]
        for name in paths:
            with self.subTest(asset=name):
                self.assertGreater((ROOT / name).stat().st_size, 0)

    def test_third_party_notice_preserved(self):
        path = ROOT / "phase3_Resnet/controllers/sumo_supervisor/SumoSupervisor.py"
        text = path.read_text(encoding="utf-8")
        self.assertIn("Copyright", text)
        self.assertIn("Apache License", text)


if __name__ == "__main__":
    unittest.main()
