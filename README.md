# Real-Time-Traffic-Sign-Recognition-with-Voice-Assistance-Using-Optimized-Curvelet-Entropy-Features
Real-Time Traffic Sign Recognition with Voice Assistance Using Optimized Curvelet Entropy Features

1. This project gives the article's codes with the same title.
2. The main file takes the dataset as input and computes all the coefficients of curvelet.

3. fdct_wrapping_window.m - Creates the two halves of a C^inf compactly supported window

 Inputs
   x       vector or matrix of abscissae, the relevant ones from 0 to 1

 Outputs
   wl,wr   vector or matrix containing samples of the left, resp. right
           half of the window

Used at least in fdct_wrapping.m and ifdct_wrapping.m

4. feature_vector_curvelet.m creates the 1D vector for the output from step 3.
5.  The py files are used for pre-processing  and the results are given in png files.
