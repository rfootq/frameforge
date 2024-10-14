# FrameForge

Frameforge helps designing beams and frames, with cut, mitter joins and so on


## Prerequisite

- FreeCAD 
  - 1.0
  - 0.21
  - Should work with other

No other packages

## Quick Start


### Create the skeleton

Beams are mapped onto Edges or ParametricLine (from a Sketch for instance)

For a start, we are going to create a simple frame.

1. In a new file, switch to the Frameforge workbench.

2. Create a sketch, and select orientation (XY for instance)

![Create Sketch](docs/images/00-create-sketch.png)

![Select Orientation](docs/images/01-select-orientation.png)


3. Draw a simple square in the sketch... it will be our skeleton

![Create Skeleton](docs/images/02-create-frame-skeleton.png)

4. Close the Sketch edit mode.

### Create the frame

1. Launch the Profile tool.

![profile](docs/images/10-profiles.png)

![profile](docs/images/10-profiles-task.png)
![profile](docs/images/10-profiles-task-2.png)

1. Select a profile from the lists (Material / Family / Size)

![profiles choice](docs/images/11-profiles-family.png)


You can change the size just below the family, the tool has a lot of predefined profile, you can also change the parameters...


3. In the 3D View, select edges to apply the profile creation:

![Edge Selection](docs/images/13-edge-selection.png)

1. And press OK in the Create Profile Task. Now, you have four profiles !

![Profiles](docs/images/14-profiles-done.png)

![Zoom in profile](docs/images/14-zoom-on-profiles.png)



**And voila ! You have your first frame !**


For more information, follow the [tutorial](docs/tutorial.md)




## Maintainer

Vivien HENRY
vivien.henry@inductivebrain.fr


## Credits

This workbench is based on [MetalWB](https://framagit.org/Veloma/freecad_metal_workbench)

Special thanks to:

- Vincent B
- Quentin Plisson
- rockn
- Jonathan Wiedemann

And others people that I don't know but they should be in this [thread](https://forum.freecad.org/viewtopic.php?style=5&t=72389)


## Changelog

- V0.1.1
  - remove f-string with quote and double quote

- V0.1.0
  - Porting code from MetalWB
  - Improving UI
  - Split Corners into EndTrim and EndMiter


## Licence: 

FrameForge is licensed under the [GPLv3](LICENSE)

