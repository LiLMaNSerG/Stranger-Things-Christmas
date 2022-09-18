# A *Stranger Things* Christmas
A Christmas light display inspired by the show "Stranger Things".

## About the Project
I was inspired by the *Stranger Things* S1E3 episode ["Holly, Jolly"](https://youtu.be/jIQ9z2bxXyg?t=143) to create my own window display for the Christmas season. Powered by a RaspberryPi and RGB adressable lights, you can create an endless pallate of colors, patterns, and messages to decorate your home for the holidays.  

**Check it out!**
- [Stranger Things Pattern](https://youtube.com/shorts/BymeMe01auQ?feature=share)

## Getting Started
### Supplies
- [RBG Addressable LED Bulbs](https://www.aliexpress.com/item/2255800248172165.html?spm=a2g0o.productlist.0.0.74976208uKK60Y&algo_pvid=a2220219-82c4-419d-ad9c-ef6253fb2516&algo_exp_id=a2220219-82c4-419d-ad9c-ef6253fb2516-16&pdp_ext_f=%7B%22sku_id%22%3A%2210000001794476841%22%7D&pdp_npi=2%40dis%21USD%2124.0%2124.0%21%21%21%21%21%4021031a5516634548348473792eca13%2110000001794476841%21sea&curPageLogUid=l6cWeQ7v3NDj) : I purchased mine from Aliexpress. Ideally, it should come with a connector for POWER, **Data**, and GROUND.
- RaspberryPi Model B+ Ver 1.2 : I had this one laying around, but any version 2 or higher will work.
- [Stranger Things Alphabet Decals](https://www.etsy.com/listing/602357061/stranger-alphabet-wall-decals-scary?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=stranger+things+decal&ref=sr_gallery-1-2&frs=1&bes=1&sts=1&organic_search_click=1) : Perfect for this project.
- [3V to 5V Level Shifter](https://www.adafruit.com/product/1787) : The DATA pin for the LED Bulbs requires a 5V input. This chip let's us use the output from the RaspberryPi (3.3V) to drive the LED Bulb pin at the adequate voltage.
- [Project Box](https://www.amazon.com/Waterproof-Plastic-Electronic-Junction-Enclosure/dp/B07TS6RY85/ref=sr_1_6?crid=2X4TBBF9IHWXJ&keywords=project+box&qid=1663455227&sprefix=project+bo%2Caps%2C147&sr=8-6)
- [DC Power Jack Adaptor](https://www.amazon.com/gp/product/B01J1WZENK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [5V 10A Power Supply](https://www.amazon.com/gp/product/B07H9XRZBP/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) : Necessary for powering the LED Bulbs.
- [Breadboard](https://www.amazon.com/DaFuRui-tie-Points-Solderless-Breadboard-Compatible/dp/B07KGQ7H8B/ref=sr_1_12_sspa?crid=1F83XRI4350YW&keywords=breadboard&qid=1663456870&s=industrial&sprefix=breadboar%2Cindustrial%2C164&sr=1-12-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFDMklDTUU2V1VTNiZlbmNyeXB0ZWRJZD1BMDc5NzMyMDJOVkI1NkZKSFRTNDQmZW5jcnlwdGVkQWRJZD1BMDU2NjA5NTJIM0JQN0VQVzRXWkMmd2lkZ2V0TmFtZT1zcF9tdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl) : I opted to use a breadboard for easier prototyping.

### Setup
![Stranger Things Project Box](https://user-images.githubusercontent.com/15962563/190879736-4345d519-14d3-49de-8ced-50c4f2303aac.jpg)
