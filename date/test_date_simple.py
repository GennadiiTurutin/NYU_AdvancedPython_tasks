
# coding: utf-8

# In[70]:

import date_simple as ds
import pytest
import datetime as dt


def test_get_date_object_args():
    assert ds.get_date_object() == dt.date.today()
    
def test_get_date_object_string(x):
    assert ds.get_date_object(x) == dt.datetime.strptime(x, '%Y-%m-%d').date()
    
def test_get_date_string_args(): 
    assert ds.get_date_string() == dt.datetime.strftime(dt.date.today(), '%m/%d/%Y')
    
def test_get_date_string(x, _format='%m/%d/%Y'):
    assert ds.get_date_string(x, _format) == dt.datetime.strftime(x, _format)
    
def test_get_date_string_extra_1(x, y):
    assert ds.get_date_string(x, _format=y) == dt.datetime.strftime(x, '%m/%d/%Y') 
    
def test_get_date_string_extra_2(x, y):
    assert ds.get_date_string(x, _format=y) == dt.datetime.strftime(x, '%d-%m-%y') 
    # I guess that this test is not complete, as my function is not capable to work with months
    # given in a format Jun, Sep etc. Must be modified
    
def test_get_date_object_value(x):
    with pytest.raises(ValueError):
        ds.get_date_object(date = x) 
                    
def test_get_date_object_type(x):        
    with pytest.raises(TypeError):
        ds.get_date_object(date = x)                      
                    
def test_get_date_string_type(x):
    with pytest.raises(ValueError):
        ds.get_date_string(date = x)
        
def test_get_date_string_type(x):
    with pytest.raises(TypeError):
        ds.get_date_string(date = x)        
        
def test_get_date_string_format_value(x):        
    with pytest.raises(ValueError):
        ds.get_date_string(_format = x)
        


# In[2]:

#1. assert that if date_simple.get_date_object() is called with no arguments, it will return a date object for today.
test_get_date_object_args()


# In[3]:

#2. assert that if date_simple.get_date_object() is called with a properly formatted date string, it will return a date object for that date.
test_get_date_object_string('2012-12-05')


# In[17]:

#3. assert that if date_simple.get_date_string() is called with no arguments, it will return a date string for today.
test_get_date_string_args()


# In[37]:

#4. assert that if date_simple.get_date_string() is called with a date object, it will return the date string for that date.
test_get_date_string(dt.datetime.strptime('02/13/2017', '%m/%d/%Y').date(), '%m/%d/%Y')


# In[48]:

#5.assert that if date_simple.get_date_string() is called with format='MM/DD/YYYY', it will return a date string in that format.
test_get_date_string_extra_1(dt.datetime.strptime('02/13/2017', '%m/%d/%Y').date(), 'MM/DD/YYYY')


# In[53]:

#6. assert that if date_simple.get_date_string() is called with format='DD-Mon-YY', it will return a date string in that format.
test_get_date_string_extra_2(dt.datetime.strptime('02-10-17', '%d-%m-%y').date(), 'DD-Mon-YY')


# In[68]:

#7. assert that if date_simple.get_date_object() is called with an improperly formatted string date, it will raise a ValueError exception.
test_get_date_object_value('2012-12-05eee')


# In[65]:

#8. assert that if date_simple.get_date_object() is called with an object that is not type str, it will raise a TypeError exception.
test_get_date_object_type(2342)


# In[73]:

#9. assert that if date_simple.get_date_string() is called with an object that is not type datetime.date, it will raise a TypeError exception.
test_get_date_string_type(353453)


# In[71]:

test_get_date_string_format('sdfsgsg')

