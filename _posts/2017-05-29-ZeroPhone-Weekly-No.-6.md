---
layout: post
title: Building ZeroPhones, UI emulator, and breakout troubles
img: ZeroPhone6.JPG
---

# Building ZeroPhones, UI emulator, and breakout troubles

---

## Project state

[Building 20 ZeroPhones has its own problems.](https://hackaday.io/project/19035/log/60349) I'm setting up and trying to fix a pick&place machine - which isn't too successful so far, but it's the only way I can assemble more than 5 ZeroPhones in a short amount of time. I've met a problem with Chinese breakouts, which have changed pinouts and layout, and I'm also concerned about possibilities of ultrasound tracking of mobile phones, more about all of that below. I saw a lot of visits to [Wiki main page](http://wiki.zerophone.org/index.php/Main_Page) from previous newsletter, then I realized the main page was actually empty - now it's fixed! =) I linked all the existing Wiki articles there, and I plan to move a lot more to it, as well as keep up-to-date **project schedule** and **project plans** documents - once they're done, I'll be linking to those in the next newsletters.  

A project's contributor, [Dillon Nichols](https://tinkerer.us/), has found and designed a lot of [3D components for ZeroPhone boards](https://github.com/ZeroPhone/ZeroPhone-PCBs/issues/12) in KiCad. The plan is simple - as KiCad has built-in board 3D views and export, to make a ZeroPhone 3D model, we need to model all components in 3D, then export the boards as 3D models, stack them together and design cases around that. Now, there are 3 or so components left to design, and that means next newsletter will very likely contain a link to a 3D model of ZeroPhone - so we can start designing ZeroPhone cases!  

---

## Software

Thanks to another project's contributor, Doug, [there's a ZeroPhone UI emulator - with setup instructions.](http://wiki.zerophone.org/index.php/PyLCI_emulator_setup) It's currently being tested, but it works! One small thing - it suffers some threading issues, as pygame isn't very happy when it's called from multiple threads at once. So, for stability, it'll likely need to be rewritten as an external application. [Anybody up for the challenge?](https://github.com/ZeroPhone/pyLCI/issues/10)  

There's some development action going on the Hackaday.io ZeroPhone project chat, and there's now an official ZeroPhone IRC channel. I'm hoping to write a gateway that could link the two - I started looking into Hackaday.io API, but the message-retrieve/message-send part of it seems to be broken. [I hope to get a response from developers](https://hackaday.io/project/5602-hackaday-api/discussion-86181) sometime soon, and once there'll be a simple bot, there'll be better coverage of development progress on IRC. 

---

## Hardware

[Chinese breakouts are a separate source of problems.](https://hackaday.io/project/19035/log/60346) The screen breakouts I received don't yet work (I have to hack them so that they don't conflict with the expansion port), and I needed to redesign the gamma boards to accept the charger breakouts. I'll work it out, but this week will be fun, for sure. Also, it seems I'll be making another ZeroPhone version closer to the end of this year - [more about that](https://hackaday.io/project/19035/log/60346#prz) [here](https://hackaday.io/project/19035/log/60346#prz), too.  

[I received the gamma board panels!](https://cdn.hackaday.io/images//9736321496058721929.JPG) It's kinda obvious from previous messages, but I had to mention this. [They're pretty,](https://cdn.hackaday.io/images//3568271496058830452.JPG) and I'll be assembling a Gamma ZeroPhone today or tomorrow - will get some pretty pictures, too! It's supposed to be prettier than the beta version I currently have, because it's [b](http://orig08.deviantart.net/49d7/f/2017/044/b/2/i_got_you_blue_by_sherapythock-daz0jrb.png)[l](http://orig08.deviantart.net/49d7/f/2017/044/b/2/i_got_you_blue_by_sherapythock-daz0jrb.png)ue, and Chinese breakouts are also mostly blue.  I also received some addon boards - for BIOS chip and ATMega flashing, will be testing them this week - we are going to have a Linux fest at our hackerspace, and that'll involve some Libreboot/Coreboot tinkering =)  

I finally received the current&voltage sensor breakouts, and I'll be measuring and tweaking ZeroPhone power consumption (Pi Zero and Zero W versions) during the crowdfunding campaign - then there'll be a big worklog on power consumption, for both ZeroPhone users and for anybody using Raspberry Pi in their low-power projects.  

---

## Thought pieces

[Ultrasound tracking of mobile phones](http://hackaday.com/2017/05/04/ultrasonic-tracking-beacons/) is real, and affects some Android phones, at least. How can we protect ourselves? How can we thwart it? Does it affect ZeroPhone in any way? That's yet to be determined, but [do read my thoughts about it here.](https://hackaday.io/project/19035/log/60071)  

I'm learning a lot from [the creator](http://rhombus-tech.net/) or [EOMA-68](https://www.crowdsupply.com/eoma68/micro-desktop), who's eager to share experience about designing open standards, manufacturing electronics, crowdfunding and history of open-source tech in general. If you're interested, [there's a mailing list](http://lists.phcomp.co.uk/mailman/listinfo/arm-netbook) where current state of EOMA-68 development and manufacturing is discussed - for me, it's absolutely worth following due to the insights I get.  

[Check out FreedomBox.](https://freedombox.org/) It's a Debian-backed effort to create your own independent personal "cloud", I will install that on my home server (as soon as I find some good SATA cables), and, after that, I'll be considering FreedomBox as a part of ZeroPhone infrastructure.  

---

## Contributing to ZeroPhone project

While I'm adding articles to ZeroPhone Wiki as I move forward with this project, it would help if somebody joined and added some of the things that are on [the Wiki TODO list](http://wiki.zerophone.org/index.php/Contribution_Priorities#Moving_project_information_to_this_Wiki) (the easiest-to-add parts are in bold).  

Also, I'll be shipping 15 ZeroPhones to different parts of the world this week,, and that's going to cost quite some money - about 200$. If you could help me with this, [please do.](https://www.paypal.me/ZeroPhone)

* * *

[There's a survey!](https://zerophone.github.io/newsletter/survey/) Many of you have already completed that, and the results have helped me add and plan many features, address concerns and find plenty of great people to work with - lots of requested things will be added to "ZeroPhone Plans" Wiki page (which I'll be sketching this week). If you haven't seen this survey and you would like to express your opinion/ideas/concerns about ZeroPhone, do check it out =)

---

## P.S.

If you have any suggestions, comments, project ideas or wishes - you can [fill out the survey](https://zerophone.github.io/newsletter/survey/), reply to this e-mail, reach me on [Hackaday](https://hackaday.io/CRImier) or [Reddit](https://www.reddit.com/user/CRImier), maybe comment on [the Hackaday project](https://hackaday.io/project/19035) - whatever works for you!
