#The first Series we create will contain basic floating point numbers. The list we use to initialize the Series is [1, 3, 5.2].
import pandas as pd
s1 = pd.Series([1,3,5.2])
#The second Series we create comes from performing elemental multiplication on s1 using a separate list of floating point numbers.
import pandas as pd
s1 = pd.Series([1,3,5.2])
s2 = s1*pd.Series([0.1,0.2,0.3])
#We'll create another Series, this time with integers. The list we use to initialize this Series is [1, 3, 8, np.nan]. 
#This Series will also have row labels, which will be ['a', 'b', 'c', 'd'].
import numpy as np
import pandas as pd
#s1 = pd.Series([1,3,5.2])
#s2 = s1*pd.Series([0.1,0.2,0.3])
s3 = pd.Series([1,3,8,np.nan], index =['a','b','c','d'])
#The final Series we create will be initialized from a Python dictionary. The dictionary will have key-value pairs 'a':0, 'b':1, and 'c':2.
import pandas as pd
s4 = pd.Series({'a':0,'b':1,'c':2})
