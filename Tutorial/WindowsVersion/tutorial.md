## Introduction
The tutorial will use an example to guide you through the usage of SPTAG on Windows 10. After finish the tutorial, you will able to build an index server and write index queries with a client.

## Steps
1. Download SPTAG.
    - git clone https://github.com/microsoft/SPTAG.git
2. Build SPTAG. We need the following build targets.
    - IndexBuilder.exe
    - Server.exe
    - SPTAG.py
    - SPTAGClient.py
    - _SPTAG.pyd
    - _SPTAGClient.pyd
3. We also need the files in the \SPTAG\Tutorial\WindowsVersion
    - Oxford102flowers.tsv
        - It's the dataset.
        - It's derived from [102 Category Flower Dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)
        - It has 8189 vectors, each of which has 4096 dimensions and represents a image of flower.
    - query.py
        - Find a vector's 3 aproximate nearest neighbors.
    - GetVector.py
        - Provide a vector for query.py
4. Build the index
    - Open a Command Prompt, and cd into \SPTAG\Tutorial\WindowsVersion
    - mkdir work && cd work
    - Copy IndexBuilder.exe and paste here
    - Copy Oxford102flowers.tsv and paste here
    - .\IndexBuilder.exe -d 4096 -v Float -i Oxford102flowers.tsv -o Oxford102flowers_bkt -a BKT -t 8 Index.DistCalcMethod=L2 Index.NeighborhoodSize=32
    - The index is generated into Oxford102flowers_bkt.
5. Serve the index
    - Copy Server.exe and paste here
    - Create a server configuration file, called myserver.ini.
        ```
        [Service]
        ListenAddr=0.0.0.0
        ListenPort=9500
        ThreadNumber=8
        SocketThreadNumber=8

        [QueryConfig]
        DefaultMaxResultNumber=6
        DefaultSeparator=|
        [Index]
        List=BKT

        [Index_BKT]
        IndexFolder=./Oxford102flowers_bkt    
        ```
    - .\Server.exe -m socket -c myserver.ini
6. Query via client
    - Open another Command Prompt, and cd into \SPTAG\Tutorial\WindowsVersion\work
    - Copy query.py, GetVector.py and paste here
    - Copy SPTAG.py, SPTAGClient.py, _SPTAG.pyd, and _SPTAGClient.pyd and paste here
    - python query.py
        - The expected output
            ```
            ([0, 3197, 3648], [0.0, 4466.427734375, 4481.18310546875], ['Oxford102flowers/jpg/image_08005.jpg', 'Oxford102flowers/jpg/image_08010.jpg', 'Oxford102flowers/jpg/image_08011.jpg'])
            ```
