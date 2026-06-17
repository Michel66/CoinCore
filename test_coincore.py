# test_coincore.py
"""
Tests for CoinCore module.
"""

import unittest
from coincore import CoinCore

class TestCoinCore(unittest.TestCase):
    """Test cases for CoinCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinCore()
        self.assertIsInstance(instance, CoinCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
