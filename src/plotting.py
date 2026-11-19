import matplotlib.pyplot as plt


def plot_revenue_by_drink(df, save_path):
    """Create a bar chart of total revenue for each drink and save it."""
    revenue = df.groupby('drink')['revenue'].sum().sort_values()

    fig, ax = plt.subplots(figsize=(6, 4))
    revenue.plot.barh(ax=ax, color='purple')
    ax.set_title('Total Revenue by Drink')
    ax.set_xlabel('Revenue ($)')
    ax.set_ylabel('')
    fig.tight_layout()

    fig.savefig(save_path)
    plt.close(fig)
