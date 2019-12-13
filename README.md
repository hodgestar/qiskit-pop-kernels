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
* [Repository guide](#repository-guide)

<a id="what-we-did">
## What we did

### Evaluate measurement performance as a function of measurement pulse frequency

* Understand qubit measurement and pulse control.
* Investigation of measurement performance as a function of measurement pulse frequency.

### Characterise X and K qubit parameters

* Characterisation of X and K for a qubit.

### Improved classification of IQ values

* Created improved discriminators.
* PR: https://github.com/Qiskit/qiskit-ignis/pull/316

<a id="repository-guide">
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
