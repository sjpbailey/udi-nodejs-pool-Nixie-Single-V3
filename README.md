# nodejs-poolController Plugin for Single Body Nixie Controller

## Using Sequent Mega-BAS with a Sequent 8 Relay Hat

0. This works with Eisy/Polisy, You can add additional circuits tied to relays to start and stop
 the Device however if at anytime a modification is made to pool controller you will need to reinstall this Plugin.

1. Install Nodejs Pool Controller and Dashboard required as a Nixie controller, additional parts listed.

[Nixie Install](https://github.com/tagyoureit/nodejs-poolController/wiki/DIY-Standalone-Nixie-Pool-Controller)

[Resource](https://www.troublefreepool.com/threads/nodejs-pool-controller-work-with-pump-only.246189/)

[Resource](https://sites.google.com/view/randypool/swg/poolcontroller)

[Nodejs PoolController](https://github.com/tagyoureit/nodejs-poolController)

[RS485 Converter](https://www.waveshare.com/usb-to-rs485.htm)

[Sequent BAS HAT](https://sequentmicrosystems.com/products/building-automation-8-layer-stackable-hat-v4-for-raspberry-pi)

[Sequent 8 Relay HAT](https://sequentmicrosystems.com/products/8-relays-stackable-card-for-raspberry-pi)

[RPi-4 8gb](https://www.canakit.com/raspberry-pi-4-8gb.html)

### Installation

1."Configuration" and add the base url to your nodejs-poolController application installation as a "Custom Configuration Parameter" with a key of "api_url"

Default:
api_url: [http://localhost:4200]

![Example:](https://github.com/sjpbailey/udi-nodejs-pool-controller-V3/blob/main/images/Screenshot%202024-03-04%20at%2011.02.50%20PM.png)
