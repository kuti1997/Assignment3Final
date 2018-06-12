# The data for your website
import os

data = {
    # Example of a collection
    "Phones": [
        {
            'name': 'Iphone 8',
            'price': '1000$',
            'category': 'Phones',
            'manufacturer': 'Apple',
            'operating_system': 'IOS',
            'form_factor': 'Touchscreen',
            'dimensions': '1384 x 67.3 x 7.3',
            'weight': '148',
            'battery_capacity': '2100',
            'removable_battery': 'No',
            'colors': 'White, Black, Gold, Silver',
            'image_url': 'images/mobile1.jpg',
            'details': """
            Witness the best display possible on the Apple iPhone 8 thanks to a Retina HD display with True Tone technology. The display automatically adjusts white balance to match the light around you. So if you're in a low light area, the screen will adjust accordingly to help you see better. The Retina HD display also has a wider colour range to brings your photos and movies to life.   

Apple iPhone 8 is the toughest, most durable iPhone to date. The front and back feature glass with a 50% deeper strengthening layer, and a stainless-steel aluminium band that provides additional reinforcement. A special oleophobic coating on the screen makes it easier than ever to wipe off smudges and fingerprints.   

Take your iPhone 8 almost anywhere. With a rating of IP67, it's engineered to resist water, splashes, and dust. So you won't have to worry if you're caught in a downpour, or if you accidentally drop your iPhone 8 in the sink. Just pick it up and dry it off as if nothing happened. """
        },
        {
            'name': 'Samsung Galaxy S9',
            'price': '850$',
            'category': 'Phones',
            'manufacturer': 'Samsung',
            'operating_system': 'Android',
            'form_factor': 'Touchscreen',
            'dimensions': '148.9 x 71.9 x 7.9',
            'weight': '163',
            'battery_capacity': '3300',
            'removable_battery': 'No',
            'colors': 'White, Black, Gray',
            'image_url': 'images/mobile2.jpg',
            'details': """The rear camera on the S9 has a large aperture lens that lets in plenty of light. Lots of light means brighter photos, so nothing gets lost in shadow when you're taking photos inside or at night. The dual aperture camera lets you get creative with your photos, for the perfect shot every time.

Don't put up with blurry photos. Dual Pixel technology lets the S9's autofocus react quickly, so you'll be able to catch the moment your pet does something cute or the second your friend does something silly.

Selfies with friends don't need to look dark and fuzzy. The front-facing camera is designed to let in plenty of light, and autofocus means no one ends up with a blurry face. Or why not use it to bring emojis to life with AR Emojis? They look just like you, so you can bring the personal touch to your messages."""
        },
        {
            'name': 'BLACKBERRY Keyone',
            'price': '650$',
            'category': 'Phones',
            'manufacturer': 'BLACKBERRY',
            'operating_system': 'Android',
            'form_factor': 'Touchscreen',
            'dimensions': '158.1 x 73.8 x 8.5',
            'weight': '180',
            'battery_capacity': '3505',
            'removable_battery': 'No',
            'colors': 'Blue, Black, Purple, Gray',
            'image_url': 'images/mobile3.jpg',
            'details': """
The main 12 MP camera has been created with Sony and can film in stunning 4K Ultra HD, so that everything you film looks vivid and realistic. Featuring a camera sensor that lets in lots of light, you can capture imagery and footage that is bright and full of colour.

The front-facing 8 MP camera can also shoot video at Full HD, so your video chats will look great."""
        },
        {
            'name': 'Google Pixel 2 XL',
            'price': '725$',
            'category': 'Phones',
            'manufacturer': 'Google',
            'operating_system': 'Android',
            'form_factor': 'Touchscreen',
            'dimensions ': '7.9 x 76.7 x 157.9',
            'weight': '175',
            'battery_capacity': '3520',
            'removable_battery': 'No',
            'colors': 'Blue, Black, Gray',
            'image_url': 'images/mobile4.jpg',
            'details': """Whether it's a YouTube video on the train home, or your collection of photos from your latest trip, it all looks stunning on the Google Pixel 2 XL with a 6 pOLED QHD+ display.

The always-on display means you can see important information at a glance, and will even tell you what song is playing in the background."""
        },
        {
            'name': 'Windows Phone 8X',
            'price': '580$',
            'category': 'Phones',
            'manufacturer': 'HTC',
            'operating_system': 'Microsoft Windows Phone 8',
            'form_factor': 'Touchscreen',
            'dimensions ': '132.35 x 66.2 x 10.12',
            'weight': '130',
            'battery_capacity': '1800',
            'removable_battery': 'No',
            'colors': 'White, Black, Gray',
            'image_url': 'images/mobile5.png',
            'details': """Simple yet smart, the HTC Windows Phone 8X is amazingly sculpted with a seamless form. Powered by the 1.5 GHz Qualcomm S4, dual-core processor, this HTC cell phone delivers a quick and efficient performance. Moreover, the HTC Windows Phone 8X runs on the Windows Phone 8 OS, which keeps you entertained with a wide range of applications on its intuitive and user-friendly interface. With a wide 4.3-inch touchscreen made of Corning Gorilla Glass 2, this HTC cell phone is resistant to damage and everyday wear and tear. Thanks to an 8 MP camera, this blue smartphone allows you to capture all the wonderful moments of your life with great clarity. Furthermore, the 16 GB memory of this HTC cell phone lets you comfortably store a lot of your media content. Also, the Wi-Fi 802.11 a/b/g/n connectivity in this smartphone ensures that you stay connected to the Web even while you are on-the-go."""
        },
        {
            'name': 'HUAWEI P8 Lite',
            'price': '500$',
            'category': 'Phones',
            'manufacturer': 'Huawei',
            'operating_system': 'Android',
            'form_factor': 'Touchscreen',
            'dimensions ': '147.2 x 72.9 x 7.6',
            'weight': '147',
            'battery_capacity': '3000',
            'removable_battery': 'No',
            'colors': 'White, Black, Gray',
            'image_url': 'images/mobile6.jpg',
            'details': """There's a 12 MP sensor on board with Huawei's suite of innovative photography apps built in. Whether you're snapping a quick photo of your breakfast for Instagram, or shooting a dramatic panorama, you're guaranteed great results. 

Round the front there's a secondary 8 MP lens for selfies and video calling. And as you can film in Full HD resolution, your Snapchat Story will be completely high res.  """
        },
    ],
    "Laptops": [
        {
            'name': 'MSI GE62VR',
            'price': '1000$',
            'category': 'Laptops',
            'manufacturer': 'MSI',
            'operating_system': 'windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '40 x 383 x 260',
            'weight': '2940',
            'battery_capacity': '8-cell Lithium-ion',
            'removable_battery': 'Yes',
            'colors': 'White, Black, Gold, Silver',
            'image_url': 'images/laptop1.jpg',
            'details': """
            Packed with NVIDIA's latest GeForce GTX 1060 graphics and a 7th generation Intel Core i7 processor, you'll be able to play the newest and most demanding titles, such as Fallout 4 and GTA V.

MSI's special gaming features and innovative Cooler Boost cooling solution means you can play for longer at maximum performance."""
        },
        {
            'name': 'DELL Inspiron 7577 ',
            'price': '850$',
            'category': 'Laptops',
            'manufacturer': 'DELL',
            'operating_system': 'Windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '24.95 x 389 x 247.7',
            'weight': '2650',
            'battery_capacity': '4-cell Lithium-ion',
            'removable_battery': 'Yes',
            'colors': 'White, Black, Gray',
            'image_url': 'images/laptop2.jpg',
            'details': """Expect smooth performance whatever you're doing. An Intel Core i7 processor makes sure applications, games, and daily tasks run smoothly, and without any signs of slowing down.

It lets you play the latest, and best-looking games. Inside the laptop is an NVIDIA GeForce GTX graphics card, which makes them look even better, and guarantees a clear picture.."""
        },
        {
            'name': 'MacBook Air',
            'price': '1500$',
            'category': 'Laptops',
            'manufacturer': 'APPLE',
            'operating_system': 'Mac Os',
            'form_factor': 'Keyboard',
            'dimensions': '17 x 325 x 227',
            'weight': '1350',
            'battery_capacity': 'Lithium-polymer',
            'removable_battery': 'No',
            'colors': 'Silver',
            'image_url': 'images/laptop9.jpg',
            'details': """
Top features:  
Responsive computing with Intel Core i5 processor  
Solid state storage speeds up saving, booting, loading and software  
Compact and beautifully crafted for a premium computing experience  
All day, everyday computing thanks to 12 hour active battery life  
"""
        },
        {
            'name': 'HP Pavilion 14-bk069sa',
            'price': '725$',
            'category': 'Laptops',
            'manufacturer': 'HP',
            'operating_system': 'Windows 10',
            'form_factor': 'Keyboard',
            'dimensions ': '19.9 x 234.8 x 335.8',
            'weight': '1660',
            'battery_capacity': '3-cell Lithium-ion',
            'removable_battery': 'Yes',
            'colors': 'Blue, Black, Gray',
            'image_url': 'images/laptop4.jpg',
            'details': """The Pavilion 14-bk069sa is powered by a reliable Pentium Gold processor - it offers smooth multitasking performance for all your everyday tasks thanks to an Intel Pentium Gold dual-core processor which is up to twice as fast as an Intel Celeron processor, and efficient enough to help conserve battery life too. With enough power to perform multiple tasks, you'll be able to edit a photo while watching a video or launch lots of applications."""
        },
        {
            'name': 'HP ENVY x360 15-bp150na',
            'price': '580$',
            'category': 'Laptops',
            'manufacturer': 'HP',
            'operating_system': 'Windows 10',
            'form_factor': 'Keyboard',
            'dimensions ': '19.6 x 248.8 x 359.7',
            'weight': '2160',
            'battery_capacity': '3-cell Lithium-ion',
            'removable_battery': 'Yes',
            'colors': 'White, Black, Gray',
            'image_url': 'images/laptop5.jpg',
            'details': """Don't be caught with an archaic-looking bit of equipment. Designed with attention to beauty and visual flow, this ENVY x360 turns heads in any hip coffee shop or hot-desking workspace.

A clever 360 hinge means you can show off the device in four distinct positions - enjoy Facebook chat in laptop mode, stand it up to present your creative achievements, prop it up in tent position for a Netflix rush or go the tablet way to skim through news headlines. All of this while keeping cool and stylish."""
        },
        {
            'name': 'ASUS VivoBook X405',
            'price': '810$',
            'category': 'Laptops',
            'manufacturer': 'ASUS',
            'operating_system': 'Windows 10',
            'form_factor': 'Keyboard',
            'dimensions ': '19 x 326 x 226',
            'weight': '1600',
            'battery_capacity': '6-cell Lithium-ion',
            'removable_battery': 'Yes',
            'colors': 'White, Black, Gray',
            'image_url': 'images/laptop6.jpg',
            'details': """Wide-angle cameras: Dual 13 MP standard-angle and wide-angle rear cameras with LED flash and wide-angle 5 MP front camera with Selfie Light
Reliable design: IP68 dust and water resistance and passed 14 different military standard tests for durability (MIL-STD-810G certification)
Android 7.0, fast 4G LTE speed, Qualcomm Snapdragon 821 2.35 GHz +1.6 GHz quad-core processor, 4 GB of RAM, 32 GB of internal memory with the option to add up to 2 TB of microSD expandable memory, and 3,300 mAh battery with wireless charging capabilities
Instantly unlock your phone with facial recognition or fingerprint sensor
Unlocked for freedom to choose your carrier."""
        },
    ],
    "Personal Computer": [
        {
            'name': 'ACER G3-710 Gaming PC',
            'price': '950$',
            'category': 'Personal Computer',
            'manufacturer': 'ACER',
            'operating_system': 'windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '510 x 180 x 409',
            'weight': '5000',
            'battery_capacity': 'None',
            'removable_battery': 'No',
            'colors': 'White, Black',
            'image_url': 'images/pc1.jpg',
            'details': """
Powerful gaming machine ideal for the latest games    
High quality sound means it sounds as good as it looks   
Expandable design lets you keep your PC at its best   
Cooling features keep your PC cool under pressure   
The G3-710 Gaming PC is part of our Gaming range, which features the most powerful PCs available today.   
 It has superior graphics and processing performance to suit the most demanding gamer.
"""
        },
        {
            'name': 'DELL Inspiron 3268 Desktop PC',
            'price': '500$',
            'category': 'Personal Computer',
            'manufacturer': 'DELL',
            'operating_system': 'windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '293.1 x 92.6 x 314.5',
            'weight': '3760',
            'battery_capacity': 'None',
            'removable_battery': 'No',
            'colors': 'White, Black',
            'image_url': 'images/pc2.jpg',
            'details': """ Top features:   
Powerful Intel Core i5 processor for a fast, reliable performance   
Large 1 TB HDD lets you store all of your files with ease   
Fast connectivity for a smooth computing experience   
The Dell Inspiron 3268 Desktop PC is part of our Achieve range, which has the latest tech to help you develop your ideas and work at your best. It's great for editing complex documents, business use, editing photos, and anything else you do throughout the day. 
            """
        },
        {
            'name': 'HP Pavilion Power 580-015na Gaming PC',
            'price': '750$',
            'category': 'Personal Computer',
            'manufacturer': 'HP',
            'operating_system': 'windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '	364 x 165 x 378',
            'weight': '4250',
            'battery_capacity': 'None',
            'removable_battery': 'No',
            'colors': 'Black',
            'image_url': 'images/pc3.jpg',
            'details': """
Top features:
Powerful Intel Core i5 processor delivers a smooth gaming experience   
NVIDIA GeForce GTX graphics card brings your gaming visuals to life   
Powerful Intel Core i5 processor   
The HP Pavilion Power 580-015na is powered by a 7th generation Intel Core i5 processor, allowing you to play the latest games. Whether you enjoy the combat experience of Battlefield 3 or prefer to hone your survival skills in Dead Space 3, you'll be able to play your favourite games with confidence."""
        },
        {
            'name': 'HP Pavilion 14-bk069sa',
            'price': '250$',
            'category': 'Personal Computer',
            'manufacturer': 'HP',
            'operating_system': 'windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '458.8 x 216 x 437.5',
            'weight': '2780',
            'battery_capacity': 'None',
            'removable_battery': 'No',
            'colors': 'Gray',
            'image_url': 'images/pc7.jpg',
            'details': """Top features:   
Powerful graphics card helps your games run smoothly and is VR-ready   
Faster performance thanks to AMD Ryzen 3 processor  
Keep cool with vented airflow to your components  
Easy upgrade if you want to boost system performance later on  
The Dell Inspiron 5675 Gaming PC is part of our Gaming range, which features the most powerful PCs available today. It has superior graphics and processing performance to suit the most demanding gamer. """
        },
        {
            'name': 'LENOVO Legion Y520 Gaming PC',
            'price': '250$',
            'category': 'Personal Computer',
            'manufacturer': 'LENOVO',
            'operating_system': 'windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '182 x 467.8 x 402.4',
            'weight': '3275',
            'battery_capacity': 'None',
            'removable_battery': 'No',
            'colors': 'Black&Red',
            'image_url': 'images/pc6.jpg',
            'details': """Top features:   
Multi-task with ease thanks to Intel i5 processor   
Prepare for battle with NVIDIA GeForce GTX graphics card   
VR ready for the next-generation of immersive gaming and entertainment  
Tool-less upgrade helps you personalise your system to your own demands   
Part of our Gaming range, which features the most powerful PCs available today, the Lenovo Legion Y520 Gaming PC has superior graphics and processing performance to suit the most demanding gamer."""
        },
        {
            'name': 'ALIENWARE Aurora R7 Gaming PC - Silver',
            'price': '1750$',
            'category': 'Personal Computer',
            'manufacturer': 'ALIENWARE',
            'operating_system': 'windows 10',
            'form_factor': 'Keyboard',
            'dimensions': '472.5 x 212 x 360.5',
            'weight': '4785',
            'battery_capacity': 'None',
            'removable_battery': 'No',
            'colors': 'Silver',
            'image_url': 'images/pc8.jpg',
            'details': '''Top features:   
Powerful Intel Core i7+ processor ideal for intense gamers   
VR Ready with the GeForce GTX 1080 graphics card   
Optimal airflow to help keep your PC cool at all times   
Designed to be upgradable so you can own a versatile gaming PC   
The Alienware Aurora R7 Gaming PC is part of our Gaming range, which features the most powerful PCs available today. It has superior graphics and processing performance to suit the most demanding gamer.'''
        },
    ],
    "hot_items": [
        {
            'name': 'MacBook Air',
            'video_url': 'https://www.youtube.com/embed/1KIqEmKJ1y0',
            'category': 'Laptops'
        },
        {
            'name': 'Samsung Galaxy S9',
            'video_url': 'https://www.youtube.com/embed/tehQjoZFyGY',
            'category': 'Phones'
        },
        {
            'name': 'Google Pixel 2 XL',
            'video_url': 'https://www.youtube.com/embed/YMFpCwBw7ps',
            'category': 'Phones'
        },
    ],
    "images": [
        {"url": '/shared/images/corgi.jpg'},
        {"url": '/shared/images/cavalier.jpg'},
        {"url": '/shared/images/aussi.jpg'},
        {"url": '/shared/images/corgi.jpg'},
        {"url": '/shared/images/cavalier.jpg'},
        {"url": '/shared/images/aussi.jpg'},
    ],
    "sizes": [
        {"name": "small", "toString": "Small"},
        {"name": "medium", "toString": "Medium"},
        {"name": "big", "toString": "Big"},
    ],
    "cities": [
        {"id": "telAviv", "toString": "Tel Aviv xoxo"},
        {"id": "2", "toString": "Haifa"}
    ],
    "days": [0, 1, 2],
    "hours": [[1, 2, 3, 4], [2, 3, 4], [3, 4]]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection])

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
