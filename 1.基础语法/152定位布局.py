'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>position布局</title>
    <style>
        .box{
        background:blue;
        width:1000px;
        height:100px;
        }
        .bg{
        background:#000
        position:absolute;
        top:0;
        bottom:0;
        left:0;
        right:0;
        opacity:0.6
        }
        .win{
        width:500px;
        height:400px;
        background:white;
        position:absolution;
        top:0;
        bottom:0;
        left:0;
        right:0;
        margin:auto;
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="bg"></div>
        <div class="win">文本内容</div>
    </div>
    <div>
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
    </div>
</body>
</html>








'''