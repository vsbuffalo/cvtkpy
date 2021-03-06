# cvtkpy 


```
                   _   _    
         _____   _| |_| | __
        / __\ \ / / __| |/ /
       | (__ \ V /| |_|   < 
        \___| \_/  \__|_|\_\
                            
```

This is a Python package that implements the methods of Buffalo and Coop (2019,
2020) to calculate temporal covariances and convergence correlations. 

I have split this repository from http://github.com/vsbuffalo/cvtk, which is
the original version of this code used in the analysis of Buffalo and Coop
(2020). This way, the original code is preserved exactly for reproducibility
purposes. See the [cvtk/notebooks](http://github.com/vsbuffalo/cvtk) for
examples from our 2020 PNAS paper on how to do these analyses; this is the most
detailed documentation/tutorial currently.

## Installation

Currently this Python package is not hosted anywhere. So you will need to
install it locally by cloning this repository,

```
$ git clone https://github.com/vsbuffalo/cvtkpy.git
```

Then installing,

```
$ python setup.py install  # must be Python 3
```

which should also install any dependencies you don't have.

Then, try:

```
$ python
Python 3.7.2 | packaged by conda-forge | (default, Mar 19 2019, 20:46:22)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cvtk 
>>> # it works!
```

## Citing 

Please cite both Buffalo and Coop (*Genetics*, 2019) which is the original
paper about temporal covariance, and Buffalo and Coop (*PNAS*, 2020) which is
the correct paper to cite for these newer methods. Here are the BibTeX entries:

```
@ARTICLE{Buffalo2019-qs,
  title    = "The Linked Selection Signature of Rapid Adaptation in Temporal
              Genomic Data",
  author   = "Buffalo, Vince and Coop, Graham",
  journal  = "Genetics",
  volume   =  213,
  number   =  3,
  pages    = "1007--1045",
  month    =  nov,
  year     =  2019,
  language = "en"
}
@ARTICLE{Buffalo2020-my,
  title     = "Estimating the genome-wide contribution of selection to temporal
               allele frequency change",
  author    = "Buffalo, Vince and Coop, Graham",
  journal   = "Proc. Natl. Acad. Sci. U. S. A.",
  publisher = "National Academy of Sciences",
  month     =  aug,
  year      =  2020,
  language  = "en"
}
```


