function snowleft(){
    var c2 = document.getElementById('c2');
    var cxt = c2.getContext('2d');
    var w = c2.width = 0.99*window.innerWidth;
    var h = c2.height = 0.99*window.innerHeight;
    window.onresize = function(){
    	var w = c2.width = 0.99*window.innerWidth
    	var h = c2.height = 0.99*window.innerHeight
    }
    var sum = 800;
    var p = [];
    for (var i=0;i<sum;i++){
    	var q = Math.random()*0.18*w;
    	var e = w-Math.random()*0.18*w;
		p.push({x:q,y:Math.random()*h,r:Math.random()*3,});
		p.push({x:e,y:Math.random()*h,r:Math.random()*3,});
    }
	function changey(){
		for (var i=0;i<sum;i++){
		p[i].y += Math.random()*5
		if (p[i].y > h){
			p[i].y = 0
		}
		}
	}
    function draw(){
    	cxt.beginPath();
    	cxt.fillStyle = '#FFF';
    	for (var i=0;i<sum;i++){
    		cxt.moveTo(p[i].x,p[i].y)
			cxt.arc(p[i].x,p[i].y,p[i].r,0,2*Math.PI,false);
		}
		cxt.fill();
		changey()
	}
	draw()
	setInterval(function(){
		cxt.clearRect(0,0,w,h);
		draw()
	},50)
}

