import unittest
import pandas as pd
from inventorytools import combine_dublicate_entries


class TestCombineDuplicateEntries(unittest.TestCase):
    def setUp(self):
        self.uncombined_df = pd.DataFrame(
            {
                "Brand": ["Straumann", "Straumann", "Straumann"],
                "Reference": ["21.2508", "21.2508", "21.3308"],
                "Quantity": [2, 4, 30],
            }
        )
        self.combined_df = pd.DataFrame(
            {
                "Brand": ["Straumann", "Straumann"],
                "Reference": ["21.2508", "21.3308"],
                "Quantity": [6, 30],
            }
        )

    def test_combine_duplicate_entries(self):
        output_df = combine_dublicate_entries(self.uncombined_df)
        pd.testing.assert_frame_equal(
            output_df,
            self.combined_df,
            obj="Output DataFrame does not match the expected combined DataFrame.",
        )


if __name__ == "__main__":
    unittest.main()
