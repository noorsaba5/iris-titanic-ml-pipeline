import plotly.graph_objects as go

# Create a simple line plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5],
                         y=[10, 11, 12, 13, 14],
                         mode='lines', name='Line Plot'))

# Add title and labels
fig.update_layout(
    title='Simple Line Chart',
    xaxis_title='X-axis Label',
    yaxis_title='Y-axis Label'
)

# Show plot
fig.show()