from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : dict[Key,Value] = {}

data['name'] = "Muhammad Qasim" #add new key and values
data['fname'] = "Muhammad Aslam"
data['education'] = "MSDS"

print(data)