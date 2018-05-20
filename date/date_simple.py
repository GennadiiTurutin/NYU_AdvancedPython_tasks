
# coding: utf-8

# In[1]:

#Import of modules
import datetime as dt

    
def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    if date == None:
        return dt.date.today()
    else:
        return dt.datetime.strptime(date, '%Y-%m-%d').date()
    
def get_date_string(date_object=dt.date.today(), _format='%m/%d/%Y'):
    """ takes an optional date object and returns a formatted string """
    
    if type(date_object).__name__ == 'date': 
        
        dic = {'%Y':['YYYY', 'yyyy'], '%y':['YY'], 
                    '%d': ['Day', 'DD', 'D', 'dd'], 
                    '%m':['Mon', 'MM', 'M', 'mm', ], '%': ['%%']}
        
        for i, j in dic.items():
            for _ in j:
                _format = _format.replace(_, i)
                
        check = "mMYydD%/-"
        
        if all(letter in check for letter in format): 
            return date_object.strftime(format)
        else: 
            raise ValueError
        
    else: 
        raise TypeError
        

