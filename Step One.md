```python
                                   #DATA PREPROCESSING AND DATA CLEANING 
```


```python
#Read my dataset into the Jupyter Notebook
import pandas as pd
df=("user_behavior_dataset.csv")
read=pd.read_csv(df)
read
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User ID</th>
      <th>Device Model</th>
      <th>Operating System</th>
      <th>App Usage Time (min/day)</th>
      <th>Screen On Time (hours/day)</th>
      <th>Battery Drain (mAh/day)</th>
      <th>Number of Apps Installed</th>
      <th>Data Usage (MB/day)</th>
      <th>Age</th>
      <th>Gender</th>
      <th>User Behavior Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>393</td>
      <td>6.4</td>
      <td>1872</td>
      <td>67</td>
      <td>1122</td>
      <td>40</td>
      <td>Male</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>OnePlus 9</td>
      <td>Android</td>
      <td>268</td>
      <td>4.7</td>
      <td>1331</td>
      <td>42</td>
      <td>944</td>
      <td>47</td>
      <td>Female</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Xiaomi Mi 11</td>
      <td>Android</td>
      <td>154</td>
      <td>4.0</td>
      <td>761</td>
      <td>32</td>
      <td>322</td>
      <td>42</td>
      <td>Male</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>239</td>
      <td>4.8</td>
      <td>1676</td>
      <td>56</td>
      <td>871</td>
      <td>20</td>
      <td>Male</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>iPhone 12</td>
      <td>iOS</td>
      <td>187</td>
      <td>4.3</td>
      <td>1367</td>
      <td>58</td>
      <td>988</td>
      <td>31</td>
      <td>Female</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>695</th>
      <td>696</td>
      <td>iPhone 12</td>
      <td>iOS</td>
      <td>92</td>
      <td>3.9</td>
      <td>1082</td>
      <td>26</td>
      <td>381</td>
      <td>22</td>
      <td>Male</td>
      <td>2</td>
    </tr>
    <tr>
      <th>696</th>
      <td>697</td>
      <td>Xiaomi Mi 11</td>
      <td>Android</td>
      <td>316</td>
      <td>6.8</td>
      <td>1965</td>
      <td>68</td>
      <td>1201</td>
      <td>59</td>
      <td>Male</td>
      <td>4</td>
    </tr>
    <tr>
      <th>697</th>
      <td>698</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>99</td>
      <td>3.1</td>
      <td>942</td>
      <td>22</td>
      <td>457</td>
      <td>50</td>
      <td>Female</td>
      <td>2</td>
    </tr>
    <tr>
      <th>698</th>
      <td>699</td>
      <td>Samsung Galaxy S21</td>
      <td>Android</td>
      <td>62</td>
      <td>1.7</td>
      <td>431</td>
      <td>13</td>
      <td>224</td>
      <td>44</td>
      <td>Male</td>
      <td>1</td>
    </tr>
    <tr>
      <th>699</th>
      <td>700</td>
      <td>OnePlus 9</td>
      <td>Android</td>
      <td>212</td>
      <td>5.4</td>
      <td>1306</td>
      <td>49</td>
      <td>828</td>
      <td>23</td>
      <td>Female</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>700 rows × 11 columns</p>
</div>




```python
#Display the first 11 rows from index 0
read.head(11)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User ID</th>
      <th>Device Model</th>
      <th>Operating System</th>
      <th>App Usage Time (min/day)</th>
      <th>Screen On Time (hours/day)</th>
      <th>Battery Drain (mAh/day)</th>
      <th>Number of Apps Installed</th>
      <th>Data Usage (MB/day)</th>
      <th>Age</th>
      <th>Gender</th>
      <th>User Behavior Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>393</td>
      <td>6.4</td>
      <td>1872</td>
      <td>67</td>
      <td>1122</td>
      <td>40</td>
      <td>Male</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>OnePlus 9</td>
      <td>Android</td>
      <td>268</td>
      <td>4.7</td>
      <td>1331</td>
      <td>42</td>
      <td>944</td>
      <td>47</td>
      <td>Female</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Xiaomi Mi 11</td>
      <td>Android</td>
      <td>154</td>
      <td>4.0</td>
      <td>761</td>
      <td>32</td>
      <td>322</td>
      <td>42</td>
      <td>Male</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>239</td>
      <td>4.8</td>
      <td>1676</td>
      <td>56</td>
      <td>871</td>
      <td>20</td>
      <td>Male</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>iPhone 12</td>
      <td>iOS</td>
      <td>187</td>
      <td>4.3</td>
      <td>1367</td>
      <td>58</td>
      <td>988</td>
      <td>31</td>
      <td>Female</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>99</td>
      <td>2.0</td>
      <td>940</td>
      <td>35</td>
      <td>564</td>
      <td>31</td>
      <td>Male</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Samsung Galaxy S21</td>
      <td>Android</td>
      <td>350</td>
      <td>7.3</td>
      <td>1802</td>
      <td>66</td>
      <td>1054</td>
      <td>21</td>
      <td>Female</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>OnePlus 9</td>
      <td>Android</td>
      <td>543</td>
      <td>11.4</td>
      <td>2956</td>
      <td>82</td>
      <td>1702</td>
      <td>31</td>
      <td>Male</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Samsung Galaxy S21</td>
      <td>Android</td>
      <td>340</td>
      <td>7.7</td>
      <td>2138</td>
      <td>75</td>
      <td>1053</td>
      <td>42</td>
      <td>Female</td>
      <td>4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>iPhone 12</td>
      <td>iOS</td>
      <td>424</td>
      <td>6.6</td>
      <td>1957</td>
      <td>75</td>
      <td>1301</td>
      <td>42</td>
      <td>Male</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>53</td>
      <td>1.4</td>
      <td>435</td>
      <td>17</td>
      <td>162</td>
      <td>34</td>
      <td>Female</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Display the last 10 rows
