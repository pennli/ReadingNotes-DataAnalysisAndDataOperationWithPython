import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from sklearn.preprocessing import FunctionTransformer
from copy import copy

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=0)

# Average CV score on the training set was:0.9912280701754387
exported_pipeline = make_pipeline(
    make_union(
        FunctionTransformer(copy),
        StackingEstimator(estimator=make_pipeline(
            make_union(
                FunctionTransformer(copy),
                FunctionTransformer(copy)
            ),
            KNeighborsClassifier(n_neighbors=35, p=1, weights="uniform")
        ))
    ),
    KNeighborsClassifier(n_neighbors=5, p=2, weights="distance")
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
