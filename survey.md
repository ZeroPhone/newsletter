---
layout: page
title: Survey
permalink: /survey/
---

Here's a short survey you can fill out to help us understand what we could do to improve this project. All fields are optional, feel free to skip questions if you can't think of an answer.


<form id="contact-form" class="form-horizontal" action="https://getsimpleform.com/messages?form_api_token=6593bd835ac595aa3f0a58bbdff4773a" method="POST" enctype="multipart/form-data">
       <fieldset>
            <div class="form-group">
                <label class="col-lg-2 control-label" for="name_optional">Name: (optional)</label>
                <div class="col-lg-10">
                <input type="text" placeholder="Your name" id="name_optional" class="form-control" name="name_optional" tabindex="1"/>
                </div>
            </div>
            <div class="form-group">
                <label class="col-lg-2 control-label" for="email_optional">Email: (optional)</label>
                <div class="col-lg-10">
                <input type="email_optional" placeholder="Your email" id="email" class="form-control" name="email" tabindex="2"/>
                </div>
            </div>
            <br>
            <div class="form-group">
                <label class="control-label" for="expectations">What do you expect from a phone with open-source hardware and software?</label>
                <textarea class="contact-textarea" placeholder="Your expectations" class="form-control" rows="4" id="expectations" name="expectations" tabindex="3"></textarea>
            </div>
            <div class="form-group">
                <!-- this fucking glitch -->
                <label class="control-label" for="plans">What are phone manufacturers doing that you would do differently?</label>
                <textarea class="contact-textarea" placeholder="Your evil plans if you were to manufacture phones" class="form-control" rows="4" id="plans" name="plans" tabindex="4"></textarea>
            </div>
            <div class="form-group">
                <label class="control-label" for="wishes">What do you wish your phone did differently?</label>
                <textarea class="contact-textarea" placeholder="Your complaints" class="form-control" rows="4" id="wishes" name="wishes" tabindex="5"></textarea>
            </div>
            <div class="form-group">
                <label class="control-label" for="badthings">Anything you think is bad/unsatisfying about the ZeroPhone project?</label>
                <textarea class="contact-textarea" placeholder="Why ZeroPhone sucks" class="form-control" rows="4" id="badthings" name="badthings" tabindex="6"></textarea>
            </div>
            <div class="form-group">
                <label class="control-label" for="sourcing">Do you plan to assemble a ZeroPhone after sourcing all the parts yourself? If so, what are the places you can get <a href="https://github.com/ZeroPhone/ZeroPhone-PCBs/blob/master/bom_and_description.xls">the parts</a> from? Does eBay/Aliexpress work for you?</label>
                <textarea class="contact-textarea" placeholder="Building them phones, sourcing them parts" class="form-control" rows="4" id="sourcing" name="sourcing" tabindex="7"></textarea>
            </div>
            <div class="form-group">
                <label class="control-label" for="feature">A feature that you want a lot?</label>
                <textarea class="contact-textarea" placeholder="It should make coffee, too" class="form-control" rows="4" id="feature" name="feature" tabindex="8"></textarea>
            </div>
            <div class="form-group">
                <label class="control-label" for="anything_else">Anything else you want to say?</label>
                <textarea class="contact-textarea" placeholder="Your message" class="form-control" rows="4" id="anything_else" name="anything_else" tabindex="9"></textarea>
            </div>            
           <div class="form-group"> 
           <div class="col-lg-10 col-lg-offset-2">  
         <input type="submit" class="btn btn-primary" value="Send" id="submit"/>
         </div>
         </div>
        <input type="hidden" value="Send message" />
    </fieldset>  
</form>


This form is made functional by [SimpleForm](https://getsimpleform.com){: target="_blank"}.
