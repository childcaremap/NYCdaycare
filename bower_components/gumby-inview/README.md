InView
======

This Gumby Framework Extension makes it easy to assign class names for elements as they appear on the screen (in view). And to remove class names as they fall off the screen (not in view).

For more detailed documentation please check out the [Gumby docs](http://gumbyframework.com).

Installation
------------

A bower package is available to install this module into your project. We recommend using this method to install Gumby and any extra UI modules, however you can alternatively move the individuals files into your project.

	$ bower install gumby-inview

Include gumby.inview.js after gumby.js and before gumby.init.js. 

	<script src="/bower_components/gumby/js/libs/gumby.js"></script>
	<script src="/bower_components/gumby/gumby-inview/gumby.inview.js"></script>
	<script src="/bower_components/gumby/js/libs/gumby.init.js"></script>


Usage
-----
Add `class="inview"` to any element. This will initialize it with default the settings. 

By default, when an element is on the screen (in view) it gets the class name `active` and when its off the screen (not in view) the class name `active` is removed. 

This functionality can be changed by adding the `gumby-classname` attribute to your element.

`gumby-classname=""`
-----
There are 3 different options for customizing the class name that is added to your element when it is in view.

**First Option - Active Class Name Replacement**

	<h1 class="inview" gumby-classname="hello">Inview Example</h1>

By specifying 1 word in the `gumby-classname` attribute this element is given the class name `hello` instead of `active` when its in view. And removed when its not in view.

**Second Option - Active and Deactive Class Names**

	<h1 class="inview" gumby-classname="hello|goodbye">Inview Example</h1>

When you specify 2 words separated by a `|` your class name will be the first word `hello` when it is in view, and your second word `goodbye` when it is not in view. 

**Third Option  (Pro Level) - Active and Deactive Underneath / Deactive Above**

	<h1 class="inview" gumby-classname="hello|hell|heaven">Inview Example</h1>

When you specify 3 words separated by a `|` your class name will be the first word `hello` when its in view, your second word `hell` when its below the screen, and your third word `heaven` when its above the screen.


`gumby-offset=""`
-----

> "Wait a minute...!?" You might be saying. "If a class name changes as soon a something appears on the screen, what's the difference between that and if it has always had that class name to begin with!?"

We can specify a margin so that our effect can be more easily seen. Like with the `gumby-classname` you have a few options.

**First Option - Top and Bottom Together**

	<h1 class="inview" gumby-offset="200">Inview Offset Example</h1>

When you specify 1 number in the `gumby-offset` attribute the extension's class name will wait to be added until your element is at least that value's distance onto the bottom of the screen. And will remove the extension's class name when your element is at most that value's distance away from being completely off the top of the screen.

**Second Option - Top and Bottom Separate**

	<h1 class="inview" gumby-offset="200|400">Inview Offset Example</h1>

As you might expect, when you specify 2 numbers in the `gumby-offset` attribute the first value is applied to the bottom offset and the second number is applied to the top offset. This will give you the ability to delay the effect and tweak how your design is presented. Pair this with `gumby-classname="active|below|above"` and you have a powerful tool for updating the visual impact of your page.

`gumby-target=""`
-----

You can specify a different element to take on the class name on behalf of your element's in view status.
	
	<img id="#diagram" src="placeholder.jpg">
	<h1 class="inview" gumby-target="#diagram">

In this case, the `img` element gets the class name `active` when the `h1` tag is in view. And the `img` element has the class name `active` removed when the `h1` is no longer in view. 

Note: Multiple targets can be used by separating them with a pipe symbol. Eg: `|`

Enjoy!


**MIT Open Source License**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

	
	
