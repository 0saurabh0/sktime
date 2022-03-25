# -*- coding: utf-8 -*-
"""Dictionaries of expected outputs of classifier predict runs."""

import numpy as np

# predict_proba results on unit test data
unit_test_proba = dict()

# predict_proba results on basic motions data
basic_motions_proba = dict()


unit_test_proba["BOSSEnsemble"] = np.array(
    [
        [0.4, 0.6],
        [0.4, 0.6],
        [0.2, 0.8],
        [1.0, 0.0],
        [1.0, 0.0],
        [0.8, 0.2],
        [0.8, 0.2],
        [0.2, 0.8],
        [1.0, 0.0],
        [1.0, 0.0],
    ]
)
unit_test_proba["ContractableBOSS"] = np.array(
    [
        [0.1126, 0.8874],
        [0.603, 0.397],
        [0.0, 1.0],
        [0.7747, 0.2253],
        [0.6621, 0.3379],
        [0.7747, 0.2253],
        [0.2843, 0.7157],
        [0.0, 1.0],
        [0.1717, 0.8283],
        [0.603, 0.397],
    ]
)
unit_test_proba["TemporalDictionaryEnsemble"] = np.array(
    [
        [0.0, 1.0],
        [0.4924, 0.5076],
        [0.0, 1.0],
        [0.9043, 0.0957],
        [0.8016, 0.1984],
        [1.0, 0.0],
        [0.706, 0.294],
        [0.0, 1.0],
        [0.8016, 0.1984],
        [1.0, 0.0],
    ]
)
unit_test_proba["WEASEL"] = np.array(
    [
        [0.2377, 0.7623],
        [0.6074, 0.3926],
        [0.0888, 0.9112],
        [0.9386, 0.0614],
        [0.926, 0.074],
        [0.9219, 0.0781],
        [0.2119, 0.7881],
        [0.1245, 0.8755],
        [0.8867, 0.1133],
        [0.9241, 0.0759],
    ]
)
unit_test_proba["ElasticEnsemble"] = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.6667, 0.3333],
        [1.0, 0.0],
        [0.6667, 0.3333],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
    ]
)
unit_test_proba["ProximityForest"] = np.array(
    [
        [0.0, 1.0],
        [0.6667, 0.3333],
        [0.0, 1.0],
        [0.3333, 0.6667],
        [0.6667, 0.3333],
        [1.0, 0.0],
        [0.6667, 0.3333],
        [0.0, 1.0],
        [0.6667, 0.3333],
        [1.0, 0.0],
    ]
)
unit_test_proba["ShapeDTW"] = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
    ]
)
unit_test_proba["Catch22Classifier"] = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
        [0.1, 0.9],
        [0.8, 0.2],
        [0.6, 0.4],
        [0.9, 0.1],
        [0.6, 0.4],
        [0.2, 0.8],
        [0.8, 0.2],
        [0.8, 0.2],
    ]
)
unit_test_proba["MatrixProfileClassifier"] = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [0.0, 1.0],
        [0.0, 1.0],
        [0.0, 1.0],
    ]
)
unit_test_proba["RandomIntervalClassifier"] = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [0.2, 0.8],
        [0.8, 0.2],
        [1.0, 0.0],
    ]
)
unit_test_proba["SignatureClassifier"] = np.array(
    [
        [0.1, 0.9],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.9, 0.1],
        [0.8, 0.2],
        [0.8, 0.2],
        [0.0, 1.0],
        [0.8, 0.2],
        [1.0, 0.0],
    ]
)
unit_test_proba["SummaryClassifier"] = np.array(
    [
        [0.0, 1.0],
        [0.9, 0.1],
        [0.0, 1.0],
        [0.9, 0.1],
        [0.9, 0.1],
        [1.0, 0.0],
        [0.8, 0.2],
        [0.6, 0.4],
        [0.9, 0.1],
        [1.0, 0.0],
    ]
)
unit_test_proba["HIVECOTEV1"] = np.array(
    [
        [0.0, 1.0],
        [0.5524, 0.4476],
        [0.0, 1.0],
        [0.8285, 0.1715],
        [0.8839, 0.1161],
        [0.9746, 0.0254],
        [0.7181, 0.2819],
        [0.0, 1.0],
        [0.7911, 0.2089],
        [0.7167, 0.2833],
    ]
)
unit_test_proba["HIVECOTEV2"] = np.array(
    [
        [0.0, 1.0],
        [0.4563, 0.5437],
        [0.0379, 0.9621],
        [1.0, 0.0],
        [0.719, 0.281],
        [1.0, 0.0],
        [0.8477, 0.1523],
        [0.0379, 0.9621],
        [0.6902, 0.3098],
        [1.0, 0.0],
    ]
)
unit_test_proba["CanonicalIntervalForest"] = np.array(
    [
        [0.41, 0.59],
        [0.7333, 0.2667],
        [0.1833, 0.8167],
        [0.7667, 0.2333],
        [0.5, 0.5],
        [0.76, 0.24],
        [0.8, 0.2],
        [0.2833, 0.7167],
        [0.86, 0.14],
        [0.7, 0.3],
    ]
)
unit_test_proba["DrCIF"] = np.array(
    [
        [0.0, 1.0],
        [0.8, 0.2],
        [0.2, 0.8],
        [1.0, 0.0],
        [0.7, 0.3],
        [0.9, 0.1],
        [0.9, 0.1],
        [0.3, 0.7],
        [0.8, 0.2],
        [1.0, 0.0],
    ]
)
unit_test_proba["RandomIntervalSpectralEnsemble"] = np.array(
    [
        [0.1, 0.9],
        [0.8, 0.2],
        [0.0, 1.0],
        [0.7, 0.3],
        [1.0, 0.0],
        [1.0, 0.0],
        [0.6, 0.4],
        [0.0, 1.0],
        [0.7, 0.3],
        [0.9, 0.1],
    ]
)
unit_test_proba["SupervisedTimeSeriesForest"] = np.array(
    [
        [0.0, 1.0],
        [0.8, 0.2],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [0.1, 0.9],
        [1.0, 0.0],
        [1.0, 0.0],
    ]
)
unit_test_proba["TimeSeriesForestClassifier"] = np.array(
    [
        [0.1, 0.9],
        [0.7, 0.3],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.8, 0.2],
        [1.0, 0.0],
        [0.8, 0.2],
        [0.0, 1.0],
        [0.8, 0.2],
        [0.9, 0.1],
    ]
)
unit_test_proba["Arsenal"] = np.array(
    [
        [-0.0, 1.0],
        [1.0, -0.0],
        [-0.0, 1.0],
        [1.0, -0.0],
        [0.9236, 0.0764],
        [1.0, -0.0],
        [0.4506, 0.5494],
        [-0.0, 1.0],
        [1.0, -0.0],
        [1.0, -0.0],
    ]
)
unit_test_proba["RocketClassifier"] = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.0],
    ]
)
unit_test_proba["ShapeletTransformClassifier"] = np.array(
    [
        [0.0, 1.0],
        [0.4, 0.6],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.8, 0.2],
        [1.0, 0.0],
        [0.8, 0.2],
        [0.0, 1.0],
        [0.8, 0.2],
        [1.0, 0.0],
    ]
)

