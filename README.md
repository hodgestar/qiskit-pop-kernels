# Understanding and Improving Qubit Measurement

Qubit measurement is a process that consists of generating a measurement
pulse, having the pulse interact with the qubit, reading out voltages,
integrating the voltages into IQ values, and classifying the IQ values
as a particular measurement outcome.

The goal of this project is to understand and characterise this pipeline.

* [Qiskit Camp Africa 2019](https://github.com/qiskit-community/qiskit-camp-africa-19/)
* Hackathon Team [#23](https://github.com/qiskit-community/qiskit-camp-africa-19/issues/23)

Contents:

* [What we did](#what-we-did)
* [What we learned](#what-we-learned)
* [Future work](#future-work)
* [Repository guide](#repository-guide)

<a id="what-we-did"></a>

## What we did

### Evaluate measurement performance as a function of measurement pulse frequency

Using the ibmq_armonk system and pulse control, we examined measurement
outcomes as a function of measurement pulse frequency.

The IQ plots clearly show how 0 and 1 outcomes become more separable on the
IQ plane as the optimal measurement frequency is approached. Separability
worsens again as one moves away from the optimal peak.

At the optimal frequency, a small cluster of values can be seen in the
lower left of the IQ plane. These might be instances where the qubit
decoheres or is excited to the 2 energy level by the measurement pulse.
Further investigation of this cluster is needed.

The experiment ran 3 schedules: one with the qubit in the ``|0>`` states,
one with a qubit in the ``|1>`` state and one with the ``|0>`` rotate by
90 degrees about the X axis ``|0> - i|1> ``. The third schedule was not
used in the analysis.

512 shots were performed for each of 11 frequency steps.

* Notebook: [measurement_freq_experiments.ipynb](./notebooks/measurement_freq_experiments.ipynb)
* Saved results: [ibmq_armonk_measurement_freq_experiment.pickle](./notebooks/ibmq_armonk_measurement_freq_experiment.pickle)

### Characterise X and K qubit parameters

We used pulse control to determine the X and K values of the ibmq_armonk
qubit.

By scanning the measurement frequency across the optimal value, we determined
the shape of the peak of the IQ magnitude for both ``|0>`` and ``|1>`` states.

X is half the separation between the two peaks and was measured to be
``2.1297e-05 GHz``.

K is the average full-width at half maximum of the two peaks and was
measured to be ``1.8751 GHz``.

The notebook includes options to simulate the frequency peaks using either
Gaussian or Lorentzians. Experimental peaks are fitted with Lorentzians
using ``scipy``'s ``curve_fit`` function.

512 shots were performed for each of 101 frequency steps.

* Notebook: [Measure X and K using OpenPulse.ipynb](./notebooks/Measure%20X%20and%20K%20using%20OpenPulse.ipynb)
* Saved results: [xk_results](./notebooks/xk_results/)

### Improved classification of IQ values

The qiskit-ignis package currently includes linear and quadratic discriminators.

We investigated the possibility of using more sophisticated classifiers, and
in particular, ``sklearn.svm.SVC``, an SVM-based classifier provided by sklearn.

We fitted the discriminators to measurements obtained of the ``|0>`` and
``|1>`` states on ``ibmq_armonk``.

Various SVC kernels were tried, and the ``rbf`` (radial basis function)
kernel was determined give the best separation and to be the most robust.

Various values of the SVC regularization parameter ``C`` were compared.

The new SVC discriminator was compared to the existing linear and
quadratic discriminators and found to offer a slight deduction in measurement
errors.

* Notebook (comparison of regularization values): [sklearn_discriminators.ipynb](./notebooks/sklearn_discriminators.ipynb)
* Notebook (comparison with existing discriminators): [sklearn_discriminators_extension.ipynb](./notebooks/sklearn_discriminators_extension.ipynb)
* Notebook (for generating results): [armonk.ipynb](./notebooks/armonk.ipynb)
* Saved results: [ibmq_armonk_results.pickle](./notebooks/ibmq_armonk_results.pickle)
* qiskit-ignis PR to add SklearnIQDiscriminator: https://github.com/Qiskit/qiskit-ignis/pull/316

<a id="what-we-learned"></a>

## What we learned

* Measurement pulses
* OpenPulse
* Understand qubit measurement and pulse control.

<a id="future-work"></a>

## Future work

* Investigate improved kernels
* Investigate multi-qubit measurement discriminators

<a id="repository-guide"></a>

## Repository guide:

* [notebooks](./notebooks): Jupyter notebooks and experiment results.
* [papers](./papers): PDFs of relevant papers.
* [pkgs](./pkgs): Custom builds of Qiskit packages needed for pulse control.
* [pop_kernels](./pop_kernels): Python package containing the new IQ discriminators.
* Other:

  * [measurement-kernels-23.pdf](./measurement-kernels-23.pdf): PDF of the
    original hackathon issue (used for sharing while the WiFi was spotty).
  * [theory-notes.rst](./theory-notes.rst): Some notes from Nick's
    lecture on X, K and the IQ plane.
