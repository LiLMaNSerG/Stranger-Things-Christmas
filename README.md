# A *Stranger Things* Christmas
A Christmas light display inspired by the show *Stranger Things*.

## About the Project
After having watched the *Stranger Things* S1E3 episode ["Holly, Jolly"](https://www.youtube.com/watch?v=jIQ9z2bxXyg&t=164s), I was motivated to create my own window display for the Christmas season. Powered by a Raspberry Pi and RGB addressable lights, you can create an endless pallate of colors, patterns, and messages to decorate your home for the holidays.  

[**VIDEO IN ACTION!**](https://youtube.com/shorts/BymeMe01auQ?feature=share)

![Christmas Lights Screenshot](https://user-images.githubusercontent.com/15962563/190881093-5bd219e3-c89d-4c47-8ea9-32bedf4eba52.png)

## Getting Started
### Supplies
- Raspberry Pi Model B+ Ver 1.2 : I had one laying around, but any higher version should work.
- [RBG Addressable LED Bulbs](https://www.aliexpress.com/item/2255800248172165.html?spm=a2g0o.productlist.0.0.74976208uKK60Y&algo_pvid=a2220219-82c4-419d-ad9c-ef6253fb2516&algo_exp_id=a2220219-82c4-419d-ad9c-ef6253fb2516-16&pdp_ext_f=%7B%22sku_id%22%3A%2210000001794476841%22%7D&pdp_npi=2%40dis%21USD%2124.0%2124.0%21%21%21%21%21%4021031a5516634548348473792eca13%2110000001794476841%21sea&curPageLogUid=l6cWeQ7v3NDj) : I purchased mine from Aliexpress. A connector for **POWER**, **DATA**, and **GROUND** is required.
- [Stranger Things Alphabet Decals](https://www.etsy.com/listing/602357061/stranger-alphabet-wall-decals-scary?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=stranger+things+decal&ref=sr_gallery-1-2&frs=1&bes=1&sts=1&organic_search_click=1) : These are perfect for this project.
- [3V to 5V Level Shifter (74AHCT125)](https://www.adafruit.com/product/1787) : The DATA pin for the LED Bulbs requires a 5V input. This chip allows us to use the output from the RaspberryPi (rated at 3.3V) to drive the adequate voltage of the LED DATA input pin.
- [Project Box](https://www.amazon.com/Waterproof-Plastic-Electronic-Junction-Enclosure/dp/B07TS6RY85/ref=sr_1_6?crid=2X4TBBF9IHWXJ&keywords=project+box&qid=1663455227&sprefix=project+bo%2Caps%2C147&sr=8-6)
- [5V-10A Power Supply](https://www.amazon.com/gp/product/B07H9XRZBP/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) : A separate power supply is necessary for driving the LED Bulbs.
- [DC Power Jack Adaptor](https://www.amazon.com/gp/product/B01J1WZENK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [Breadboard](https://www.amazon.com/DaFuRui-tie-Points-Solderless-Breadboard-Compatible/dp/B07KGQ7H8B/ref=sr_1_12_sspa?crid=1F83XRI4350YW&keywords=breadboard&qid=1663456870&s=industrial&sprefix=breadboar%2Cindustrial%2C164&sr=1-12-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFDMklDTUU2V1VTNiZlbmNyeXB0ZWRJZD1BMDc5NzMyMDJOVkI1NkZKSFRTNDQmZW5jcnlwdGVkQWRJZD1BMDU2NjA5NTJIM0JQN0VQVzRXWkMmd2lkZ2V0TmFtZT1zcF9tdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl) : I opted to use a breadboard for easier prototyping.

### Setup

#### Prerequisites
 - [Python 3](https://www.python.org/downloads/)
 - Adafruit's NeoPixel library will be used to interface with the addressable LEDs. Installation instructions can be found [here...](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)

#### Project Diagram
![Christmas Lights Schematic](https://user-images.githubusercontent.com/15962563/190881040-889eec6e-b92b-445c-bab8-a39a8582b8bf.png)

![Stranger Things Project Box](https://user-images.githubusercontent.com/15962563/190879736-4345d519-14d3-49de-8ced-50c4f2303aac.jpg)

### What's Next?
Having the knowledge gained from this project, I would love to extend this application to a full outdoor display for the holidays. In addition to driving different types of lights and chaining patterns together, I am interested in the incorporation of music to synchronize the whole presentation together.

### Contact
You can reach out to me, Sergio Perez, at my [email](sperez.cpp@gmail.com).
