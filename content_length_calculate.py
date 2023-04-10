#!/usr/bin/env python

import json

# Calculating the size of the payload here
# We will be sending this as part of the Content-length Key value pair (I know not exactly the right term lol)

sample_data = {'Reason' : '4fun'}

json_sample_data = json.dumps(sample_data).encode('utf-8')

print('Before:', sample_data, 'After:', json_sample_data)

# Encoding it to json using utf-8 scheme.

content_length = len(json_sample_data)

print(content_length)
