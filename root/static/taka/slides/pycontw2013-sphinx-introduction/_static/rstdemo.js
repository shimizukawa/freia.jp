//  sphinxcontrib.rstdemo
//  ~~~~~~~~~~~~~~~~~~~~~~
//
//  This package is a namespace package that contains all extensions
//  distributed in the ``sphinx-contrib`` distribution.
//
//  :copyright: Copyright 2007-2013 by the Sphinx team, see AUTHORS.
//  :license: BSD, see LICENSE for details.

$(function(){
	$('.rstdemo').each(function(i, elem){
		elem = $(elem);
		var hover = $('<span>').addClass('rstdemo-hover').text('rst');
		hover.click(function(evt){
			console.log(evt);
			elem.find('.highlight-rst').toggle();
			elem.find('.rstdemo-rendered').toggle();
			evt.stopPropagation();
			return false;
		});
		elem.append(hover);
	});
});
