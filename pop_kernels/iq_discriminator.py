# -*- coding: utf-8 -*-

""" SVM based IQ discriminator. """

from typing import Union, List

from qiskit.ignis.measurement.discriminator.iq_discriminators import (
    IQDiscriminationFitter,
)
from qiskit.result import Result
from qiskit.pulse.schedule import Schedule
from sklearn.svm import SVC


class SklearnIQDiscriminator(IQDiscriminationFitter):
    """ A generic discriminant analysis discriminator for IQ data that
        takes an sklearn classifier as an argument.
    """

    def __init__(self, classifier, cal_results: Union[Result, List[Result]],
                 qubit_mask: List[int], expected_states: List[str] = None,
                 standardize: bool = False,
                 schedules: Union[List[str], List[Schedule]] = None):
        """
        Args:
            classifier:
                An sklearn classifier to train.
            cal_results (Union[Result, List[Result]]): calibration results,
                Result or list of Result used to fit the discriminator.
            qubit_mask (List[int]): determines which qubit's level 1 data to
                use in the discrimination process.
            expected_states (List[str]): a list that should have the same
                length as schedules. All results in cal_results are used if
                schedules is None. expected_states must have the corresponding
                length.
            standardize (bool): if true the discriminator will standardize the
                xdata using the internal method _scale_data.
            schedules (Union[List[str], List[Schedule]]): The schedules or a
                subset of schedules in cal_results used to train the
                discriminator. The user may also pass the name of the schedules
                instead of the schedules. If schedules is None, then all the
                schedules in cal_results are used.
        """
        self._classifier = classifier

        # Also sets the x and y data.
        IQDiscriminationFitter.__init__(self, cal_results, qubit_mask,
                                        expected_states, standardize,
                                        schedules)

        self._description = '{} IQ discriminator for measurement level 1.'.format(
            classifier.__class__.__name__)

        self.fit()

    def fit(self):
        """ Fits the discriminator using self._xdata and self._ydata. """
        if len(self._xdata) == 0:
            return

        self._classifier.fit(self._xdata, self._ydata)
        self._fitted = True

    def discriminate(self, x_data: List[List[float]]) -> List[str]:
        """ Applies the discriminator to x_data.

            Args:
                x_data (List[List[float]]): list of features. Each feature is
                    itself a list.

            Returns (List[str]):
                the discriminated x_data as a list of labels.
        """
        return self._classifier.predict(x_data)
