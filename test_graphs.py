import unittest
import os
from graph_app import generate_bar_chart, generate_pie_chart

class TestGraphApp(unittest.TestCase):

    def test_generate_bar_chart(self):
        """Test the generate_bar_chart function."""
        sample_data = [1, 2, 3, 4, 5]
        sample_labels = ['A', 'B', 'C', 'D', 'E']
        chart_title = "Test Bar Chart"

        file_path = None
        try:
            file_path = generate_bar_chart(sample_data, sample_labels, chart_title)

            self.assertTrue(os.path.exists(file_path), "Chart file was not created.")
            self.assertTrue(file_path.endswith(".png"), "Chart file does not have a .png extension.")

            # Further checks could involve image analysis if libraries are available
            # For now, existence and extension are the main checks.

        finally:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)

    def test_generate_pie_chart(self):
        """Test the generate_pie_chart function."""
        sample_data = [10, 20, 30, 40]
        sample_labels = ['X', 'Y', 'Z', 'W']
        chart_title = "Test Pie Chart"

        file_path = None
        try:
            file_path = generate_pie_chart(sample_data, sample_labels, chart_title)

            self.assertTrue(os.path.exists(file_path), "Chart file was not created.")
            self.assertTrue(file_path.endswith(".png"), "Chart file does not have a .png extension.")

        finally:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
