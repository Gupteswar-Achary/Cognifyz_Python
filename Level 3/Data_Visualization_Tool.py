import pandas as pd
import plotly.express as px


def load_dataset(file_path):
    """
    Load dataset from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def generate_scatter_plot(df, x_column, y_column, color_column=None):
    """
    Generate an interactive scatter plot.
    """
    fig = px.scatter(df, x=x_column, y=y_column, color=color_column, title=f"Scatter Plot: {x_column} vs {y_column}")
    fig.show()


def generate_line_plot(df, x_col, y_col, color_column=None):
    """
    Generate an interactive line plot.
    """
    fig = px.line(df, x=x_col, y=y_col, color=color_column, title=f"Line Plot: {x_col} vs {y_col}")
    fig.show()


def generate_histogram(df, column, color_column=None):
    """
    Generate an interactive histogram.
    """
    fig = px.histogram(df, x=column, color=color_column, title=f"Histogram: {column}")
    fig.show()


def generate_bar_chart(df, x_column, y_column, color_column=None):
    """
    Generate an interactive bar chart.
    """
    fig = px.bar(df, x=x_column, y=y_column, color=color_column, title=f"Bar Chart: {x_column} vs {y_column}")
    fig.show()


def main():
    # Example usage
    file_path = 'Book_ipl.csv'  # Change this to your dataset path
    df = load_dataset(file_path)

    if df is not None:
        # Example visualizations using specific columns
        x_column = 'first_ings_score'
        y_column = 'second_ings_score'
        color_column = None  # Set this to a column name if you want to color by another variable

        generate_scatter_plot(df, x_column=x_column, y_column=y_column, color_column=color_column)
        generate_line_plot(df, x_col='first_ings_wkts', y_col='second_ings_wkts', color_column=color_column)
        generate_histogram(df, column=x_column, color_column=color_column)
        generate_bar_chart(df, x_column=x_column, y_column=y_column, color_column=color_column)


if __name__ == "__main__":
    main()
