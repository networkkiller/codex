import matplotlib.pyplot as plt
import tempfile

def generate_bar_chart(data, labels, title):
  """
  Generates a bar chart and saves it to a temporary PNG file.

  Args:
    data: A list of numerical data for the bar chart.
    labels: A list of labels for the x-axis.
    title: The title of the chart.

  Returns:
    The path to the saved PNG file.
  """
  fig, ax = plt.subplots()
  ax.bar(labels, data)
  ax.set_ylabel("Values")
  ax.set_title(title)

  # Create a temporary file to save the chart
  temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
  chart_path = temp_file.name
  temp_file.close() # Close the file so matplotlib can write to it

  fig.savefig(chart_path)
  plt.close(fig)

  return chart_path

if __name__ == '__main__':
  # Example Usage (optional - for testing)
  sample_data = [10, 25, 15, 30, 20]
  sample_labels = ['A', 'B', 'C', 'D', 'E']
  chart_title = "Sample Bar Chart"

  # Generate the chart
  image_path = generate_bar_chart(sample_data, sample_labels, chart_title)
  print(f"Bar chart saved to: {image_path}")

  # To verify, you would typically open the image_path file.
  # For automated testing, you might check if the file exists and is a valid PNG.
  import os
  if os.path.exists(image_path) and image_path.endswith(".png"):
    print("Test: Chart generated successfully.")
    # os.remove(image_path) # Clean up the temp file after verification
  else:
    print("Test: Chart generation failed.")

def generate_pie_chart(data, labels, title):
  """
  Generates a pie chart and saves it to a temporary PNG file.

  Args:
    data: A list of numerical data for the pie chart.
    labels: A list of labels for the slices.
    title: The title of the chart.

  Returns:
    The path to the saved PNG file.
  """
  fig, ax = plt.subplots()
  ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
  ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  ax.set_title(title)

  # Create a temporary file to save the chart
  temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
  chart_path = temp_file.name
  temp_file.close() # Close the file so matplotlib can write to it

  fig.savefig(chart_path)
  plt.close(fig)

  return chart_path

if __name__ == '__main__':
  # Example Usage (optional - for testing)
  sample_data_bar = [10, 25, 15, 30, 20]
  sample_labels_bar = ['A', 'B', 'C', 'D', 'E']
  chart_title_bar = "Sample Bar Chart"

  # Generate the bar chart
  image_path_bar = generate_bar_chart(sample_data_bar, sample_labels_bar, chart_title_bar)
  print(f"Bar chart saved to: {image_path_bar}")

  if os.path.exists(image_path_bar) and image_path_bar.endswith(".png"):
    print("Test: Bar chart generated successfully.")
  else:
    print("Test: Bar chart generation failed.")

  # Example Usage for Pie Chart
  sample_data_pie = [30, 20, 25, 15, 10]
  sample_labels_pie = ['X', 'Y', 'Z', 'W', 'V']
  chart_title_pie = "Sample Pie Chart"

  # Generate the pie chart
  image_path_pie = generate_pie_chart(sample_data_pie, sample_labels_pie, chart_title_pie)
  print(f"Pie chart saved to: {image_path_pie}")

  if os.path.exists(image_path_pie) and image_path_pie.endswith(".png"):
    print("Test: Pie chart generated successfully.")
  else:
    print("Test: Pie chart generation failed.")
