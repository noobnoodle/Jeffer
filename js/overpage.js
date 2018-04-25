function overpage(){
	var $c1 = $('#c1');
	var $p1 = $('#p1');
	var $p2 = $('#p2');
	$c1.click(function(){
		$p1.fadeOut(1000);
		$p2.fadeIn(1000);
		snow();
	})
}