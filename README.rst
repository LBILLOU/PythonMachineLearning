=====================================================
Python Machine Learning w/ Zettafox
=====================================================

- Run as follows::

  $ python documentation_file.py    #Python Built-in Methods Documentation
  $ python class_file.py            #Python Basic Class Example
  $ python pandas_file.py           #Python Data Analysis & Predictions

---------------------------------

**pandas_file.py**
============================
This file is a machine learning prediction script. Prepare a csv file you want to work on, place it in the same directory and finally execute the script.

- Execution should look like so::

  $ >>> Import data from csv file, which file? (filename.csv)
  $ nflplayers.csv
  $
  $ Imported Data shape
  $ (1874, 7)
  $
  $ Imported Data columns
  $ ['number', 'full_name', 'position', 'height_in_inches', 'weight_in_lbs', 'date_of_birth', 'team']
  $
  $ >>> Which column would you like to predict?
  $ position
  $
  $ >>> Whould you like to drop a column for the prediction model? y/n
  $ y
  $
  $ >>> Which column would you like to drop?
  $ ['number', 'full_name', 'height_in_inches', 'weight_in_lbs', 'date_of_birth', 'team']
  $ team
  $
  $ >>> Would you like to drop another column? y?
  $ n
  $
  $ Data shape: (1874, 6)
  $ Training shape: (749, 6)
  $ Testing shape: (1125, 6)
  $
  $ Predictions Examples
  $       prediction  reality predictionTest
  $ 1831           7       22          right
  $ 1198          19       21          right
  $ 1461           3        3          wrong
  $ 275           21       19          right
  $ 416           15       10          right
  $
  $ Columns weight for defining prediction
  $ ('number', 0.33494276627361064)
  $ ('full_name', 0.14816128768493025)
  $ ('height_in_inches', 0.11351285140246144)
  $ ('weight_in_lbs', 0.26874000117490138)
  $ ('date_of_birth', 0.13464309346409625)
  $
  $ Prediction Results
  $ wrong    594
  $ right    531
  $ Name: predictionTest, dtype: int64
  $
  $ Model Efficiency
  $ 0.528
  $
  $
  $ END OF SCRIPT

.. image:: http://creativejunkie.fr/wp-content/uploads/2015/09/g-by-google.png


-----------------------------------

**documentation_file.py**
===============================
This file is a self made documentation for python 2.7, it refers every built-in function and method in an enjoyable menu.

.. image:: http://creativejunkie.fr/wp-content/uploads/2015/09/g-by-google.png


----------------------------------

**class_file.py**
===============================
This file is a basic python class used as an example.
