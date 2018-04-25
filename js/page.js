function drawDown() {
    var c1 = document.getElementById("c1");
    var cxt = c1.getContext("2d");
    cxt.beginPath();
    cxt.moveTo(5, 20);
    cxt.lineTo(25, 45);
    cxt.lineTo(45, 20);
    cxt.lineWidth = 5;
    cxt.strokeStyle = "gray";
    cxt.lineCap = 'round';
    cxt.lineJoin = "round";
    cxt.stroke();
    cxt.moveTo(5, 5);
    cxt.lineTo(25, 30);
    cxt.lineTo(45, 5);
    cxt.lineWidth = 5;
    cxt.strokeStyle = "gray";
    cxt.lineCap = 'round';
    cxt.lineJoin = "round";
    cxt.stroke();
}
