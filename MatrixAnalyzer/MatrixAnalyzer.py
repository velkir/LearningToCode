# Read CSV numeric data, construct matrix, compute summary stats + eigenvalues (with numpy).
# Output top‑2 eigenvalues & eigenvectors.
import numpy as np
import os.path


class MatrixAnalyzer:
    """This is a class to transform and analyze numeric data from csv-file."""
    def __init__(self):
        self.data = None

    def load_csv(self, csv_path, skip_header=1, delimiter=","):
        """Load numeric csv-data."""
        if os.path.exists(csv_path):
            data = np.genfromtxt(fname=csv_path,
                             delimiter=delimiter,
                             skip_header=skip_header)
            if np.isnan(data).any():
                raise ValueError(f"{csv_path} contains non-numeric values!")
            else:
                self.data = data
                return 1
        else:
            raise FileNotFoundError(f"{csv_path} not found!")

    def compute_statistics(self):
        """Aggregate all statistics methods and print their results."""
        stats_steps = [
            ("Range of values:", self.compute_range_of_values),
            ("Median:", self.compute_median),
            ("Standard deviation:", self.compute_std),
            ("Variance:", self.compute_variance)
        ]
        for step in stats_steps:
            print(step[0])
            print(step[1]())
            print()

    def compute_eigenvalues(self):
        """Check if matrix is square and compute eigenvalues."""
        if self.data.shape[-1]==self.data.shape[-2]:
            return np.linalg.eig(self.data)
        else:
            return 'Please provide a square matrix to compute eigen values.'

    def compute_range_of_values(self):
        return np.ptp(self.data)

    def compute_median(self):
        return np.median(self.data)

    def compute_std(self):
        return np.std(self.data)

    def compute_variance(self):
        return np.var(self.data)

csv_path = "numeric_data.csv"
matrixAnalyzer = MatrixAnalyzer()
matrixAnalyzer.load_csv(csv_path, skip_header=1, delimiter=",")
eugen = matrixAnalyzer.compute_eigenvalues()
std = matrixAnalyzer.compute_std()
range = matrixAnalyzer.compute_range_of_values()
median = matrixAnalyzer.compute_median()
var = matrixAnalyzer.compute_variance()
# matrixAnalyzer.compute_statistics()
# eigen = matrixAnalyzer.compute_eigenvalues()
pass

