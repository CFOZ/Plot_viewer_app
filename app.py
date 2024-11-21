import matplotlib.pyplot as plt
import numpy as np
import panel as pn
from io import BytesIO

# Enable Panel extension
pn.extension()

# Step 1: Define some example datasets
datasets = {
    "Dataset 1": np.random.rand(10),
    "Dataset 2": np.random.rand(10),
    "Dataset 3": np.random.rand(10),
    "Dataset 4": np.random.rand(10),
    "Dataset 5": np.random.rand(10),
}

# Step 2: Create a function to plot selected datasets
def create_plot(dataset_name):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(datasets[dataset_name], marker='o')
    ax.set_title(dataset_name)
    
    # Save plot to a buffer and display as Panel Image
    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    return pn.pane.PNG(buf.getvalue(), width=300)

# Step 3: Create widgets to select datasets
dataset_selector = pn.widgets.MultiChoice(
    name="Select Datasets to Display",
    options=list(datasets.keys()),
    value=["Dataset 1", "Dataset 2"]
)

# Step 4: Define a function to update plots based on selected datasets
@pn.depends(dataset_selector)
def update_plots(selected_datasets):
    plots = [create_plot(name) for name in selected_datasets]
    return pn.Row(*plots)

# Step 5: Set up the layout of the app
app = pn.Column(
    pn.pane.Markdown("# Interactive Plot Viewer"),
    dataset_selector,
    update_plots
)

# Step 6: Serve the app
app.servable()
