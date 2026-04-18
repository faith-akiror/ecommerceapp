#!/usr/bin/env python
"""Test script to verify app can be imported."""

try:
    import app.main
    print("✓ IMPORT_SUCCESS: app.main imported successfully")
except ImportError as e:
    print(f"✗ IMPORT_ERROR: {e}")
except Exception as e:
    print(f"✗ ERROR: {type(e).__name__}: {e}")
