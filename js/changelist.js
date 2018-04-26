function changelist(){
    var $l1 = $('#p3 ul .l1');
    var $l2 = $('#p3 ul .l2');
    $l1.click(function(){
        var lindex = 0.5*$(this).index();
        $l2.eq(lindex).stop().animate({height:'75.5%'},1200).siblings('.l2').animate({height:'0'},1);
    })
}