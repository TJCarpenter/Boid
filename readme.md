# Boids

This project was inspired by a recent visit to an art museum and a video of a cat of all things. At the museum, there was a projected display of some birds on the ground and when you would move your hand across it, the birds would fly away from your hand. The same was true for the video of the cat. After seeing this, I wanted to make my own version of this with a spare projector that I had laying around.

The start of this project was to first discover what this was called. I found that this was similar or exactly the same as the Boids that Craig Reynolds was talking about. After reading his paper I also came across a paper from Conrad Parker. This went over the psuedo-code and vector math that was needed to make this possible. After that I had everything that I needed to get started. I also had the side challenge of creating this entire thing in NeoVim.

## How it works in my mind

So for each boid, they will follow a strict set of rules for the base behavior of a boid. 
1. Separation
2. Alignment
3. Cohesion

Ill go through each of them. With separation, each boid wants their own personal space. Because of this, they will avoid eachother as best as they can. When the boid gets all up in their personal space, they want to fly in the oposite direction. If there are a collection of boids in their personal space, they will fly in the collective opposite direction. I have also added that the closer that the boid is, the stronger the resulting vector will be.

Alignment will be realted to the perceived direction of the group. With the individual boid wanting to be a part of the group and not be left out all alone to die, it flies to the perceived center of the flock. To do this, it will have a radius that it will consider to be its friendly neighborly distance (the distance that it desires its neighbors to be). By looking at what is around the boid, it will take the collective position and then average it to get the center of mass and then fly towards that.

Cohesion will relate to the overall velocity of the group. So if the group is flying quickly in one direction, it will match the speed of the surrounding boids and match their velocity. The boid will use the same distance as the alignment to check for its friendly neighbors.

Combining all three of these rules you get a somewhat flock. At first, it might look a little jittery but this can be adjusted by going to the gym and lifting some _weights_. Applying weights to each of the resulting vectors and you can get a I Can't Believe Its Not Butter with a few toast crumbs smooth simulation of some flying orbs.

## Preditors

I want to make the flying orbs die. Actually I just want them to fear for their very existance. But don't worry, Ill give them the advantage of speed so they have a fighting chance. 

Adding preditors should use some of the same code as the actual boids but with a few differences. First, I need to give them the ability to *HUNT* like the natural born killers they are. To do this, I will give them vison of the surrounding boids and make them go in that general direction. They will mathematically favor large groups rather than trying to pick off and corner the helpless young but maybe I can fix that later.

I've also given them the separation rule as well as the contain rule so that they can stay on the same playing field as the boids. I don't know what is fair in the sense of how can I give the preditors the advantage of capturing the boids. Their size might help but thats for later me (totally not going to do this)

## Running the simlation
Just run `python main.py`



