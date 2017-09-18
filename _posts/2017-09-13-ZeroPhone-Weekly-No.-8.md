---
layout: post
title: Mod boards, project priorities and building a new batch
img: 2017-09-13_8_1.jpg 
---

# Mod boards, project priorities and building a new batch

   
 There'll be mod boards for ZeroPhone - expanding its capabilities, using the expansion sockets that are added to ZeroPhone. [Here's more about the concept](https://hackaday.io/project/19035-zerophone-a-raspberry-pi-smartphone/log/67055-mod-boards-and-expansion-ports), and [here are descriptions for all mod boards](http://wiki.zerophone.org/index.php/Mod_boards) that I designed so far, on the ZeroPhone Wiki. Some of them are going to be demoed during the crowdfunding, and most of them are likely going to be included in the funding goals in one way or another =)   
   
 One of before-crowdfunding priorities is having a 3D-printed case - at the very least, one. This week, two ZeroPhones will be sent to people that volunteered to help with this, and I'll designate a day or two to finally sort it out from my side - as it's going to require quite some KiCad tinkering.   
   
 3G board proved to be harder than I imagined. I drew the board, then lasercut the outline to see what it looks like. So far, it interferes heavily with the battery connector - my options are:  * Moving the battery connector (won't help completely and will require changing part types, adding a new part to the BOM, which'll unlikely be as easy to obtain)
 * Rotating the modem module 90 degrees (no guarantee everything will still fit, there'll either be things sticking out the ZeroPhone outline or suboptimal antenna connector placement)
 * Moving the modem up from the board (will likely require some custom pin headers)
  There are some more less-likely-to-work options, too, I return to this topic from time to time now. 3G is still doable, just that it's taking longer time to design the board - I'll likely finish it the next week.  
   
 I've been going through all of your survey responses once again, looking for things that I might have missed, and I've also added in my own experience and opinions. So far, the guideline for user-facing software is, almost unilaterally, having phone software that's stable, reliable, responsive and functional - pretty much in this order. Of course, for now I'm mainly researching existing GSM software options - there's a small placeholder GSM modem handler in UI software, but it's too basic and doesn't even handle SMS properly.  
   
 In other news, SIM800 modem appears to have a nasty bug - sometimes, when a voice call is finished (initiated either from ZeroPhone or from another phone to ZeroPhone), the "call is finished" fact won't be detected by the modem until some sort of timeout happens, which takes about 10 seconds. I have to see if, say, ofono or ModemManager has a workaround for it - it wasn't clear from reading their code, and I haven't yet gotten to launch these frameworks properly with ZeroPhone GSM hardware, so it's in the works.  
   
 PSA - if you haven't seen [the recent news about a new Bluetooth vulnerability](https://arstechnica.com/information-technology/2017/09/bluetooth-bugs-open-billions-of-devices-to-attacks-no-clicking-required/%20), you might want to update your Bluetooth drivers - [here's the path I'll be taking](https://unix.stackexchange.com/questions/392001/how-do-i-secure-linux-systems-against-the-blueborne-remote-attack) until kernel&driver updates are pushed out, at least for some of my devices.  
   
 Talking about Bluetooth - there's a way for you to help ZeroPhone! Basically, BCM2835 has two UARTs - "stable-frequency reliable UART" and "unstable-frequency not-so-reliable UART". Currently, ZeroPhone re-maps the "stable frequency UART" to the GSM modem, because GSM first and foremost. Bluetooth, in turn, is re-mapped to the "unstable UART". The question is - can you help with getting Bluetooth to work in the basic configuration, as it is? You need a Pi Zero W or a Raspberry Pi 3, add one line in /boot/config.txt, see how Bluetooth can be brought back to life, test it and document your findings - [more details here](https://hackaday.io/project/19035/log/67082). People who'll help the most will get some Latvian chocolate mailed to them =)  
   
 Slightly unrelated: PayPal limited my account because I was underage when I opened it (that's true, but still feels weird because it was such a long time ago - I'm turning 22 in 6 days). PSA: if there's a chance you opened your PayPal account when you were under 18, be informed that, once PayPal gets to know about this, they'll limit your account and only allow withdraws through customer support. As I've read, if PayPal requests some sort of ID from you and you have concerns about it, best tactic is to withdraw any PayPal balance you have before submitting the ID scans (I'd also make sure that money actually gets to you before submitting). While it's obviously bureaucracy, I can understand why PayPal is doing this - they might get in trouble with underage people accepting ToS of a banking service, as ToS accepted while underage might be considered invalid (IANAL, but this definitely feels like staying on the safe side).  
   
 Thankfully, funds for the next batch of ZeroPhones have been long transferred out by now, I got a new PayPal account and I'm now placing orders for a new batch of ZeroPhone parts, including displays for the currently unfinished batch, Pi Zeros, 3G modems and some more cool hardware to pair with ZeroPhones. I have enough for the basic set of parts&boards and some extras, but [any financial help](https://zerophone.github.io/newsletter/help/#donate) will allow me to buy more (to have more replacement parts in stock and more cool hardware to integrate with ZeroPhone), so donations will be greatly appreciated!   
   
 Next newsletter, likely, will concern self-assembly - I'm going to clean up and reform the available BOMs and, hopefully, finish the [parts sourcing guide](http://wiki.zerophone.org/index.php/Sourcing_ZeroPhone_parts) that I started on Wiki, but haven't yet finished.  
   
---

## P.S.

 If you have any suggestions, comments, project ideas or wishes - you can [fill out the survey](https://zerophone.github.io/newsletter/survey/), reply to this e-mail, reach me on [Hackaday](https://hackaday.io/CRImier) or [Reddit](https://www.reddit.com/user/CRImier), maybe comment on [the Hackaday project](https://hackaday.io/project/19035) - whatever works for you! 

  