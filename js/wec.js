function wec(){
	var $wec = $('#main #header ul li #wec');
	var $wecp= $('#wechat');
	$wec.click(function(){
		$wecp.fadeIn(1000);
	})
}

function wecp(){
	var $wec = $('#main #header ul li #wec');
	var $wecp= $('#wechat');
	$wecp.click(function(){
		$wecp.fadeOut(500);
	})
}