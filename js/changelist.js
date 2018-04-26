function changelist(){
    var $l1 = $('#p3 ul .l1');
    var $l2 = $('#p3 ul .l2');
    $l1.click(function(){
        var lindex = 0.5*$(this).index();
        if($l2.eq(lindex).height() != 0){$l2.eq(lindex).stop().animate({height:'0'},1200);}
        else{$l2.eq(lindex).stop().animate({height:'75.5%'},1200).siblings('.l2').animate({height:'0'},1189);}
    })
}