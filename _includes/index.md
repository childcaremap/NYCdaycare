<article class="avgrund-contents">
<hr>
<h2>Cartodb Map</h2>

<iframe width='100%' height='520' frameborder='0' src='http://schmiani.cartodb.com/viz/77a6017a-b918-11e3-8a7a-0e73339ffa50/embed_map?title=true&amp;description=true&amp;search=false&amp;shareable=true&amp;cartodb_logo=true&amp;layer_selector=false&amp;legends=true&amp;scrollwheel=true&amp;fullscreen=true&amp;sublayer_options=1&amp;sql=&amp;sw_lat=40.47349688875087&amp;sw_lon=-74.553582072258&amp;ne_lat=40.92431462903681&amp;ne_lon=-73.03060233592987' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

<button onclick="avgrund.activate();">Filter</button> 
</article>

<div class="avgrund-cover"></div>

<aside class="avgrund-popup">
<div id="layer_selector" class="cartodb_infobox">
<ul>
<li data-value="all" data-table="nyc_day_care_2013violations_alldescriptions_1" class="selected">All Day Care Centers</li>
<li data-value="0 years - 2 years" data-table="nyc_day_care_2013violations_alldescriptions_1" data-column="age_range">0 - 2 years</li>
<li data-value="2 years - 5 years" data-table="nyc_day_care_2013violations_alldescriptions_1" data-column="age_range">2 - 5 years</li>
<li data-value="yes" data-table="nyc_day_care_2013violations_alldescriptions_1" data-column="certified_to_administer_medication">Certified to give medicine</li>
<li data-value="no" data-table="nyc_day_care_2013violations_alldescriptions_1" data-column="certified_to_administer_medication">Not certified to give medicine</li>
<li id="zipContainer" data-table="nyc_day_care_2013violations_alldescriptions_1" data-column="zip" data-value="zip"><input id="zipSearch" type="text" placeholder="Search by Zip Code" data-table="nyc_day_care_2013violations_alldescriptions_1" data-column="zip" data-value="zip"/></li>
</ul>
<button onclick="avgrund.deactivate();">Close</button>
</div>
</aside>

<p>
This map was made with great help from the <a href="http://betanyc.us/" target="new window">BetaNYC</a> community. This is work in progress, check out the current status on our <a href="https://github.com/child-care-map/NYCmap" target="new window">github repo</a>.
</p>

<hr>

<h2>Google Fusion Table Map</h2>

<div id="map-canvas"></div>

<input id="googft-legend-open" style="display:none" type="button" value="Legend"></input>
  <div id="googft-legend">
    <p id="googft-legend-title">Maximum Capacity</p>
    <div>
      <span class="googft-legend-range">7 to 50</span>
      <img class="googft-dot-icon" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJCAYAAADgkQYQAAAAiElEQVR42mNgQIAoIF4NxGegdCCSHAMzEC81izL7n746/X/VmSowbRho+B8oPhOmKM02zfb/TCzQItYCpDAWpOhA8YFirIoK9xaCFO0FKXrY/rAdq6Lm280gRbeJNikWZDc2RUYhRiBFITDHzwf5LmtjFth3GesyYL6bxoAGQOG0ERpO65DDCQDX7ovT++K9KQAAAABJRU5ErkJggg=="/>
    </div>
    <div>
      <span class="googft-legend-range">50 to 100</span>
      <img class="googft-dot-icon" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJCAYAAADgkQYQAAAAi0lEQVR42mNgQIAoIF4NxGegdCCSHAMzEC+NijL7v3p1+v8zZ6rAdGCg4X+g+EyYorS0NNv////PxMCxsRYghbEgRQcOHCjGqmjv3kKQor0gRQ8fPmzHquj27WaQottEmxQLshubopAQI5CiEJjj54N8t3FjFth369ZlwHw3jQENgMJpIzSc1iGHEwB8p5qDBbsHtAAAAABJRU5ErkJggg=="/>
    </div>
    <div>
      <span class="googft-legend-range">100 to 150</span>
      <img class="googft-dot-icon" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJCAYAAADgkQYQAAAAiklEQVR42mNgQIAoIF4NxGegdCCSHAMzEC+NUlH5v9rF5f+ZoCAwHaig8B8oPhOmKC1NU/P//7Q0DByrqgpSGAtSdOCAry9WRXt9fECK9oIUPXwYFYVV0e2ICJCi20SbFAuyG5uiECUlkKIQmOPng3y30d0d7Lt1bm4w301jQAOgcNoIDad1yOEEAFm9fSv/VqtJAAAAAElFTkSuQmCC"/>
    </div>
    <div>
      <span class="googft-legend-range">150 to 403</span>
      <img class="googft-dot-icon" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJCAYAAADgkQYQAAAAiklEQVR42mNgQIAoIF4NxGegdCCSHAMzEC81M4v6n56++n9V1RkwbWgY+B8oPhOmKM3WNu3/zJn/MbCFRSxIYSxI0YHi4gNYFRUW7gUp2gtS9LC9/SFWRc3Nt0GKbhNtUizIbmyKjIxCQIpCYI6fD/JdVtZGsO8yMtbBfDeNAQ2AwmkjNJzWIYcTAMk+i9OhipcQAAAAAElFTkSuQmCC"/>
    </div>
    <div class="googft-legend-source">
      <a href="https://www.google.com/fusiontables/data?docid=1_WLUFMZkCPz2jZJiZHUS7moFCAxUE0cIHLpKI_gX#rows:id=1" target="_blank">Data source</a>
    </div>
	</div>
	<input id="googft-legend-close" style="display:none" type="button" value="Hide"></input>

<div style="margin-top: 10px;">
	<label class="layer-wizard-search-label">
        Show by Zip Code
        <input type="text" id="search-string_0">
        <input type="button" onclick="changeMap_0()" value="Search">
	</label> 
</div>


<!--iframe width="100%" height="520" scrolling="no" frameborder="no" src="https://www.google.com/fusiontables/embedviz?q=select+col14+from+1_WLUFMZkCPz2jZJiZHUS7moFCAxUE0cIHLpKI_gX&amp;viz=MAP&amp;h=false&amp;lat=40.691959794876894&amp;lng=-74.00954473876948&amp;t=1&amp;z=10&amp;l=col14&amp;y=5&amp;tmplt=7&amp;hml=TWO_COL_LAT_LNG"></iframe-->