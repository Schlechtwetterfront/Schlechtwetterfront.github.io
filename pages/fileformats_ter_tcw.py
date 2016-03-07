from page_core import *

PAGE = {
    'page_template': 'project_index.html',
    'path': '../',
    'output_file': 'xxw.html',
    'output_folder': 'ze_filetypes',
    'page_title': 'ZE File Formats - .XXW',
    'use_bright_theme': True,
    'fixed_categories': [

    ],
    'categories': [
        Category('Navigation', [
            Link('Overview', '#overview'),
            Link('Back', 'index.html', LINK_INTERNAL),
            Link('Homepage', 'http://schlechtwetterfront.github.io/', LINK_INTERNAL)
            ]),
        Category('Format', [
            Link('Terrain Header', '#terrain_header'),
            Link('Terrain Blocks', '#terrain_blocks'),
            Link('Terrain Structs', '#terrain_structs')
            ], True),
    ],
    'sections': [
        Section('Overview', 'overview', True, False, False, '''
Terrain files (\*.xxw) represent a single terrain to be used by a world. This format was used in _Star Wars: The Clone Wars_.  
THIS IS HEAVY WORK IN PROGRESS.
'''),
        Section('Terrain Header', 'terrain_header', True, False, False, '''
The Terrain Header is always 1152 bytes in length.

```
ad  length  type    ex          desc
0   4       ?       1152        ?
4           long    3           version?
8           long    1024        terrain size?
12          int     257         ?
16          int     2           ?
20          float   32          grid size?
24          float   0.1...      ?
28          
32          int     128         map size?
36
40          int     128         extents with 8? or 6 sets of RGB colors?

64-124      float               Tile-range for each texture layer


1,668 -     514 size chunks?
132,218
--- BLOCKS
size * size (* 2) heights
xV4_ ?


```

 Offset       | Data Type           | Size (bytes)  | Description
------------- | ------------        |---------------| ---
 0            | byte [4]{: .orange} | 4             | Header size indicator (1152).
 4            | long uint{: .red}   | 4             | File format version? (03)
 8            | long uint{: .red}   | 4             | ? (1024)
 12           | long uint{: .red}   | 4             | Terrain size. (257, 513) 
 16           | long uint{: .red}   | 4             | ? (2)
 20           | float {: .red}      | 4             | Grid scale. (32, 16, 8)
 24           | float {: .red}      | 4             | Height scale. (0.1, 0.03, 0.23)
 28           | long int [4]{: .red}| 16            | Map extents (i.e. -256, 256, -256, 256 for a 512x512 map)
 44+          | ?                   | 20            | ? 
 64           | float [16] {: .red} | 64            | Tile-range for each texture layer. _0.031 (1/32): the texture spans 32 meters. This is stored as 1/X of the value in ZeroEditor._
 128          | TextureLayer [16]   | 1024          | Texture layers (see below).

'''),
        Section('Terrain Blocks', 'terrain_blocks', True, False, False, '''
The Terrain Header is always 2821 bytes in length.

Name            | Data Type             | Size
------------    |---------------        |-------------
**Height**      | signed short{: .red}  | **Terrain size * Terrain size** * 2
                | | Height value for every point on the grid. This value will be multiplied with the map scale multiplier.
**?**           | ?                     | Size: (Terrain size - 1) * (Terrain size - 1) * 2 
                | | 
**?**           | ?                     | Size: 
                | | Chunks with 38 bytes of data?

'''),
        Section('Terrain Structs', 'terrain_structs', True, False, False, '''
### TextureLayer

Data Type           | Size (bytes)  | Description
------------        |---------------|-------------
char [32]{: .green} | 32            | Diffuse texture name.
char [32]{: .green} | 32            | Detail texture name.

### WaterLayer

Data Type           | Size (bytes)  | Description
------------        |---------------|-------------
float [2]{: .red}   | 8             | Water height value (twice).
byte [8]{: .orange} | 8             | Unknown, always zero. 
float [2]{: .red}   | 8             | UV animation velocity. 
float [2]{: .red}   | 8             | UV animation repeat. 
byte [4]{: .orange} | 4             | RGBA color values. 
char [32]{: .green} | 32            | Water texture name.

'''),
        ]
    }