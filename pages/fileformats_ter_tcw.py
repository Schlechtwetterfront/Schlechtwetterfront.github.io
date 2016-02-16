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
The Terrain Header is always ? bytes in length.

```
ad  length 	type 	ex 			desc
0	4		?		1152		?
4			long 	3			version?
8 			long 	1024		terrain size?
12			int 	257 		?
16			int 	2 			?
20			float 	32 			grid size?
24			float 	0.1... 		?
28			
32			int 	128 		map size?
36
40 			int 	128 		extents with 8? or 6 sets of RGB colors?

64-124		float 				Tile-range for each texture layer


1,668 - 	514 size chunks?
132,218

```

Data Type			| Size (bytes)	| Offset		| Description
------------		|---------------|-------------  | ---
byte [4]{: .orange}	| 4				| 0				| ?
long int{: .red}	| 4				| 4				| File format version? (03)
long int{: .red}	| 8				| 8				| Terrain size? (1024)
long int{: .red}	| 4				| 12			| ? (257)
long int{: .red}	| 4				| 16			| ? (2)
float {: .red}		| 4				| 20			| ? (32)
float {: .red}		| 4				| 24			| ? (0.1)
float {: .red}		| 4				| 28			| ? 
float {: .red}		| 4				| 32			| map size? (128)
float {: .red}		| 4				| 36			| ? 
float {: .red}		| 4				| 40			| map size? (128)
?					| 4				| 44+			| ? 
float [16] {: .red} | 64			| 64			| Tile-range for each texture layer. _0.031 (1/32): the texture spans 32 meters. This is stored as 1/X of the value in ZeroEditor.
TextureLayer [16] 	| 1024			| 80			| Texture layers (see below).
?					| 516			| 480			| ? 

'''),
			Section('Terrain Blocks', 'terrain_blocks', True, False, False, '''
The Terrain Header is always 2821 bytes in length.

Name			| Data Type				| Length
------------	|---------------		|-------------
**Height**		| signed short{: .red}	| Full map size * Full map size * 2 
				| |	Height value for every point on the grid. This value will be multiplied with the map scale multiplier.
**Color**		| float [4]{: .red}		| Full map size * Full map size 
				| |	Color values for every point on the grid. 4 floats (from 0.0 to 1.0) corresponding to the RGBA channels.
**Color 2**		| float [4]{: .red}		| Full map size * Full map size 
				| |	Color values for every point on the grid. 4 floats (from 0.0 to 1.0) corresponding to the RGBA channels.
**Texture**		| byte [16]{: .orange}	| Full map size * Full map size 
				| |	One byte (0-255) for each texture layer indicating the transparency of its texture layer.
**Water**		| byte{: .orange}		| Full map size * Full map size / 2 
				| |	Structure unknown.
**Foliage**		| byte{: .orange}		| Full map size * Full map size / 2 
				| |	Structure unknown.

'''),
			Section('Terrain Structs', 'terrain_structs', True, False, False, '''
### TextureLayer

Data Type			| Size (bytes)	| Description
------------		|---------------|-------------
char [32]{: .green}	| 32			| Diffuse texture name.
char [32]{: .green}	| 32			| Detail texture name.

### WaterLayer

Data Type			| Size (bytes)	| Description
------------		|---------------|-------------
float [2]{: .red}	| 8				| Water height value (twice).
byte [8]{: .orange}	| 8				| Unknown, always zero. 
float [2]{: .red}	| 8				| UV animation velocity. 
float [2]{: .red}	| 8				| UV animation repeat. 
byte [4]{: .orange}	| 4				| RGBA color values. 
char [32]{: .green}	| 32			| Water texture name.

'''),
		]
	}
