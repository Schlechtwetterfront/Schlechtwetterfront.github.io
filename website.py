from page_core import *

pages = [
	{
		'page_template': 'index_template.html',
		'path': '',
		'output_file': 'index.html',
		'output_folder': '',
		'page_title': 'Schlechtwetterfront',
		'social_links': [
			SocialLink('https://github.com/Schlechtwetterfront', 'img/github_white.png'),
			SocialLink('https://twitter.com/schlchtwtrfrnt', 'img/twitter_white.png'),
			SocialLink('http://steamcommunity.com/id/andeweget/', 'img/steam_white.png'),
			SocialLink('https://youtube.com/user/andeweget', 'img/youtube_white.png')
		],
		'projects': [
			Project('XSI ZETools', pid='zet', links=[Link('Downloads', 'https://github.com/Schlechtwetterfront/xsizetools/releases'),
	                                                 Link('Overview', '/xsizetools'),
	                                                 Link('View Source on GitHub', 'https://github.com/Schlechtwetterfront/xsizetools'),
	                                                 Link('GameToast Forum Thread', 'http://gametoast.com/viewtopic.php?f=36&t=26664')]),
	        Project('SoftCry', pid='sc', links=[Link('Downloads', 'https://github.com/Schlechtwetterfront/softcry/releases'),
	                                            Link('Overview', '/softcry'),
	                                            Link('View Source on GitHub', 'https://github.com/Schlechtwetterfront/softcry'),
	                                            Link('CRYDEV Forum Thread', 'http://www.cryengine.com/community/viewtopic.php?f=315&t=102978')]),
	        Project('ZE File Formats', links=[Link('Overview', '/ze_filetypes'),
	                                          Link('Download Source', 'https://github.com/Schlechtwetterfront/ze_filetypes/archive/gh-pages.zip'),
	                                          Link('View Source on GitHub', 'https://github.com/Schlechtwetterfront/ze_filetypes')])
		]
	},
	{
		'page_template': 'project_index.html',
		'path': '../',
		'output_file': 'project_index.html',
		'output_folder': 'xsizetools',
		'page_title': 'XSI ZETools',
		'categories': [
			Category('Downloads', [
							   Link('Releases', 'https://github.com/Schlechtwetterfront/xsizetools/releases'),
							   Link('C++ Source (deprecated)', 'http://schlechtwetterfront.github.io/xsizetools/XSIZETools_src.7z')
							   ]),
			Category('General Info', [
							   Link('Main Info', '#main_info'),
							   Link('Download & Installation', '#download_installation'),
							   Link('Contributors', '#contributors'),
							   ]),
			Category('Guidelines', [
							   Link('Export', '#export-guidelines'),
							   Link('Import', '#import-guidelines'),
							   Link('Cloth', '#cloth-guidelines'),
							   ]),
			Category('Documentation', [
							   Link('Scripts', '#scripts'),
							   Link('.msh Export', '#export-docs'),
							   Link('.msh Import', '#import-docs'),
							   Link('Material Manager', '#material-docs'),
							   Link('MSH 2 TXT', '/msh2text.html'),
							   Link('Animation Export', '/animation_export.html'),
							   ]),
			Category('Other Resources', [
							   Link('View on GitHub', 'https://github.com/Schlechtwetterfront/xsizetools'),
							   Link('View Thread on GameToast', 'http://gametoast.com/viewtopic.php?f=36&t=26664')
							   ]),
			Category('Personal', [
							   Link('Schlechtwetterfront', 'http://schlechtwetterfront.github.io/')])
		],
		'sections': [
			Section('Main Info', 'main_info', '''XSIZETools is an addon for Softimage (tested with ModTool 7.5, 2012 SP1 and 2014).
The main features are full export and import of 3D .msh files for ZeroEngine (Star Wars Battlefront I and II). That includes geometry, materials with all ZeroEngine-specific flags, animations and collisions.
<br><br>
This began as a small collection of scripts to help setup hierarchies and the like and turned into a full-fledged exporter/importer for the .msh format. As only a small amount of the .msh file format structure was known when I began writing the exporter I had to reverse-engineer (with contributions from a handful of other people) the rest (which was about 70% of the chunks).
'''),
			Section('Download & Installation', 'download_installation', '''
The main chunk of the project is hosted on GitHub.
The source for the CGeometryAccessorWrappers can be found on the sidebar (the source is outdated though as I lost the code used for the current DLLs.
Check the sidebar for a link to the releases page on GitHub.
<br><br>
To install ZETools, unzip the downloaded archive into <br>
<strong>C:/users/%user%/Autodesk/Softimage_%version%/Addons/</strong> <br>
OR <br>
<strong>C:/users/%user%/Softimage/Softimage_%version%/Addons/</strong>. <br><br>
Make sure you use this path and not the factory addon path.

If you have any Softimage version up to (and including) 2010 you need to install

<a class="normal_link" href="http://www.python.org/ftp/python/2.6.6/python-2.6.6.msi">python</a>
and
<a class="normal_link" href="http://sourceforge.net/projects/pywin32/files/pywin32/Build%20217/pywin32-217.win32-py2.6.exe/download">pywin32</a>. <br>
If python and pywin32 was installed correctly it should look something like
<a class="normal_link" href="installed_python.jpg">this</a>.<br>
<br>
The low-level geometry functions are written in C++, so the Visual C++ 2010 redist is required.
<a class="normal_link" href="http://www.microsoft.com/download/en/details.aspx?id=5555" target="_blank">x86</a> 
|
<a class="normal_link" href="http://www.microsoft.com/downloads/de-de/details.aspx?FamilyID=bd512d9e-43c8-4655-81bf-9350143d5867" target="_blank">x64 </a>(only if x86 didn't work).
'''),
		Section('Contributors', 'contributors', '''
<strong>ME (ANDEWEGET/Ande)</strong>
All programming - Graphics/UI - Main .msh file research
<br>
<strong>AceMastermind (gametoast.com)</strong>
    Created most  templates - Provided example .msh files - Additional .msh research
<br>
<strong>DarthD.U.C.K (gametoast.com)</strong>
    Created some templates - Provided example .msh files - Additional .msh research
<br>
<strong>tirpider (gametoast.com, swbfgamers.com)</strong>
    Additional .msh research - MSH Info Tool greatly helped with debugging - Interesting discussions
<br>
<strong>FragMe! (gametoast.com)</strong>
    Provided a tool/material for some additional research

'''),
		ListSection('Export', 'export-guidelines', [
			'''The CheckSel function in the export dialog can detect some problems.''',
			'''The currently selected object + all it's children will be exported.''',
			'''<strong>Overlapping clusters:</strong> Might break the .msh file. Might mess up the exported .msh's UVs/Weights/Vertex Colors.''',
			'<strong>5-Sided(or more) Polygons:</strong> Might break the .msh file. Will mess up export result(missing polies).',
			'<strong>Supported Model Types:</strong> The supported model types are: poly mesh, null, bone.',
			'''Only apply one 'master' UV projection to a object. All subsequent projections should be Sub-projections.''',
			'Collision meshes can be created by naming the model <em>collision_*</em> or <em>*_collision</em>.',
			'For XSI ZETools to recognize collision primitives the name needs to contain the type of primitive (cube, cylinder, sphere).',
			'Do not freeze any primitives, freezing will remove essential information.',
			'''It's not important how you animate bones (FK or IK etc), the exporter will go through all frames one-by-one and get the current local transforms of every bone.''',
			'<strong>Always apply the envelope to ALL bones.</strong> This might slow your workflow down but it ensures the points are weighted to the correct bone after export.',
			'Only weight to objects with bone in their name(NOT: root, eff).',
			'''Try to apply the envelope only to models which won't be merged after weighting. This does not have to break the .msh, it could though.''',
			'''<strong>No Materials:</strong> You should have at least one material named Scene_Material when exporting. If you have at least one material you don't need Scene_Material.''',
			'''<strong>Material/Render flags are applied per material.</strong> You can apply them by opening the ZETools Material Manager, selecting a material and then clicking "ZE-ify".
			This will add all the ZeroEngine material flags to the material.
			Afterwards inspect your material (click the "Edit" button) and change those settings in the appended options.''',
			]),
		ListSection('Import', 'import-guidelines', [
			'Animations will be imported as linear animations on a per-frame basis.',
			'It should be possible to re-export animations directly after import. For SWBF1 you need to have at least one material though.',
			'There might be some misplaced edges.',
			]),
		ListSection('Cloth', 'cloth-guidelines', [
			'''Try to avoid triangles in the cloth mesh. There's a high change triangles might produce artifacts in the cloth simulation.''',
			'''Cloth will be split along UV seams, so UV accordingly.''',
			'''If you have problems with cloth simulation artifacts, provide a screenshot from the debug SWBF.exe with "render_cloth_connections" enabled via the console.''',
			]),
		Section('Scripts', 'scripts', '''
<strong>Create Bone Group</strong> <br>
Creates a group of all objects which have 'bone' in their name. If you have a SWBF2 skeleton in your scene this will group all bones you need to envelope to.
<br><br>
<strong>Addon Mesh Setup</strong> <br>
Creates an addon mesh hierarchy, by creating a null (named like the *Addon Root* text box) and matching its position and rotation to the selected *Addon Bone*. You can then move the currently selected object(s) into the hierarchy by pressing *Set As Addon Mesh*.
'''),
		ListSection('Export UI', 'export-docs', [
			'<strong>Auto-Overwrite.</strong> Overwrites any output files if they already exist.',
			'<strong>Use root model name for .msh file name.</strong> Will use the name of the topmost object in the currently selected hierarchy as the .msh file name. Has to be enabled when Batch Exporting.',
			'<strong>Batch Export.</strong> Exports all children of the currently selected object as a full hierarchy.',
			'<strong>Export Animation.</strong> Exports animation for the current frame range.',
			'<strong>Current Frame as Basepose.</strong> Exports only the currently selected and following frame to minimize file size.',
			'<strong>Check Sel.</strong> Loops through all objects in the currently selected hierarchy and analyzes it for problems which could cause a bad export.',
			'<strong>Check Sel: Bad model type.</strong> Only nulls, bones and polygon meshes should be used.',
			'<strong>Check Sel: Bad Faces.</strong> Faces should not have more than 4 sides. To fix use Modify>PolygonMesh>Triangulate or Select>Select n-sided polygons>Five sides or more.',
			'<strong>Check Sel: Bad Clusters.</strong> Overlapping clusters, should be fixed.',
			'<strong>Check Sel: Unnecessary clusters.</strong> Do not need to be fixed, just warnings.',
			'<strong>Store Flags.</strong> Stores the current export configuration (path, check boxes etc).',
			]),
		ListSection('Import UI', 'import-docs', [
			'<strong>Texture Folder.</strong> If the textures for the to-be-imported .msh file are not located in the same folder as the .msh file.',
			'<strong>Set Frame Range.</strong> Will set the frame range to that stored in the .msh file.',
			'<strong>Apply animation to selected hierarchy.</strong> If you have already imported a .msh file (like a unit) then you can apply an animation stored in another .msh file to the previously imported mesh (root of that hierarchy must be selected).',
			'<strong>Null Display Size.</strong> Set the display size of nulls.',
			'<strong>Ignore Geometry.</strong> Will replace any meshes with nulls, use this if you are applying an animation to a hierarchy.',
			'<strong>Ignore Animation.</strong> Ignores any animation. Use this if you are importing baseposes to later apply animations (and just generally if you do not need the animation).',
			'<strong>Color Nulls.</strong> Will color nulls if the importer can find out which type they are (bones, effs and roots).',
			'<strong>Hide Roots/Effectors.</strong> Will hide roots and effectors in the hierarchy so they are not accidentally animated.',
			'<strong>Wield Boundary Edges.</strong> Imported meshes usually have splits along the UV seams. This option will wield any of these edges after geometry import.',
			'<strong>Store Flags.</strong> Stores the current import configuration (path, check boxes etc).',
			'<strong>Triangulate.</strong> Triangulates any quads or more-sided polygons on import.',
			'<strong>Log.</strong> Logs the MSH unpack (can be slow).',
			]),
		ListSection('Material Manager', 'material-docs', [
			'<strong>Create.</strong> Creates a new Phong material with the name in the box to the left of the button.',
			'<strong>Edit.</strong> Will inspect the currently selected material for editing.',
			'''<strong>ZEify.</strong> Will add ZeroEngine specific material and shader settings to the selected material(s). This lets you add features like scrolling textures, glow, bump mapping and many more.<br>
                For more information on render types <a class="normal_link" href="http://schlechtwetterfront.github.io/ze_filetypes/rendertypes.html">look here</a>. Textures listed under <strong>Additional</strong> on that page will need to be put into the <em>Texture 1-3</em> slots.''',
			'<strong>De-ZEify.</strong> Removes ZeroEngine specific settings.',
			'<strong>Remove.</strong> Deletes the currently selected material(s).',
			'<strong>Assign Tex.</strong> Opens a dialog to assign a color/diffuse texture to the selected material.',
			'<strong>Assign.</strong> Assigns the currently selected material to the currently selected component/object in the scene.',
			'<strong>Unassign.</strong> Unassigns the material.',
			]),
		]
	}
]
