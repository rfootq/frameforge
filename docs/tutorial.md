

# FrameForge Tutorial

FrameForge is dedicated for creating Frames and Beams, and apply operations (miter cuts, trim cuts) on theses profiles.

## Create the skeleton

Beams are mapped onto Edges or ParametricLine (from a Sketch for instance)

For a start, we are going to create a simple frame.

1. In a new file, switch to the Frameforge workbench.

2. Create a sketch, and select orientation (XY for instance)

![Create Sketch](images/00-create-sketch.png)

![Select Orientation](images/01-select-orientation.png)


3. Draw a simple square in the sketch... it will be our skeleton

![Create Skeleton](images/02-create-frame-skeleton.png)

4. Close the Sketch edit mode.

## Create the frame

1. Lauch the Profile tool.

![profile](images/10-profiles.png)

![profile](images/10-profiles-task.png)
![profile](images/10-profiles-task-2.png)

1. Select a profile from the lists (Material / Family / Size)

![profiles choice](images/11-profiles-family.png)


You can change the size just below the family, the tool has a lot of predefined profile, you can also change the parameters...


3. In the 3D View, select edges to apply the profile creation:

![Edge Selection](images/13-edge-selection.png)

1. And press OK in the Create Profile Task. Now, you have four profiles !

![Profiles](images/14-profiles-done.png)

![Zoom in profile](images/14-zoom-on-profiles.png)



**And voila ! You have your first frame !**


## Going 3D... Making a cube !

We can build more complexe shapes, and there are severals ways of doing it.

### More Sketchs !

We can add more sketchs into our project:

1. Create a new Sketch
2. Select the same orientation as the previous one (XY)
3. Draw a square the same size and placement as the previous one.


4. Now, change the position of the sketch:

![Base Placement](images/20-sketch-base-placement.png)

![Sketch moved !](images/20-sketch-base-placement-2.png)

And the new sketch is 400mm on top of the first one !

You can therefore use Create Profile Command again to create another square frame !

![Stacked Frames](images/21-stacked-frames.png)

### Parametric Line

You can create parametrics lines for joining two vertexes (points), theses lines can be used with Warehouse Profile as well...

1. one can hide profiles objects with [Space Bar] (it allows to see the sketches)

![Hide profile](images/22-hide-profiles.png)

2. Selects vertexes

![Select Vertexes](images/23-select-vertexes.png)


3. Create Parametric Line

![Create parametric line](images/24-create-parametric-line.png)

![alt text](images/25-parametric-line.png)


You can therefore use Create profile again to create the four vertical beams !

1. Open Create Profile, select the profile you want
2. Select the Parametric lines, click OK.

![alt text](images/26-cube-done.png)



### More Sketchs / Part2 !

There is another ways to add sketchs, that allows to do more complicated stuff...

Sometime you want add a sketch to a specific place, and link it to another sketch. (If you modify the first Sketch, then the second will follow, hopefully)

This is not possible with the Position / Base Placement, that is an absolute position.

We are going to "Map" the sketch to something else.

1. Create a new Sketch, and set orientation to: YZ

I added a circle to the sketch so you can see where it is.. (just for reference !)

![alt text](images/30-mapmode-sketch.png)

2. Click on the map mode property:

![alt text](images/31-mapmode.png)

![alt text](images/32-mapmode-dialog.png)


You can change the map mode, selecting faces, vertexes and edges...

![alt text](images/33-mapmode.png)

Here, our circle is in a new plan, the one at the top left of the screen...

There are a lot of options here.

You can then edit the sketch, and create more line and frames...

## Bevels and corners.

As you can see, the junctions are not that good (yet !). The profiles are centered on the skeleton, and stops right at the end of the edges.

We are going to make corners, and bevels. There are two methods for that.


### Via Bevels property

It is my favorite for simple frame..

Let's hide everything except the first frame we made...

![alt text](images/40-show-first-frame.png)

1. Select one of the profile, and in the property section, go for Bevel Start/End Cut 1/2

![alt text](images/41-bevels.png)

There are 4 entries (Start / End Cut1 Cut2)

That allows you to create bevels in the two axis, at the start or end of the profile.

Negative angles works, and must be used to compensate directions.

You can batch-modify that, by selecting all the profiles....

![alt text](images/42-batchs-bevels.png)

**And Voila ! a square frame !**


### Via End Miter Command

Let's show the other base frame ...

![alt text](images/50-base-config.png)

We first must add offsets to the existing profiles...  (offsets adds up to the dimension of the edge !)

1. add Offset (One profile by one, Or selecting all the profiles and change the offset.)

![alt text](images/51-add-offset.png)

2. Unselect all objects, then select two touching Profiles. (**select faces in the 3D view, not objects in the tree view**)

![alt text](images/52-select-touching-profiles.png)

1. Click on the Create Miter End Command

![alt text](images/53-create-miter-end.png)

**And voila !** You have two "TrimmedProfile"

![alt text](images/54-miter-end.png)


### Via End Trim Command

Let's finish the 3 others corners of the second frame...

![alt text](images/60-startwith.png)

![alt text](images/61-bad-joint.png)

When everything is showed again, you can see the vertical profiles are not cut as they should...

Let's open again the corner manager, selecting "end trim"

![alt text](images/62-endtrim.png)


![alt text](images/62-endtrim-task.png)

1. Select the vertical profile first, add it to the trimmed object with the plus (+) button

![alt text](images/63-select-trimmed-body-1.png)
![alt text](images/63-select-trimmed-body-2.png)

2. Select the face of the profile you want to cut with.. (here, I add to move the view and select the bottom **face**)

![alt text](images/64-select-trimming-boundaries-1.png)
![alt text](images/64-select-trimming-boundaries-2.png)

You can change the cut type: straight or following the other profile.

![alt text](images/64-select-cuttype-1.png)
![alt text](images/64-select-cuttype-2.png)


And you also can add faces related to the other side of the trimmed profile.

## Organizing Objects

That's the bad part.

I find the tree view messy. Really messy.

### Part Container

I often use Part container for grouping profiles, sketchs, etc.

![alt text](images/70-part-container.png)

![alt text](images/71-part-container.png)

You should drag only one profile to the container... I don't know why, but FreeCAD is not happy about a group drag.

Sometime parts and profile get out of the Part Container.



### Fusion

One can fuse profiles together.

![alt text](images/72-fusion.png)

![alt text](images/72-fusion-done.png)

It allows to group objects. 


## Using profiles in Part Design... ie, making holes !

To use all of theses profiles in PartDesign, for instance, to make holes... in it.. !

you need to use a fusion of the profile, and create a body...

![Body](images/80-body.png)

1. Drag and drop the fusion into the body.

![base feature](images/81-basefeature.png)

2. Now, you have a standard Part design Body...

You can map a sketch to any face, and use Part design to do whatever you want !

![Making Holes](images/82-making-holes.png)

![Holes Made](images/83-holes-made.png)