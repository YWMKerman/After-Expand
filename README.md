# _The AfterExpand Mod_


_“来了，爱了，给Ta一颗星星，走了”_
_<p align="right">- 《三体 III 死神永生》 </p>_


_"AEX is not just about exploring stars — it’s about exploring time itself.
See what our cosmic neighborhood might look like billions of years from now."_

<img width="2048" height="800" alt="AEX" src="https://github.com/user-attachments/assets/feaa00c9-1bac-4e12-b379-20f2de87b978" />

***

AfterExpand (AEX) is a Kerbal Space Program (KSP) mod that expands upon the AfterSolarSystem project.
It adds at least 10 scientifically plausible nearby star systems for you to explore — all modeled as they might appear billions of years in the future, when the Sun has evolved into its red giant stage.
_**In AEX, the positions of nearby stars are assumed to remain roughly unchanged. Based on that, the mod presents a speculative but realistic future snapshot of the solar neighborhood, featuring:**_

-	Alpha Centauri System – now consisting of a red giant and a white dwarf

-	Barnard’s Star – still on the main sequence.

-	Sirius System – both stars have ended their lives as white dwarfs.

-	Epsilon Eridani (ε Eri) – nearing the end of its main sequence phase.

-	Tau Ceti (τ Cet) – evolving toward a subgiant state. 

- ...

Unlike purely fictional expansions, AEX maintains a balance between realism and fun, offering an immersive scientific experience without unnecessary exaggerations.
For instance, planets like TRAPPIST-1b won’t feature unrealistically thick atmospheres — atmospheric models are designed to be scientifically grounded yet engaging.
In addition to real-world stars, AEX includes several fictional systems created by collaborator Linfox.
While fictional, their planetary architectures, atmospheres, and physical parameters still follow realistic astrophysical principles.
*Don’t like fictional systems?*
*No problem — you can disable them entirely in the mod’s configuration settings.*

AEX is designed as a counterpart to RealExpand, but with a stronger emphasis on scientific consistency and future plausibility.
It’s meant to complement the AfterSolarSystem mod, extending your journey beyond the far-future Sun into the wider cosmos.

 ## _**Known Limitations**_
Due to KSP’s floating origin and precision issues, you may encounter graphical artifacts such as:
- “cracked” terrain
- surface “mosaic” glitches
- or physics instability

These effects become more common when you travel several light-years away from the original solar system.
 ***Tip: If you use the in-game console to teleport a vessel directly to a distant star system,
these issues will almost certainly occur.
To minimize them, first teleport your craft into a high, stable orbit around the target Body,
then manually descend to the surface.***

***
# _Compatibility and  Mod Installation:_
<img width="2500" height="862" alt="awa" src="https://github.com/user-attachments/assets/dcc9d564-526b-4fbf-a11e-95930010caae" />

## **AfterSolarSystemExpand is compatible with (or provides support for) the following mods：**

- Scatterer
- EnvironmentalVisualEnhancements
- Distant Object Enhancement
- PlanetShine
- ParallaxContinued

## **AfterSolarSystem is not compatible with the following mods：**

- Principia
- External visual mods (RVE, RSSVE, EVO, etc.)
- External planet mods (RealExpand, AfterKerbin, BeyondHome, etc.)

***
# _**Installation:**_
<img width="1600" height="800" alt="Trappist-1" src="https://github.com/user-attachments/assets/c94bc228-299b-44e0-b0a9-e022e9095ab4" />

### **_Requirements:_**

- [Kopernicus](https://github.com/Kopernicus/Kopernicus/releases)

 *↑ Download the files above and unzip them, then copy them into [KSP_Root]/GameData*
  
## **_before opening the game:_**
Please make sure that Principia is **not** installed in your GameData directory！

## **_Installation method under RealSolarSystem：_**

- No.1 The AfterExpand installation package already includes a RealSolarSystem installation patch. You can simply drag it along with AfterExpand mod into GameData to replace the original mod.
- NO.2 The second method is to manually open the ```GameData/RealSolarSystem/```directory, find ```RSSKopernicusSettings.cfg```, open it with Notepad, find       ```!Body,* {} ```
in the text and replace it with
```
    !Body[Sun] {}  	  
	!Body[Moho] {}   
	!Body[Eve] {}     
	!Body[Gilly] {}
	!Body[Kerbin] {}    
	!Body[Mun] {}   
	!Body[Minmus] {} 
	!Body[Duna] {} 
	!Body[Ike] {} 
	!Body[Dres] {}  
	!Body[Jool] {}   
	!Body[Laythe] {}   
	!Body[Vall] {}   
	!Body[Tylo] {}   
	!Body[Bop] {}   
	!Body[Pol] {}   
	!Body[Eeloo] {}
```
and save it.


***

# _Contact or learn more:_
<img width="1920" height="952" alt="More" src="https://github.com/user-attachments/assets/dcbf98f2-4ac6-47dd-b0c1-02e5fb03dfc3" />

## _**Questions and Answers**_

_**Q: Why is installing AfterExpand so cumbersome in the RealSolarSystem environment?**_

A: Because the early development of RealSolarSystem was quite limited and poorly structured. In its initial versions, it strictly restricted the appearance of any celestial bodies that did not actually exist in our Solar System. In other words, only real, historically known Solar System objects were allowed, and all other planets or stars were automatically blocked.
As a result, there are two possible ways to install AfterExpand under RealSolarSystem:

-	Direct replacement – simply copy and overwrite the existing files.
-	Manual configuration – manually edit the restricted configuration files to allow additional celestial bodies to appear.

Q: _**Why does AfterSolarSystemExpand appear so large, yet the number of celestial bodies seems small?**_

A: *Unlike traditional planet expansions, AfterSolarSystemExpand uses real-world scale celestial bodies rather than Kerbal Space Program’s scaled-down system.
Because of this, each planet requires high-resolution textures (8K or higher) to maintain visual quality. This results in a much larger overall mod size, even though the number of celestial bodies may appear smaller.*

Q: _**Why is AfterSolarSystemExpand incompatible with Principia?**_

A: *Principia implements N-body physics, meaning it continuously simulates the gravitational interactions of all celestial bodies at once.
In AfterSolarSystemExpand, this involves dozens of solar systems, causing extreme lag and long-term orbital instability. Over time, this can lead to planets or even entire systems being ejected or colliding.*

Q: _**Why are some hot gas giants in AfterSolarSystemExpand blue or white?**_

A: *According to Sudarsky’s gas giant classification, gas giants with equilibrium temperatures above 250 K are classified as Class II (Water Clouds), which appear white due to reflective water clouds.
At even higher temperatures, they become Class III (Cloudless) — appearing blue because their atmospheres lack thick condensate clouds, allowing Rayleigh scattering to dominate.*
***



