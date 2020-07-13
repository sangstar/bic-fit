# bic-fit


A package I've been working on which takes array-like x and y data, generates polynomial and piecewise (maximally 3 model breaks) fit parameters and evaluates the BIC score used. Makes certain assumptions as to the nature of the error, listed here: https://en.wikipedia.org/wiki/Bayesian_information_criterion#Gaussian_special_case

Please feel free to submit a pull request. Any corrections or problems raised is more than welcome.

# Things to note

1. The y-array has to be an array of shape (N,1). 
2. The segmented regressions tend to fail when there the number of points it is given far outnumber the training data.
3. Due to the unforgiving nature of BIC when dealing with a large number of parameters, polynomial fits greater than degree 0 and segmented regressions greater than 1 model break (each incremental model break increases parameters by 3) almost never score lowest.

# Possible issues
1. It seems to be routinely the case that segmented regressions with 1 model break minimize BIC nearly every time, typically followed by the other segmented regressions of 2 and 3 model breaks and then followed by polynomial models. This is a bit suspicious, but likely a consequence of the fact that the residual sum of squares found using segmented regressions are typically far lower than that found with polynomial models. 
