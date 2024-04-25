import csv
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LabelSet


data = [
    ["Country", "City", "Share of green areas in FUA's urban centres", "Well-being of population out of 10"],
    ["Finland", "Helsinki", 54.9, 7.828],
    ["Denmark", "Århus", 47.5, 7.625],
    ["New Zealand", "Wellington", 57.8, 7.553],
    ["Switzerland", "Zurich", 54.7, 7.541],
    ["Denmark", "København", 47.5, 7.530],
    ["Norway", "Bergen", 65.6, 7.527],
    ["Norway", "Oslo", 53.1, 7.527],
    ["Sweden", "Stockholm", 60.5, 7.373],
    ["Iceland", "Reykjavík", 53.5, 7.317],
    ["Canada", "Toronto", 41.7, 7.232],
    ["Australia", "Greater Melbourne", 43.7, 7.296],
    ["New Zealand", "Auckland", 45.6, 7.232],
    ["New Zealand", "Christchurch", 33.7, 7.191],
    ["United States of America", "Washington (Greater)", 64, 7.185],
    ["United States of America", "Dallas", 45.8, 7.155],
    ["Austalia", "Greater Sydney", 47.3, 7.133],
    ["United States of America", "Houston", 55.1, 7.110],
    ["Ireland", "Dublin", 48.4, 7.096],
    ["Sweden", "Göteborg", 57.5, 7.080],
    ["United States of America", "Chicago", 50.4, 7.033],
    ["United States of America", "Atlanta", 64, 7.031],
    ["United States of America", "Miami (Greater)", 33.7, 7.028],
    ["United States of America", "New York (Greater)", 55.7, 6.959],
    ["United States of America", "Los Angeles", 25.6, 6.956],
    ["Ireland", "Cork", 53.1, 6.946],
    ["United Kingdom", "London", 52.5, 6.782],
    ["Chile", "Santiago", 19.2, 6.770],
    ["Mexico", "Mexico City", 25.4, 6.693],
    ["Belgium", "Brussels", 87, 6.674],
    ["France", "Paris", 43.6, 6.635],
    ["Czechia", "Praha", 49.3, 6.620],
    ["Colombia", "Bogota D.C", 33.1, 6.612],
    ["Spain", "Madrid", 37.2, 6.500],
    ["Slovakia", "Bratislava", 47.3, 6.383],
    ["Spain", "Barcelona", 41.2, 6.380],
    ["Lithuania", "Vilnius", 54.1, 6.163],
    ["Romania", "Bucharest", 33.4, 5.974],
    ["Greece", "Thessalooniki", 25.6, 5.778],
    ["Türkiye", "Ankara", 34.1, 5.749],
    ["Estonia", "Tallinn", 50, 5.679],
    
]


with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")

data = pd.read_csv('data.csv')

source = ColumnDataSource(data)

p = figure(title="Scatter Plot of Green Area per Capita vs. Well-being of Population",
           x_axis_label="Share of green areas in FUA's urban centres",
           y_axis_label="Well-being of population")

p.circle("Share of green areas in FUA's urban centres", "Well-being of population out of 10", size=10, source=source, color='green', alpha=0.7)

# Add labels for selected points
selected_indices = [0, 10, 20, 30]  # Indices of points to annotate

# Create a list of tuples containing x, y coordinates, and text labels
annotations = [(data["Share of green areas in FUA's urban centres"][i], data["Well-being of population out of 10"][i], f"{data['City'][i]}, {data['Country'][i]}") for i in selected_indices]

# Ensure annotations are provided as a list of tuples
labels = LabelSet(x='x', y='y', text='text', level='glyph',
                  x_offset=5, y_offset=5, source=ColumnDataSource({'x': [], 'y': [], 'text': []}), text_font_size='8pt')

p.add_layout(labels)

# Show the plot
show(p)