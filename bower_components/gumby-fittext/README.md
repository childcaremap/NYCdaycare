Gumby FitText
=============

This module resizes text to fill the available space. Refactored into a Gumby UI module from the awesome [FitText.js](http://fittextjs.com/). For more detailed documentation please check out the [Gumby docs](http://gumbyframework.com).

Installation
------------

A bower package is available to install this module into your project. We recommend using this method to install Gumby and any extra UI modules, however you can alternatively move the individuals files into your project.

	$ bower install gumby-fittext

Include gumby.fittext.js in the same fashion as your other UI modules, after gumby.js and before gumby.init.js. In production you should minify JavaScript files into a single optimized gumby.min.js file, ensuring the order (gumby.js, UI modules, gumby.init.js) is retained. 

	<!--
	Include gumby.js followed by UI modules.
	Or concatenate and minify into a single file-->
	<script src="/bower_components/gumby/js/libs/gumby.js"></script>
	<script src="/bower_components/gumby/js/libs/ui/gumby.skiplink.js"></script>
	<script src="/bower_components/gumby/js/libs/ui/gumby.toggleswitch.js"></script>
	<script src="/bower_components/gumby-images/gumby.images.js"></script>
	<script src="/bower_components/gumby/js/libs/gumby.init.js"></script>
	
	<!-- In production minifiy and combine the above files into gumby.min.js -->
	<script src="js/gumby.min.js"></script>
	<script src="js/plugins.js"></script>
	<script src="js/main.js"></script>

Usage
-----
Using the FitText module is simple. Add the class `.fittext` to any element for the module to initialize with default settings. There are two optional attributes that can be used to customize the behaviour. Specify the rate at which the font size changes using `gumby-rate`, this is an exact copy of [FitText.js's](http://fittextjs.com/) Compressor value. You can also specify minimum and maximum font sizes using the `gumby-sizes` attribute, specify `min|max` sizes separated by a pipe.

    <h1 class="fittext" gumby-rate="0.8" gumby-sizes="14|60">Hello this text will resize to fill the available area</h1>


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

	
	
