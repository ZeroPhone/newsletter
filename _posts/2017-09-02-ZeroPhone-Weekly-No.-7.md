---
layout: post
title: Sending out ZeroPhones, new revision and 3G
img: 2017-09-02_7_1.jpg 
---

# Sending out ZeroPhones, new revision and 3G

 Gamma ZeroPhones are being sent out. Even though I encountered a problem with display breakouts, which doesn't allow me to send out most of the phones, I still had some spare breakouts which were working. While experimenting, I've destroyed a lot of OLED panels by accident - reverse polarity, clipped edges, some cases are undetermined. This is a hint at one of the challenges which I'll encounter when producing ZeroPhones on a larger scale - by now, I've found a reliable source of display breakouts, but there surely will be issues with other breakouts, too. Currently, 3 phones have been sent out, 3 more are being tested before being shipped, and two more are to be assembled soon. One of first ZeroPhones that was sent out [appeared at DebConf in Montreal](https://bits.debian.org/2017/08/debian-mobile-continues.html), even! (first picture taken from this article, too)  
   
 There's a Delta revision coming. It's supposed to be v1.0, *much like Gamma revision was supposed to be ;-)* This revision, though, is mostly bugfixes, [silkscreen additions](https://github.com/ZeroPhone/ZeroPhone-PCBs/issues/52) (various labels and drawings, to help with assembly and usage), as well as features being removed, so, this far, I don't see any reason why it can't become the hardware v1.0. Also, hardware switches are becoming actual switches, there'll be an option to add [a debug console interface to the charging board](https://github.com/ZeroPhone/ZeroPhone-PCBs/issues/49), assembly will be even more easy - oh, and the PCBs will be red.  
   
 Crowdfunding is going to be soon. It's hard for me to provide an estimate, but eash day I'm making sure I move forward, towards it. In general, I'm going for October right now, coinciding with [Hackaday Prize](https://hackaday.io/prize) final rounds. Right now, I'm pretty much working on "how do I price the kits/assembled phones, how to have enough profit to account for risks and still be able to grow the project, how to promote the crowdfunding efficiently, what content to release during updates" questions, while also doing hardware&a little software+documentation. A little bit of spoilers - there'll be E-Ink support, RTL-SDR, radio communication and removing Intel ME from a laptop, all using a ZeroPhone. There'll be more than that, of course ;-)  
   
 ![](https://gallery.mailchimp.com/055beefeabea5aa48a0c0bc74/images/9caebd29-24bd-4f49-8b31-f5f22f3046c9.png)  
   
 [Here's](https://github.com/ZeroPhone/ZeroPhone-Mod-PCBs/tree/master/sim53x0_breakout) a PCB I'm designing that makes 3G modem board a drop-in replacement for current ZeroPhone back boards, and even though making it fully compatible with current layout is tricky, I'll make sure it is a good drop-in replacement for 2G modem currently used. What that means is - there'll be 3G, and I aim to include it in the crowdfunding campaign. I'm also filming a video while I'm designing the 3G modem breakout board, outlining my reasons for decisions made in the process - hopefully, you'll like it =)  
   
 ![](https://gallery.mailchimp.com/055beefeabea5aa48a0c0bc74/images/34e2fe90-2367-4c38-a86d-86ea143a0033.jpg)  
   
 [I'm also playing with UI](https://github.com/ZeroPhone/pyLCI/tree/prettier_ui). By now, UI elements got the visual representation split into a separate layer, which allows for menus that look in many different ways. This is not in the master branch for now, since it's still experimental and bugs might appear, but it's a great feature to have - the interface can look much better and work with more than just text (also, it's a stepping stone for UI localization, since this feature also allows different fonts to be used). Next in the line - make it easy to customize fonts, menus and other UI elements!  
   
 ![](https://gallery.mailchimp.com/055beefeabea5aa48a0c0bc74/images/0cda64d1-1346-4555-9806-519d5132f84a.jpg)  
   
 If you want to write apps, [here's](https://hackaday.io/project/19035/log/63675) a small tutorial to get you started! More to come, eventually. Also, [pyLCI emulator](http://wiki.zerophone.org/index.php/PyLCI_emulator_setup) (a way to prototype apps without ZeroPhone hardware) got a redesign [thanks to Brian Dunlay](https://github.com/ZeroPhone/pyLCI/pull/12), so it works reliably now (although it temporarily lost the ability to show the splash screen, that's going to be fixed when aforementioned UI branch is merged).  
   
 I'm really bad at this "keeping a newsletter running" thing - for now. I'm making a first reminder app for ZeroPhone (working with MailChimp API to determine time when last newsletter was published), that'd ping me each week about having to designate time to make a new campaign. If this works out, I'll have a new newsletter edition in a week or so. Also, I've switched to a new workflow and it was surprisingly quicker to compile a newsletter than with the format I did before.  
   
 [ZeroPhone Wiki](http://wiki.zerophone.org/index.php/Main_Page) is slowly but surely being filled with content. Creating accounts is now blocked, but you can request one, which is pretty much the same thing, just adds a delay of up to a day (that's approximately how often I check the page with account requests).  
---

## P.S.

 As usual, if you have any suggestions, comments, project ideas or wishes - you can [fill out the survey](https://zerophone.github.io/newsletter/survey/), reply to this e-mail, reach me on [Hackaday](https://hackaday.io/CRImier) or [Reddit](https://www.reddit.com/user/CRImier), maybe comment on [the Hackaday project](https://hackaday.io/project/19035) - whatever works for you! 

  