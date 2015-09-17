from page_core import *

PAGE = {
		'page_template': 'project_index.html',
		'path': '../',
		'output_file': 'render_types.html',
		'output_folder': 'ze_filetypes',
		'page_title': 'ZE File Formats - .MSH Render Types',
		'categories': [
			Category('Navigation', [
							   Link('Back', 'index.html'),
							   Link('General Info', '#general_info'),
							   ]),
			Category('Render Types', [
								Link('01 - Glow', '#glow'),
								Link('02 - Detail', '#detail'),
								Link('03 - Scrolling', '#scrolling'),
								Link('04 - Specular', '#specular'),
								Link('05 - Glossmap', '#glossmap'),
								Link('06 - Chrome', '#chrome'),
								Link('07 - Animated', '#animated'),
								Link('08 - Ice', '#ice'),
								Link('09 - Sky', '#sky'),
								Link('10 - Water', '#water'),
								Link('11 - Lightmap', '#lightmap'),
								Link('12 - 2 Scroll', '#2scroll'),
								Link('13 - Rotate', '#rotate'),
								Link('14 - Glow Rotate', '#glow_rotate'),
								Link('15 - Planar Reflection', '#planar_reflection'),
								Link('16 - Glow Scroll', '#glow_scroll'),
								Link('17 - Glow 2 Scroll', '#glow2scroll'),
								Link('18 - Curved Reflection', '#curved_reflection'),
								Link('19 - Normalmap Fade', '#normalmap_fade'),
								Link('20 - Normalmap Inv Fade', '#normalmap_inv_fade'),
								Link('21 - Ice Reflection', '#ice_reflection'),
								Link('22 - Ice Refraction', '#ice_refraction'),
								Link('23 - Emboss', '#emboss'),
								Link('24 - Wireframe', '#wireframe'),
								Link('25 - Energy', '#energy'),
								Link('26 - Afterburner', '#afterburner'),
								Link('27 - Bumpmap', '#bumpmap'),
								Link('28 - Bumpmap + Glossmap', '#bumpmap_glossmap'),
								Link('29 - Teleportal', '#teleportal'),
								Link('30 - MultiState', '#multistate'),
								Link('31 - Shield', '#shield'),
								]),
			Category('Personal', [
							   Link('Personal Homepage', 'http://schlechtwetterfront.github.io/')])
		],
		'sections': [
			Section('General Info', 'general_info', True, False, False, '''
Render Types are stored as 1-byte integers in the ATRB chunk of materials.  
**See Also:** [Inside Edit Flags (GT)](http://www.gametoast.com/viewtopic.php?p=279620#p279620)
'''),
			Section('Glow', 'glow', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
1	| 01	| -		| -		|

Glow amount is defined by material color and diffuse texture.

'''),
			Section('Detail', 'detail', True, True, False, '''
ID 	| Hex 	| Data0								| Data1							|
----|-------|-------							|-------						|
2	| 02	| Tiling along U (horizontal)		| Tiling along V (vertical)		|

Tiles a detail texture. Requires an additional texture (detail texture).

'''),
			Section('Scrolling', 'scrolling', True, True, False, '''
ID 	| Hex 	| Data0										| Data1								|
----|-------|-------									|-------							|
3	| 03	| Scrolling along U (horizontal)			| Scrolling along V (vertical)		|

Scrolls the texture positively. To scroll in the other directions flip the texture coordinates.

'''),
			Section('Specular', 'specular', True, True, False, '''
ID 	| Hex 	| Data0		| Data1	|
----|-------|-------	|-------|
4	| 04	| -			| -		|

Enables Specular. Specular Flag doesn't seem to be needed for it to work. Specular power is affected by material color and Specular Decay (gloss).

'''),
			Section('Glossmap', 'glossmap', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
5	| 05	| -		| -		|

This uses the diffuse texture's alpha channel for specular intensity. Specular Color and Decay are used to determine specularity. Make sure the values are valid. If they are too low the specular might not appear. If the diffuse texture doesn't have an alpha channel specular will be turned off.

'''),
			Section('Chrome', 'chrome', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
6	| 06	| -		| -		|

Environment map. Gives the illusion of reflection on a surface. If no environment map is specified as Texture1 then the game will choose one dynamically at run time.
If the object is static or does not move you should provide an environment map.
'''),
			Section('Animated', 'animated', True, True, False, '''
ID 	| Hex 	| Data0											| Data1					|
----|-------|-------										|-------				|
7	| 07	| Number of frames in the texture (Minimum: 4) 	| Animation Speed. 		| 

Animates UVs to loop through different UV positions on the texture. UVs should be mapped to the first cell and not the whole texture. Cells have to be square and will be calculated automatically from the number of frames.  
The number of cells always habe to be square (4, 9, 16, etc).

See also: [Render Animated discussion on GT](http://www.gametoast.com/viewtopic.php?p=361010#p361010)

'''),
			Section('Ice', 'ice', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
8	| 08	| -		| -		|

Ice.

'''),
			Section('Sky', 'sky', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
9	| 09	| -		| -		|

Sky.
'''),
			Section('Water', 'water', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
10	| 0a	| -		| -		|

Water.
'''),
			Section('Lightmap', 'lightmap', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
11	| 0b	| -		| -		| 

Basically a glow map. Requires an additional texture. The texture's alpha channel determines glow strength, rgb glow color and intensity.

See also: [Lightmap discussion on GT ](http://www.gametoast.com/viewtopic.php?p=323899#p323899)

'''),
			Section('2 Scroll', '2scroll', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
12	| 0c	| -		| -		|

2 Scroll.
'''),
			Section('Rotate', 'rotate', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
13	| 0d	| -		| -		|

Rotate.
'''),
			Section('Glow Rotate', 'glow_rotate', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
14	| 0e	| -		| -		|

Glow Rotate.
'''),
			Section('Planar Reflection', 'planar_reflection', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
15	| 0f	| -		| -		|

Planar Reflection.
'''),
			Section('Glow Scroll', 'glow_scroll', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
16	| 10	| -		| -		|

Glow Scroll.
'''),
			Section('Glow 2 Scroll', 'glow2scroll', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
17	| 11	| -		| -		|

Glow 2 Scroll.
'''),
			Section('Curved Reflection', 'curved_reflection', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
18	| 12	| -		| -		|

Curved Reflection.
'''),
			Section('Normalmap Fade', 'normalmap_fade', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
19	| 13	| -		| -		|

Normalmap Fade.
'''),
			Section('Normalmap Inv Fade', 'normalmap_inv_fade', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
20	| 14	| -		| -		|

Normalmap Inv Fade.
'''),
			Section('Ice Reflection', 'ice_reflection', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
21	| 15	| -		| -		|

Ice Reflection.
'''),
			Section('Ice Refraction', 'ice_refraction', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
22	| 16	| -		| -		|

Models bend the light (see Bothan Spy). Model behaves as a transparent object but the transparency is distorted. Alpha channel of the diffuse is used to control the opacity. Requires an additional bump texture which controls amount of distortion. 
A refraction object can have an optional environment map associated with it.

See also: [Ice Refraction discussion on GT ](http://www.gametoast.com/viewtopic.php?p=397720#p397720)
'''),
			Section('Emboss', 'emboss', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
23	| 17	| -		| -		|

Emboss. Requires an additional texture. Purpose uncertain. Might control specular.
'''),
			Section('Wireframe', 'wireframe', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
24	| 18	| -		| -		|

Wireframe.
'''),
			Section('Energy', 'energy', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
25	| 19	| -		| Throbbing frequency.		|

Makes the texture/material throb.
'''),
			Section('Afterburner', 'afterburner', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
26	| 1a	| -		| -		|

Afterburner.
'''),
			Section('Bumpmap', 'bumpmap', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
27	| 1b	| -		| -		|

Requires an additional texture (greyscale bumpmap or normalmap). The bumpmap needs a .option with -format bump in it. Specular flag should be enabled for better effect.

See also: [Bumpmap tutorial on GT ](http://www.gametoast.com/viewtopic.php?p=262541#p262541)
'''),
			Section('Bumpmap + Glossmap', 'bumpmap_glossmap', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
28	| 1c	| -		| -		|

Requires an additional texture (greyscale bumpmap or normalmap). The bumpmap needs a .option with -format bump in it.
Optional texture which controls the specular intensity through it's alpha channel. Specular flag should be enabled for better effect.

See also: [Bumpmap tutorial on GT ](http://www.gametoast.com/viewtopic.php?p=262541#p262541)
'''),
			Section('Teleportal', 'teleportal', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
29	| 1d	| -		| -		|

Teleportal.
'''),
			Section('MultiState', 'multistate', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
30	| 1e	| -		| -		|

MultiState.
'''),
			Section('Shield', 'shield', True, True, False, '''
ID 	| Hex 	| Data0	| Data1	|
----|-------|-------|-------|
31	| 1f	| -		| -		|

Shield.
'''),
		]
	}
