"""Backward-compatible entry point for v0.4 validation commands."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from css.cli import main
raise SystemExit(main(['validate']))