read.tail(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User ID</th>
      <th>Device Model</th>
      <th>Operating System</th>
      <th>App Usage Time (min/day)</th>
      <th>Screen On Time (hours/day)</th>
      <th>Battery Drain (mAh/day)</th>
      <th>Number of Apps Installed</th>
      <th>Data Usage (MB/day)</th>
      <th>Age</th>
      <th>Gender</th>
      <th>User Behavior Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>690</th>
      <td>691</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>195</td>
      <td>5.7</td>
      <td>1447</td>
      <td>48</td>
      <td>679</td>
      <td>30</td>
      <td>Male</td>
      <td>3</td>
    </tr>
    <tr>
      <th>691</th>
      <td>692</td>
      <td>iPhone 12</td>
      <td>iOS</td>
      <td>178</td>
      <td>4.0</td>
      <td>856</td>
      <td>37</td>
      <td>569</td>
      <td>51</td>
      <td>Female</td>
      <td>2</td>
    </tr>
    <tr>
      <th>692</th>
      <td>693</td>
      <td>Xiaomi Mi 11</td>
      <td>Android</td>
      <td>378</td>
      <td>6.7</td>
      <td>1898</td>
      <td>78</td>
      <td>1455</td>
      <td>48</td>
      <td>Female</td>
      <td>4</td>
    </tr>
    <tr>
      <th>693</th>
      <td>694</td>
      <td>Xiaomi Mi 11</td>
      <td>Android</td>
      <td>505</td>
      <td>8.6</td>
      <td>2792</td>
      <td>82</td>
      <td>1709</td>
      <td>31</td>
      <td>Male</td>
      <td>5</td>
    </tr>
    <tr>
      <th>694</th>
      <td>695</td>
      <td>Samsung Galaxy S21</td>
      <td>Android</td>
      <td>564</td>
      <td>9.7</td>
      <td>2422</td>
      <td>83</td>
      <td>1985</td>
      <td>34</td>
      <td>Female</td>
      <td>5</td>
    </tr>
    <tr>
      <th>695</th>
      <td>696</td>
      <td>iPhone 12</td>
      <td>iOS</td>
      <td>92</td>
      <td>3.9</td>
      <td>1082</td>
      <td>26</td>
      <td>381</td>
      <td>22</td>
      <td>Male</td>
      <td>2</td>
    </tr>
    <tr>
      <th>696</th>
      <td>697</td>
      <td>Xiaomi Mi 11</td>
      <td>Android</td>
      <td>316</td>
      <td>6.8</td>
      <td>1965</td>
      <td>68</td>
      <td>1201</td>
      <td>59</td>
      <td>Male</td>
      <td>4</td>
    </tr>
    <tr>
      <th>697</th>
      <td>698</td>
      <td>Google Pixel 5</td>
      <td>Android</td>
      <td>99</td>
      <td>3.1</td>
      <td>942</td>
      <td>22</td>
      <td>457</td>
      <td>50</td>
      <td>Female</td>
      <td>2</td>
    </tr>
    <tr>
      <th>698</th>
      <td>699</td>
      <td>Samsung Galaxy S21</td>
      <td>Android</td>
      <td>62</td>
      <td>1.7</td>
      <td>431</td>
      <td>13</td>
      <td>224</td>
      <td>44</td>
      <td>Male</td>
      <td>1</td>
    </tr>
    <tr>
      <th>699</th>
      <td>700</td>
      <td>OnePlus 9</td>
      <td>Android</td>
      <td>212</td>
      <td>5.4</td>
      <td>1306</td>
      <td>49</td>
      <td>828</td>
      <td>23</td>
      <td>Female</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
#display the total number of rows and columns in the dataset
read.shape
```




    (700, 11)




```python
#The columns in the dataset described
read.columns
```




    Index(['User ID', 'Device Model', 'Operating System',
           'App Usage Time (min/day)', 'Screen On Time (hours/day)',
           'Battery Drain (mAh/day)', 'Number of Apps Installed',
           'Data Usage (MB/day)', 'Age', 'Gender', 'User Behavior Class'],
          dtype='object')




```python
#Check for datatypes in the columns of the dataset
read.dtypes
```




    User ID                         int64
    Device Model                   object
    Operating System               object
    App Usage Time (min/day)        int64
    Screen On Time (hours/day)    float64
    Battery Drain (mAh/day)         int64
    Number of Apps Installed        int64
    Data Usage (MB/day)             int64
    Age                             int64
    Gender                         object
    User Behavior Class             int64
    dtype: object




```python
#General overview of the dataset
read.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 700 entries, 0 to 699
    Data columns (total 11 columns):
     #   Column                      Non-Null Count  Dtype  
    ---  ------                      --------------  -----  
     0   User ID                     700 non-null    int64  
     1   Device Model                700 non-null    object 
     2   Operating System            700 non-null    object 
     3   App Usage Time (min/day)    700 non-null    int64  
     4   Screen On Time (hours/day)  700 non-null    float64
     5   Battery Drain (mAh/day)     700 non-null    int64  
     6   Number of Apps Installed    700 non-null    int64  
     7   Data Usage (MB/day)         700 non-null    int64  
     8   Age                         700 non-null    int64  
     9   Gender                      700 non-null    object 
     10  User Behavior Class         700 non-null    int64  
    dtypes: float64(1), int64(7), object(3)
    memory usage: 60.3+ KB
    


```python
#Check for duplicates in the rows and columns
read.duplicated()
```




    0      False
    1      False
    2      False
    3      False
    4      False
           ...  
    695    False
    696    False
    697    False
    698    False
    699    False
    Length: 700, dtype: bool




```python
#Sum of the duplicates found
read.duplicated(). sum()
```




    0




```python
#Summary statistics for quantitative data
read.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User ID</th>
      <th>App Usage Time (min/day)</th>
      <th>Screen On Time (hours/day)</th>
      <th>Battery Drain (mAh/day)</th>
      <th>Number of Apps Installed</th>
      <th>Data Usage (MB/day)</th>
      <th>Age</th>
      <th>User Behavior Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>700.00000</td>
      <td>700.000000</td>
      <td>700.000000</td>
      <td>700.000000</td>
      <td>700.000000</td>
      <td>700.000000</td>
      <td>700.000000</td>
      <td>700.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>350.50000</td>
      <td>271.128571</td>
      <td>5.272714</td>
      <td>1525.158571</td>
      <td>50.681429</td>
      <td>929.742857</td>
      <td>38.482857</td>
      <td>2.990000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>202.21688</td>
      <td>177.199484</td>
      <td>3.068584</td>
      <td>819.136414</td>
      <td>26.943324</td>
      <td>640.451729</td>
      <td>12.012916</td>
      <td>1.401476</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.00000</td>
      <td>30.000000</td>
      <td>1.000000</td>
      <td>302.000000</td>
      <td>10.000000</td>
      <td>102.000000</td>
      <td>18.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>175.75000</td>
      <td>113.250000</td>
      <td>2.500000</td>
      <td>722.250000</td>
      <td>26.000000</td>
      <td>373.000000</td>
      <td>28.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>350.50000</td>
      <td>227.500000</td>
      <td>4.900000</td>
      <td>1502.500000</td>
      <td>49.000000</td>
      <td>823.500000</td>
      <td>38.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>525.25000</td>
      <td>434.250000</td>
      <td>7.400000</td>
      <td>2229.500000</td>
      <td>74.000000</td>
      <td>1341.000000</td>
      <td>49.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>700.00000</td>
      <td>598.000000</td>
      <td>12.000000</td>
      <td>2993.000000</td>
      <td>99.000000</td>
      <td>2497.000000</td>
      <td>59.000000</td>
      <td>5.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
read.isnull().sum()
```




    User ID                       0
    Device Model                  0
    Operating System              0
    App Usage Time (min/day)      0
    Screen On Time (hours/day)    0
    Battery Drain (mAh/day)       0
    Number of Apps Installed      0
    Data Usage (MB/day)           0
    Age                           0
    Gender                        0
    User Behavior Class           0
    dtype: int64




```python
#Once completeness has been achieved uniqueness is automatically proven
```


```python
import pandas as pd

#the dataframe
dataset=("user_behavior_dataset.csv")
read=pd.read_csv(dataset)

#Identify numerical columns
numeric_read=read.select_dtypes(include='number')

#Calculate Q1 and Q3 and IQR
Q1=numeric_read.quantile(0.25)
Q3=numeric_read.quantile(0.75)
IQR=Q3-Q1

#Define outlier bounds
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

#Create a mask for outliers (Use logical conditions to identify rows that contain outliers in any numerical column)
outlier_mask=~((numeric_read<lower_bound)|(numeric_read>upper_bound)).any(axis=1) #axis=1 confirms that we are working on rows

#Filter the Dataframe to remove outliers,keeping non-numerical columns
read_no_outliers=read[outlier_mask]

#Display the results
print("Original Dataframe:")
print(read)
print("\nDataFrame without outliers:")
print(read_no_outliers)
```

    Original Dataframe:
         User ID        Device Model Operating System  App Usage Time (min/day)  \
    0          1      Google Pixel 5          Android                       393   
    1          2           OnePlus 9          Android                       268   
    2          3        Xiaomi Mi 11          Android                       154   
    3          4      Google Pixel 5          Android                       239   
    4          5           iPhone 12              iOS                       187   
    ..       ...                 ...              ...                       ...   
    695      696           iPhone 12              iOS                        92   
    696      697        Xiaomi Mi 11          Android                       316   
    697      698      Google Pixel 5          Android                        99   
    698      699  Samsung Galaxy S21          Android                        62   
    699      700           OnePlus 9          Android                       212   
    
         Screen On Time (hours/day)  Battery Drain (mAh/day)  \
    0                           6.4                     1872   
    1                           4.7                     1331   
    2                           4.0                      761   
    3                           4.8                     1676   
    4                           4.3                     1367   
    ..                          ...                      ...   
    695                         3.9                     1082   
    696                         6.8                     1965   
    697                         3.1                      942   
    698                         1.7                      431   
    699                         5.4                     1306   
    
         Number of Apps Installed  Data Usage (MB/day)  Age  Gender  \
    0                          67                 1122   40    Male   
    1                          42                  944   47  Female   
    2                          32                  322   42    Male   
    3                          56                  871   20    Male   
    4                          58                  988   31  Female   
    ..                        ...                  ...  ...     ...   
    695                        26                  381   22    Male   
    696                        68                 1201   59    Male   
    697                        22                  457   50  Female   
    698                        13                  224   44    Male   
    699                        49                  828   23  Female   
    
         User Behavior Class  
    0                      4  
    1                      3  
    2                      2  
    3                      3  
    4                      3  
    ..                   ...  
    695                    2  
    696                    4  
    697                    2  
    698                    1  
    699                    3  
    
    [700 rows x 11 columns]
    
    DataFrame without outliers:
         User ID        Device Model Operating System  App Usage Time (min/day)  \
    0          1      Google Pixel 5          Android                       393   
    1          2           OnePlus 9          Android                       268   
    2          3        Xiaomi Mi 11          Android                       154   
    3          4      Google Pixel 5          Android                       239   
    4          5           iPhone 12              iOS                       187   
    ..       ...                 ...              ...                       ...   
    695      696           iPhone 12              iOS                        92   
    696      697        Xiaomi Mi 11          Android                       316   
    697      698      Google Pixel 5          Android                        99   
    698      699  Samsung Galaxy S21          Android                        62   
    699      700           OnePlus 9          Android                       212   
    
         Screen On Time (hours/day)  Battery Drain (mAh/day)  \
    0                           6.4                     1872   
    1                           4.7                     1331   
    2                           4.0                      761   
    3                           4.8                     1676   
    4                           4.3                     1367   
    ..                          ...                      ...   
    695                         3.9                     1082   
    696                         6.8                     1965   
    697                         3.1                      942   
    698                         1.7                      431   
    699                         5.4                     1306   
    
         Number of Apps Installed  Data Usage (MB/day)  Age  Gender  \
    0                          67                 1122   40    Male   
    1                          42                  944   47  Female   
    2                          32                  322   42    Male   
    3                          56                  871   20    Male   
    4                          58                  988   31  Female   
    ..                        ...                  ...  ...     ...   
    695                        26                  381   22    Male   
    696                        68                 1201   59    Male   
    697                        22                  457   50  Female   
    698                        13                  224   44    Male   
    699                        49                  828   23  Female   
    
         User Behavior Class  
    0                      4  
    1                      3  
    2                      2  
    3                      3  
    4                      3  
    ..                   ...  
    695                    2  
    696                    4  
    697                    2  
    698                    1  
    699                    3  
    
    [700 rows x 11 columns]
    


```python
#Outliers have not been found hence dataframe mantains its original shape of 700 rowsx 11columns
```
