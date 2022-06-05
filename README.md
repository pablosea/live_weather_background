# Live Weather Desktop Background

## About
I never check the weather and I'm tired of hurricanes sneaking up on me.

This program grabs NOAA Satalitte images from their [site](https://www.star.nesdis.noaa.gov/GOES/sector.php?sat=G16&sector=car) and updates your desktop background as often as you'd like.


## How to use:
### Edit the Code
Edit the xpath to the image source you want 
ie.. "GeoColor: 4000 x 4000 px" and then add "/@href" to the end of the xpath tag to grab the link to the image.

### Update background
In your windows task scheduler; set this script to run as often as you would like.
(NOAA images are updated every 5 minutes so no need to run it faster than that.)