function changelist(){
    var $l1 = $('#p3 ul .l1');
    var $l2 = $('#p3 ul .l2');
    $l1.click(function(){
        var lindex = $(this).index();
        $l1.eq(lindex).css('border','3px groove rgba(0,0,0,0.35)').siblings('.l1').css('border','1px solid rgba(0,0,0,0.15)');
        $l1.eq(lindex).css('background-color','rgba(0,0,0,0.35)').siblings('.l1').css('background-color','rgba(0,0,0,0.15)');
        $l1.eq(lindex).css('border-right-width','0px').siblings('.l1').css('border-right','1px solid rgba(0,0,0,0.15)');
        $l2.eq(lindex).fadeIn(500).siblings('.l2').fadeOut(500);
    })
}