basic_motions_proba["ColumnEnsembleClassifier"] = np.array(
    [
        [0.0, 0.0, 0.25, 0.75],
        [0.25, 0.0, 0.3325, 0.4175],
        [0.0, 0.0, 0.3325, 0.6675],
        [0.5, 0.0, 0.0825, 0.4175],
        [0.0, 0.0, 0.5, 0.5],
        [0.0, 0.0, 0.5, 0.5],
        [0.25, 0.25, 0.0825, 0.4175],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.5, 0.0825, 0.4175],
        [0.0, 0.25, 0.0825, 0.6675],
    ]
)
basic_motions_proba["MUSE"] = np.array(
    [
        [0.0019, 0.0013, 0.0009, 0.9959],
        [0.8212, 0.0796, 0.0336, 0.0657],
        [0.0111, 0.0098, 0.9602, 0.019],
        [0.0576, 0.9091, 0.0143, 0.019],
        [0.0032, 0.0049, 0.0021, 0.9898],
        [0.0036, 0.0016, 0.0026, 0.9922],
        [0.8459, 0.0698, 0.0328, 0.0514],
        [0.0562, 0.0186, 0.8846, 0.0405],
        [0.0573, 0.9249, 0.0102, 0.0076],
        [0.0106, 0.9833, 0.004, 0.0022],
    ]
)
basic_motions_proba["TemporalDictionaryEnsemble"] = np.array(
    [
        [0.0, 0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.6261, 0.3739, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.7478, 0.0, 0.0, 0.2522],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.7478, 0.2522, 0.0],
        [0.0, 0.7478, 0.2522, 0.0],
    ]
)
basic_motions_proba["Catch22Classifier"] = np.array(
    [
        [0.0, 0.2, 0.2, 0.6],
        [0.0, 0.9, 0.0, 0.1],
        [0.2, 0.2, 0.3, 0.3],
        [0.2, 0.5, 0.3, 0.0],
        [0.0, 0.2, 0.1, 0.7],
        [0.0, 0.0, 0.4, 0.6],
        [0.2, 0.4, 0.2, 0.2],
        [0.1, 0.0, 0.7, 0.2],
        [0.1, 0.7, 0.1, 0.1],
        [0.0, 0.9, 0.0, 0.1],
    ]
)
basic_motions_proba["RandomIntervalClassifier"] = np.array(
    [
        [0.0, 0.0, 0.2, 0.8],
        [0.3, 0.1, 0.1, 0.5],
        [0.0, 0.0, 0.8, 0.2],
        [0.2, 0.7, 0.0, 0.1],
        [0.0, 0.1, 0.4, 0.5],
        [0.0, 0.0, 0.4, 0.6],
        [0.2, 0.3, 0.1, 0.4],
        [0.0, 0.1, 0.9, 0.0],
        [0.1, 0.8, 0.0, 0.1],
        [0.1, 0.7, 0.0, 0.2],
    ]
)
basic_motions_proba["SignatureClassifier"] = np.array(
    [
        [0.0, 0.0, 0.5, 0.5],
        [0.4, 0.0, 0.3, 0.3],
        [0.0, 0.0, 0.9, 0.1],
        [0.2, 0.3, 0.1, 0.4],
        [0.0, 0.0, 0.4, 0.6],
        [0.0, 0.0, 0.7, 0.3],
        [0.1, 0.0, 0.6, 0.3],
        [0.0, 0.0, 0.9, 0.1],
        [0.0, 0.7, 0.1, 0.2],
        [0.2, 0.3, 0.1, 0.4],
    ]
)
basic_motions_proba["SummaryClassifier"] = np.array(
    [
        [0.0, 0.0, 0.3, 0.7],
        [0.5, 0.2, 0.1, 0.2],
        [0.0, 0.0, 0.8, 0.2],
        [0.0, 1.0, 0.0, 0.0],
        [0.1, 0.1, 0.2, 0.6],
        [0.0, 0.0, 0.3, 0.7],
        [0.5, 0.2, 0.1, 0.2],
        [0.0, 0.0, 0.8, 0.2],
        [0.1, 0.9, 0.0, 0.0],
        [0.1, 0.9, 0.0, 0.0],
    ]
)
basic_motions_proba["HIVECOTEV2"] = np.array(
    [
        [0.0, 0.0222, 0.0222, 0.9557],
        [0.8065, 0.0701, 0.0, 0.1235],
        [0.0222, 0.0, 0.858, 0.1198],
        [0.0701, 0.2803, 0.3774, 0.2722],
        [0.0222, 0.0, 0.0701, 0.9078],
        [0.0222, 0.0, 0.1144, 0.8634],
        [0.7843, 0.1845, 0.0, 0.0312],
        [0.0222, 0.0, 0.8483, 0.1295],
        [0.0922, 0.7843, 0.0922, 0.0312],
        [0.0, 0.9466, 0.0222, 0.0312],
    ]
)
basic_motions_proba["CanonicalIntervalForest"] = np.array(
    [
        [0.0, 0.0, 0.3, 0.7],
        [0.6, 0.2, 0.2, 0.0],
        [0.0, 0.1, 0.6, 0.3],
        [0.1, 0.5, 0.0, 0.4],
        [0.0, 0.0, 0.3, 0.7],
        [0.0, 0.0, 0.3, 0.7],
        [0.6, 0.2, 0.0, 0.2],
        [0.2, 0.0, 0.6, 0.2],
        [0.0, 0.5, 0.1, 0.4],
        [0.3, 0.7, 0.0, 0.0],
    ]
)
basic_motions_proba["DrCIF"] = np.array(
    [
        [0.1, 0.1, 0.3, 0.5],
        [0.8, 0.2, 0.0, 0.0],
        [0.0, 0.1, 0.7, 0.2],
        [0.3, 0.6, 0.0, 0.1],
        [0.2, 0.0, 0.2, 0.6],
        [0.0, 0.1, 0.4, 0.5],
        [0.5, 0.5, 0.0, 0.0],
        [0.0, 0.0, 0.8, 0.2],
        [0.3, 0.7, 0.0, 0.0],
        [0.2, 0.8, 0.0, 0.0],
    ]
)
basic_motions_proba["Arsenal"] = np.array(
    [
        [-0.0, 0.158, -0.0, 0.842],
        [1.0, -0.0, -0.0, -0.0],
        [0.6394, 0.3606, -0.0, -0.0],
        [-0.0, -0.0, 0.586, 0.414],
        [-0.0, -0.0, 0.2254, 0.7746],
        [-0.0, -0.0, 0.256, 0.744],
        [0.7771, 0.2229, -0.0, -0.0],
        [0.256, 0.2229, 0.3631, 0.158],
        [-0.0, 0.842, 0.158, -0.0],
        [-0.0, 1.0, -0.0, -0.0],
    ]
)
basic_motions_proba["RocketClassifier"] = np.array(
    [
        [0.0, 0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
    ]
)
basic_motions_proba["ShapeletTransformClassifier"] = np.array(
    [
        [0.2, 0.0, 0.0, 0.8],
        [0.2, 0.8, 0.0, 0.0],
        [0.2, 0.2, 0.4, 0.2],
        [0.0, 0.8, 0.0, 0.2],
        [0.2, 0.0, 0.0, 0.8],
        [0.2, 0.0, 0.2, 0.6],
        [0.2, 0.8, 0.0, 0.0],
        [0.0, 0.2, 0.6, 0.2],
        [0.0, 0.8, 0.0, 0.2],
        [0.2, 0.6, 0.0, 0.2],
    ]
)
