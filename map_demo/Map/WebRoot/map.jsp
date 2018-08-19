<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<body>
<div id="container"></div>
<!-- <div class="button-group">
    <input type="button" class="button" value="添加点标记覆盖物" id="addMarker"/>
    <input type="button" class="button" value="更新点标记覆盖物" id="updateMarker"/>
    <input type="button" class="button" value="删除点标记覆盖物" id="clearMarker"/>
    
</div>  -->
	<%-- <%=request.getSession().getAttribute("d")%> --%>
	<%-- <%String longitude= (String)request.getSession().getAttribute("d");%>  --%>
     
</body>
<head>
<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <title>点标记</title>
    <link rel="stylesheet" href="http://cache.amap.com/lbs/static/main1119.css"/>
    <script src="http://webapi.amap.com/maps?v=1.4.1&key=您申请的key值"></script>
    <script type="text/javascript" src="http://cache.amap.com/lbs/static/addToolbar.js"></script>
    <!--  <script type="text/javascript" src="http://a.amap.com/jsapi_demos/static/resource/heatmapData.js"></script> -->
    <%-- <%String longitude="34.043537";String lattitude="119.401459";%> --%>
    
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<script language="javascript" >
    <%-- var longitude="<%=longitude%>";  --%>
    var longitude=${d.longitude};
     /*  alert(longitude);  */
   <%--   var lattitude="<%=lattitude%>";  --%>
    var lattitude=${d.lattitude};
    /*  alert(lattitude);  */
    var map = new AMap.Map('container');
    map.setZoom(13);
    map.setCenter([119.40,34.04]);
    
   /*  AMap.event.addDomListener(document.getElementById('addMarker'), 'click', function() {
        addMarker();
    }, false); */
      // 实例化点标记
 	var marker = new AMap.Marker("container",{
            icon: "http://webapi.amap.com/theme/v1.3/markers/n/mark_b.png",
            position: [longitude, lattitude]
        });
         marker.setMap(map);
        /* marker.setContent(markerContent);  *///更新点标记内容
        /* marker.setPosition([longitude, lattitude]);  *///更新点标记位置
        
    /* if (!isSupportCanvas()) {
        alert('热力图仅对支持canvas的浏览器适用,您所使用的浏览器不能使用热力图功能,请换个浏览器试试~')
    } */
    //详细的参数,可以查看heatmap.js的文档 http://www.patrick-wied.at/static/heatmapjs/docs.html
    //参数说明如下:
    /* visible 热力图是否显示,默认为true
     * opacity 热力图的透明度,分别对应heatmap.js的minOpacity和maxOpacity
     * radius 势力图的每个点的半径大小   
     * gradient  {JSON} 热力图的渐变区间 . gradient如下所示
     *	{
     .2:'rgb(0, 255, 255)',
     .5:'rgb(0, 110, 255)',
     .8:'rgb(100, 0, 255)'
     }
     其中 key 表示插值的位置, 0-1 
     value 为颜色值 
     */
	<%-- var longitude="<%=longitude%>";
	alert(longitude);
	var lattitude="<%=lattitude%>";
	alert(lattitude); --%>
	
   /*  var heatmapData=[{
        "lng":34.043537,
        "lat":119.401459,
        "count":200
    }];  */
    
/*     var heatmap;
    map.plugin(["AMap.Heatmap"], function() {
        //初始化heatmap对象
        heatmap = new AMap.Heatmap(map, {
            radius: 25, //给定半径
            opacity: [0, 0.8]
            /*,gradient:{
             0.5: 'blue',
             0.65: 'rgb(117,211,248)',
             0.7: 'rgb(0, 255, 0)',
             0.9: '#ffea00',
             1.0: 'red'
             }
        });
      /*   //设置数据集：该数据为北京部分“公园”数据
        heatmap.setDataSet({
            data: heatmapData,
            max: 100
        });
    });
    //判断浏览区是否支持canvas
    function isSupportCanvas() {
        var elem = document.createElement('canvas');
        return !!(elem.getContext && elem.getContext('2d'));
    }  */
</script> 
<title>Insert title here</title>
</head>
<!-- <body>
<center>
<div id="container">
</div></center>
<script language="javascript">
var map = new AMap.Map('container');
map.setZoom(10);
map.setCenter([121.48,31.41]);
</script>
</body> -->
</html>