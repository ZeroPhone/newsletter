---
layout: post
title: Call for contributors, first batch of ZeroPhones and ZeroPhone Wiki
img: ZeroPhone5.jpg
---

# Call for contributors, first batch of ZeroPhones and ZeroPhone Wiki

---

## Project state

You do remember about my plans to build a batch of 10 ZeroPhones - for reviewers? Well, I've got enough money for parts and more, [ordered parts for 20 ZeroPhones](https://hackaday.io/project/19035-zerophone-a-raspberry-pi-smartphone/log/58563-project-state-gamma-boards-finished-beta-boards-released-components-on-the-way), [received them, made some board redesigns to suit the parts](https://hackaday.io/project/19035-zerophone-a-raspberry-pi-smartphone/log/59341-project-state-prototype-batch-will-soon-be-built) and now I'm waiting for the boards to arrive! Once I receive them, I'll assemble about 20 ZeroPhones - they'll go to project contributors, reviewers (for advertising) and a couple of pre-orders. Other than that, I got the most I wanted out of PCBs, for now, and [I'm preparing for the crowdfunding](https://www.crowdsupply.com/arsenijs/zerophone) - it's about a month before it starts, Getting this far wouldn't be possible without all the donations I've received, and I want to thank everybody that helped me collect money for the parts - we finally got through that stage.   

This and the previous weeks were mainly spent by creating a contributor-friendly infrastructure that'd also help ZeroPhone go in the right direction. Most of [software](https://github.com/ZeroPhone/pyLCI/issues) and [hardware](https://github.com/ZeroPhone/ZeroPhone-PCBs/issues) problems were added to GitHub issues, so that it's easier to track progress and see what's yet to be done. A project's contributor - Maxlive_dev - has set up [the ZeroPhone wiki](http://wiki.zerophone.org/index.php/Main_Page) and I've started filling it up with articles, intending to make it a one-stop resource about all things ZeroPhone. I've also set up the #ZeroPhone IRC channel on Freenode ([webchat link](http://webchat.freenode.net/?channels=%23ZeroPhone)) - so pop over if you want to talk about open-source phones and stuff (though I'm going to sleep right now, so maybe in about 8 hours ;-) ) There's now also a protonmail.com email address - the username is "zerophone" (I sure hope spam bots aren't smart enough to crawl through this sentence) .

---

##   
Software

After assembling ZeroPhones and mailing them to recipients, I'll concentrate on apps (and will be writing about that) - but before that, [there are some fundamental software flaws](https://hackaday.io/project/19035-zerophone-a-raspberry-pi-smartphone/log/58572-zerophone-software-pylci-todo-and-challenges) that need to be solved, or worked around. If you're a Python programmer and you'd be interested in contributing, please [take a look at these issues](https://github.com/ZeroPhone/pyLCI/issues) and see if you could help solve some of them. By the way, there's now an emulator so you don't need an OLED just to run the ZeroPhone interface for development; I currently haven't published the instructions for installing it, but I send them out upon requests (ask in IRC?); and will make a wiki page for them this week.

---

##   
Hardware

Gamma boards have been released - [currently in the master branch](https://github.com/ZeroPhone/ZeroPhone-PCBs). I fixed plenty of bugs, added some features and even managed to squeeze in a place for accelerometer/gyroscope breakout (untested). There'll likely be a Delta revision before v1.0 - with bugfixes for Gamma and, maybe, some features added. If you're [interested in helping](http://wiki.zerophone.org/index.php/Contribution_Priorities#Reviewing_ZeroPhone_PCBs_and_working_on_PCB_TODOs) with PCB design, [head here](http://wiki.zerophone.org/index.php/PCB_versions,_features_and_guidelines) and [then here](https://github.com/ZeroPhone/ZeroPhone-PCBs/issues), I'll be happy to hear your thoughts and accept your pull requests =)  

For all those people that were concerned about ZeroPhone assembly - my decision is that CrowdSupply campaign will mostly focus on phones that are as fully assembled as possible, because it appears that not that many people are thrilled with hand-soldering 0603 SMD components and 0.8mm TQFP - in hindsight, it seems to be something obvious =) Of course, the ease of assembly is going to remain for those that intend to assemble a ZeroPhone independently - it's one of project's priorities, not a side-effect. By the way, it's likely there'll also be PCB kits and "PCB kits with most of the small parts" during the campaign =)

---

##   
Contribution priorities

Without doubt, one of the most important things in any project is information that's collected during the project's development. This is why [we now have a wiki](http://wiki.zerophone.org/index.php/Main_Page), and it has to be the main source of detailed information for anybody who's going to be interested in ZeroPhone. However, behind each wiki there's a community effort, and if somebody has some free time and interest, [I ask you to step in and help](http://wiki.zerophone.org/index.php/Contribution_Priorities#Moving_project_information_to_this_Wiki) - the wiki needs content, and that's a list of topics which will need to be covered in ZeroPhone Wiki. There are some points which so far only I know enough to write about, and I myself will concentrate on those - but I've highlighted the "can likely be written by anybody" topics in bold, just so that it's easier to pick a topic to cover for anybody who has the time to do it =)

* * *

**[There's a survey!](https://zerophone.github.io/newsletter/survey/) Many of you have already completed that, and the results have helped me add and plan many features, address concerns and find plenty of great people to work with. If you haven't seen this survey and you would like to express your opinion/ideas/concerns about ZeroPhone, check it out =)**  

This mailing list has grown to over 500 people in the meantime - I'm happy to be able to reach out to you all, knowing that we share the same goals and all want this project to succeed. I've got a huge delay in between mailing list archive again - unfortunately, I had to accept some freelance jobs in order to find the remaining money for ZeroPhone parts. I'll compensate by having one more newsletter this week, and those are the articles I'm about to finish that will go into it:

*   A story about Chinese breakout inconsistencies
*   Privacy concerns and audio hardware switches
*   ZeroPhone interface emulator install instructions - for UI work and app development
*   3D modelling requirements - so we can finally design cases for ZeroPhone

---

##   
P.S.

If you have any suggestions, comments, project ideas or wishes - you can [fill out the survey](https://zerophone.github.io/newsletter/survey/), reply to this e-mail, reach me on [Hackaday](https://hackaday.io/CRImier) or [Reddit](https://www.reddit.com/user/CRImier), maybe comment on [the Hackaday project](https://hackaday.io/project/19035) - whatever works for you!
