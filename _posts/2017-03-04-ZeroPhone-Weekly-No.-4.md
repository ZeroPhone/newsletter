---
layout: post
title: Testing beta hardware, preparing v1.0 and planning - ZeroPhone survey!
img: ZeroPhone4.jpg
---

# Testing beta hardware, preparing v1.0 and planning - ZeroPhone survey!

Sorry for the lack of updates - it's been almost a month, I've just been very busy - won't leave you like that again =) During those four weeks, I made the Nmap app, then went on a hackathon, came back, got the beta boards, fell ill for a couple of days and still managed to get some stuff done. Now I'm testing the beta ZeroPhone, just need to source all of the parts here ASAP - currently I'm out of screens and ESP-12 to assemble a working phone - hoping to get them at the beginning of next week =)  

Plus, I'm working with CrowdSupply to crowdfund a small manufacturing run of ZeroPhones. The more I learn about CrowdSupply, the more I love it and its principles of operation - and I'm learning a lot while preparing this project for the inevitable larger-scale processes it'll have to go through. I'll let you know as soon as there'll be a ZeroPhone landing page on CrowdSupply =)  

I'm kinda rushing this newsletter just to let you guys know there's work being done, right now the main project's bottleneck is, let's say, single-threaded development - due to the simple fact that I can't send the boards for prototypes off to fab (and parts, too) until I test the beta version and fix all the bugs on it. Thus, I'm now working on that and only that. The "thoughts" post, as well as the proper "hardware" and "software" posts (with a video for the nmap app!), will come as soon as I'll finish the back board, and then I'll continue the software development.  

---

## Project state

[Basically, the two paragraphs above,](https://hackaday.io/project/19035/log/53917) in slightly more words. Also, [there was a Raspberry Pi Chat on Hackaday.io today](https://hackaday.io/event/20043-raspberry-pi-hackchat) (you can read the transcript here: [first part](https://hackaday.io/event/20043/log/54287-edited-transcript-of-raspberry-pi-hack-chat​) and [second part](https://hackaday.io/event/20043/log/54291-edited-transcript-of-raspberry-pi-hack-chat-part-2)). Most of my questions (power consumption, for example) were answered (Ctrl+F "Arsenijs" to see the questions I asked). Now, the only thing I'm wondering about is whether this project could receive some kind of help from the RPF engineers. Hopefully, that'll happen and we'll get better power consumption, software support and hardware workarounds - both with my and RPF effort. Whatever the chances are, I'm sure I'll do my part =)  

---

## Hardware

I'm assembling a beta ZeroPhone now. As soon as the testing's over, expect the beta board release (and a corresponding worklog) - with quite a list of TODOs and bugs, there are about 20 now. I'm not going to describe it - I'd better do actual work on the boards, with the time limit that I have, it makes sense.  

For mass-production, I'm thinking about moving to metal dome switches - those clicky springy round pieces of metal you can see if you disassemble a keypad phone, (or even a smartphone - they're also often often used for volume keys) They have a better feel (my fingers get easily tired while writing SMS on ZeroPhone), they're amazingly cheap, oh, and it's trivial to adjust ZeroPhone for that. The best part of it - as it's modular, I don't even need to change much - only the keypad board! And, of course, the "physical buttons you solder on" board is going to remain, for the project hardware accessibility reasons.  

---

## Software

I made a quite chaotic [worklog](https://hackaday.io/project/19035/log/53206-software-notes-on-beta-software-part-1) while making the nmap app. I'm trying to develop some kind of "log as you work"&"worklogs as development tutorials" technique, and it still needs improvement. Nevertheless, if you're determined enough, you might even read through all of this =) I promise I'll get better on this - I'll have plenty of practice.  

---

## More software

I was on a hackathon, remember? We developed a lifestreaming solution - see [our landing page](http://streamo.me). It's not going to be an actual product and was marketed this good just for the fun of it, but my friend is going to work to make it a working device. It's Pi-powered, and I think it can grow into a ZeroPhone "Video streamer" app that could stream to Youtube, Facebook, Twitch and Ustream (or even work as a security camera, for that matter). [Some more on that here](https://hackaday.io/project/19035/log/54298-zerophone-streaming-to-youtube-live-facebook-or-twitch) (if the video isn't yet embedded, that means my laptop still struggles to transcode it, so that I can finally stuff it in Sony Vegas, cut out the interesting parts and put them on YouTube).  

---

## Ways you can help this project

**[There's a survey!](https://zerophone.github.io/newsletter/survey/) I've actually made it about a month ago, but forgot to link it to the third newsletter. Go complete it, I want to know what you're thinking about this project =) **  

I'm still collecting money for the prototype run - I got most of the BOM covered, just struggling to find the last 150$ needed. I'm thinking of a Patreon - to cover the parts I need to buy from time to time, as well as to account for unexpected development expenses (like parts breaking), what do you think?

---

## P.S.

If you have any suggestions, comments, project ideas or wishes - you can [fill out the survey](https://zerophone.github.io/newsletter/survey/), reply to this e-mail, reach me on [Hackaday](https://hackaday.io/CRImier) or [Reddit](https://www.reddit.com/user/CRImier), maybe comment on [the Hackaday project](https://hackaday.io/project/19035) - whatever works for you!
