from ucimlrepo import fetch_ucirepo
import pandas as pd

# fetch dataset
adult = fetch_ucirepo(id=2)

# data (as pandas dataframes)
X = pd.DataFrame(adult.data.features)
Y = pd.DataFrame(adult.data.targets)

# metadata
# print(adult.metadata)

# variable information
# print(adult.variables)
print(
    X[
        [
            "workclass",
            "education",
            "occupation",
        ]
    ]
)
print(Y)
