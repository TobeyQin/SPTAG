import SPTAGClient
import time
import numpy as np
from GetVector import GetOneVector

index = SPTAGClient.AnnClient('127.0.0.1', '9500')
while not index.IsConnected():
    time.sleep(1)
index.SetTimeoutMilliseconds(18000)

embedding = GetOneVector()
# print (embedding.tobytes())
result = index.Search(embedding.tobytes(), 3, 'Float', True)
print (result)
# The result is ([0, 3197, 3648], [0.0, 4466.427734375, 4481.18310546875], ['Oxford102flowers/jpg/image_08005.jpg', 'Oxford102flowers/jpg/image_08010.jpg', 'Oxford102flowers/jpg/image_08011.jpg'])
