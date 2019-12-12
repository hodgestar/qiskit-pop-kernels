Measurement Kernels
===================

Figuring out X and K parameters
-------------------------------

X = g^2 / D

D = w_r - w_q
  ~ 7 - 5 GHz
  ~ 2 GHz

C_g -> resonator -> C_X

Read out frequencies:
  * f_R(|0>) -- read out frequency in the |0> state
  * f_R(|1>) -- read out frequency in the |1> state
  * typically these are slightly shifted from each other
  * separation of the peaks is 2X
  * width of the peaks is K (FWHM)

Determining peak shapes:

  * |0> -> I -> measure at different f_R (measuring |0>)
  * |0> -> X_pi -> measure at different f_R (measuring |1>)
  * repeat for q in (0, 1)
  * f_R reported by backend.properties (read out frequency)
  * f_R -+ 5 MHz in steps of 100 kHz
  * fit poisson

IQ plane
--------

I = in phase
Q = quadrature

Each measurement is a dot on the IQ plane.

Theta = angle between lines from origin to |0> and |1> blobs.
      = 2 * arctan (2X / K)

Length of line = gain from amplifiers.
