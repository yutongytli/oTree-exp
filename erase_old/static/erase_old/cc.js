'use strict';

// From https://gist.github.com/jonathantneal/3748027
!window.addEventListener && (function (WindowPrototype, DocumentPrototype, ElementPrototype, addEventListener, removeEventListener, dispatchEvent, registry) {
	WindowPrototype[addEventListener] = DocumentPrototype[addEventListener] = ElementPrototype[addEventListener] = function (type, listener) {
		var target = this;
		registry.unshift([target, type, listener, function (event) {
			event.currentTarget = target;
			event.preventDefault = function () { event.returnValue = false };
			event.stopPropagation = function () { event.cancelBubble = true };
			event.target = event.srcElement || target;

			listener.call(target, event);
		}]);
		this.attachEvent("on" + type, registry[0][3]);
	};
	WindowPrototype[removeEventListener] = DocumentPrototype[removeEventListener] = ElementPrototype[removeEventListener] = function (type, listener) {
		for (var index = 0, register; register = registry[index]; ++index) {
			if (register[0] == this && register[1] == type && register[2] == listener) {
				return this.detachEvent("on" + type, registry.splice(index, 1)[0][3]);
			}
		}
	};
	WindowPrototype[dispatchEvent] = DocumentPrototype[dispatchEvent] = ElementPrototype[dispatchEvent] = function (eventObject) {
		return this.fireEvent("on" + eventObject.type, eventObject);
	};
})(Window.prototype, HTMLDocument.prototype, Element.prototype, "addEventListener", "removeEventListener", "dispatchEvent", []);

// from http://davidwalsh.name/javascript-debounce-function
function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};

// index page code
var scrawlWebsite = (function(){

	var exports = {};

	// navigation variables
	var navItemsDisplayed = false,
		navButton = document.querySelector('#nav_burger'),
		navContainer = document.querySelector('#nav_container'),
		navBarDisplayed = true,
		scrollPosition = 0,
		newScroll,
		navControls = document.querySelector('#nav_controls'),
		navItems = document.querySelector('#nav_items'),
		socialButtons;

	// panel variables
	var panels = document.querySelectorAll('.panels'),
		doc = document.documentElement,
		body = document.body,
		getBrowserWidth,
		getMaxPanelHeight,
		setPanelHeights,
		maxPanelHeight,
		mediumBreakpoint = 1024,
		largeBreakpoint = 1600,
		columns, oldColumns,
		i, iz, j, jz,
		resizeTime,
		resizeChoke = 16;

	// feature detection testing
	var temp, test,
		testFeatures,
		loadScrawl,
		startTour,
		checkStartTour,
		loadCount = 2,
		scrawlScript, scrawlCore;

	//display or hide the navigation items (mobile view)
	navButton.addEventListener('mouseup', function updateNavigationOnClick(){
		navContainer.className = (navItemsDisplayed) ? '' : 'show';
		navItemsDisplayed = !navItemsDisplayed;
	}, false);

	//display or hide the navigation bar
	document.addEventListener('scroll', function updatePageOnScroll(e){
		var temp;
		if(!socialButtons){
			socialButtons = document.querySelector('#sthoverbuttons');
		}
		newScroll = window.scrollY;
		if(newScroll > scrollPosition && navBarDisplayed && !navItemsDisplayed){
			navControls.className = '';
			navItems.className = '';
			if(socialButtons) {
				socialButtons.className += ' hide-social';
			}
			navBarDisplayed = false;
		}
		else if(newScroll < scrollPosition && !navBarDisplayed){
			navControls.className = 'show';
			navItems.className = 'show';
			if(socialButtons) {
				temp = socialButtons.className;
				temp = temp.replace(' hide-social', '');
				socialButtons.className = temp;
			}
			navBarDisplayed = true;
		}
		scrollPosition = newScroll;
	}, false);

	// feature checking; dynamically add scrawl library
	startTour = function(){
		scrawl.loadExtensions({
			// minified: false,
			// path: 'source/',
			minified: true,
			path: 'min/',
			extensions: ['stacks', 'phrase', 'images', 'block', 'path', 'factories', 'animation', 'filters', 'shape', 'frame', 'wheel', 'physics', 'collisions'],
			callback: function() {
				scrawl.init();
				scrawlTour.run();
			}
		});
	};
	checkStartTour = function(){
		loadCount--;
		if(!loadCount){
			scrawlCore.removeEventListener('load', checkStartTour, false);
			scrawlScript.removeEventListener('load', checkStartTour, false);
			startTour();
		}
	};
	loadScrawl = function(){
		scrawlCore = document.createElement('script');
		scrawlCore.async = 'async';
		scrawlCore.addEventListener('load', checkStartTour, false);
		// scrawlCore.src = 'source/scrawlCore.js';
		scrawlCore.src = 'min/scrawlCore-min.js';
		body.appendChild(scrawlCore);
		scrawlScript = document.createElement('script');
		scrawlScript.async = 'async';
		scrawlScript.addEventListener('load', checkStartTour, false);
		// scrawlScript.src = 'js/scrawlTour.js';
		scrawlScript.src = 'js/scrawlTour-min.js';
		body.appendChild(scrawlScript);
	};
	testFeatures = function(){
		temp = document.createElement('canvas'),
		test = temp.getContext('2d');
		if(typeof test !== 'undefined') {
			loadScrawl();
		};
	};

	// equal height panel functionality
	getBrowserWidth = function(){
		var w = window.innerWidth || doc.clientWidth || body.clientWidth;
		oldColumns = columns;
		if(w >= largeBreakpoint){
			columns = 3;
		}
		else if(w >= mediumBreakpoint){
			columns = 2;
		}
		else{
			columns = 1;
		}
		return w;
	};
	getMaxPanelHeight = function(el){
		var h = el.offsetHeight;
		if(h > maxPanelHeight){
			maxPanelHeight = h;
		}
		return h;
	};
	setPanelHeights = function(){
		getBrowserWidth();
		if(columns > 1){
			for(i = 0, iz = panels.length; i < iz; i += columns){
				for(j = i, jz = i + columns; j < jz; j++){
					panels[j].style.height = 'auto';
				}
				maxPanelHeight = 0;
				for(j = i, jz = i + columns; j < jz; j++){
					getMaxPanelHeight(panels[j]);
				}
				maxPanelHeight += 'px';
				for(j = i, jz = i + columns; j < jz; j++){
					panels[j].style.height = maxPanelHeight;
				}
			}
		}
		else{
			if(columns !== oldColumns){
				for(i = 0, iz = panels.length; i < iz; i++){
					panels[i].style.height = 'auto';
				}
			}
		}
		if(window.scrawlTour){
			scrawlTour.updateStacks();
			scrawlTour.updatePads();
		}
		resizeTime = Date.now() + resizeChoke;
	};
	window.addEventListener('load', function setPanelHeightsOnLoad(){
		setPanelHeights();
		testFeatures();
		window.removeEventListener('load', setPanelHeightsOnLoad, false);
	}, false);
	// seems to work better than a 'debounce' function, as long as the choke is fairly small
	// I can live with the resize jank - too much is going on anyway to worry about it
	// ... given that every canvas is forced to recalculate all entity positioning when canvas is resized
	// ... or is it???
	window.addEventListener('resize', function setPanelHeightsOnResize(){
		if(Date.now() > resizeTime){
			setPanelHeights();
		}
	}, false);

	exports.panels = panels;
	exports.setPanelHeights = setPanelHeights;
	return exports;
})();