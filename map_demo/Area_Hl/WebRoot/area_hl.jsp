<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%-- <%@ page isELIgnored="false"%> --%>
<html lang="zh-CN">

<head>
    <!-- 原始地址：//webapi.amap.com/ui/1.0/ui/misc/PointSimplifier/examples/index.html -->
    <base href="//webapi.amap.com/ui/1.0/ui/misc/PointSimplifier/examples/" />
    <base href="//webapi.amap.com/ui/1.0/ui/geo/DistrictCluster/examples/" />
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <!-- <script type="text/javascript" src="js/createPoints.js"></script> -->
    <title>区划聚合+海量点展示</title>
    <style>
    html,
    body,
    #container {
        width: 100%;
        height: 100%;
        margin: 0px;
    }
    
    #loadingTip {
        position: absolute;
        z-index: 9999;
        top: 0;
        left: 0;
        padding: 3px 10px;
        background: red;
        color: #fff;
        font-size: 14px;
    }
    </style>
</head>

<body>
    <div id="container"></div>
    <!--引入高德地图JSAPI -->
    <script type="text/javascript" src='//webapi.amap.com/maps?v=1.4.2&key=您申请的key值'></script> 
	<!--引入UI组件库（1.0版本） -->
    <script src="//webapi.amap.com/ui/1.0/main.js?v=1.0.11"></script>
    
    <script type="text/javascript">
    var arraydt = new Array();  
    var arrayms = new Array(); 
    var arraylg = new Array(); 
    var arrayla = new Array(); 
    var arrayst = new Array(); 
	<c:forEach items="${t}" var="d" >
	    arraydt.push(${d.flashTime})    
	    arrayms.push(${d.microSeconds}) 
	    arraylg.push(${d.longitude})
	    arrayla.push(${d.latitude})
	    arrayst.push(${d.strength})
	</c:forEach>  
	
    //创建地图
    var map = new AMap.Map('container', {
        zoom: 4
    });
    
    //$即为UI组件库最终使用的DomLibrary //调用$, PointSimplifier,继承可扩展该方法能力 http://lbs.amap.com/api/javascript-api/guide/amap-ui/advanced/
       function initPage(DistrictCluster, PointSimplifier, $) {  

    //创建组件实例
    var pointSimplifierIns = new PointSimplifier({
            map: map, //所属的地图实例
            autoSetFitView: false, //禁止自动更新地图视野
            zIndex: 110,
            getPosition: function(item) {
                if (!item) {
                    return null;
                }
                var parts = item.split(',');
                
                //返回经纬度
                return [parseFloat(parts[0]), parseFloat(parts[1])];
            },
            
            getHoverTitle: function(dataItem, idx) {
                return idx + ': ' + dataItem;
            },
            
            renderOptions: {
                //点的样式
                pointStyle: {
                    width: 6,
                    height: 6,
                    fillStyle:'rgba(153, 0, 153, 0.38)'
                },
                //鼠标hover时的title信息
                hoverTitleStyle: {
                    position: 'top'
                }
            }
        });
     
          var distCluster = new DistrictCluster({
            zIndex: 100,
            map: map, //所属的地图实例

            getPosition: function(item) {

                if (!item) {
                    return null;
                }

                var parts = item.split(',');

                //返回经纬度
                return [parseFloat(parts[0]), parseFloat(parts[1])];
            }
        });
          
        window.distCluster = distCluster;

        function refresh() {
            var zoom = map.getZoom();      
            //获取 pointStyle
            var pointStyle = pointSimplifierIns.getRenderOptions().pointStyle;
            //根据当前zoom调整点的尺寸
            pointStyle.width = pointStyle.height = 2 * Math.pow(1.2, map.getZoom() - 3);   
           }

        map.on('zoomend', function() {
            refresh();
        });

        refresh();
        
        
         function createPoints(arraylg,arrayla) {
		    var list = [];
		    for(var i = 0; i< arraylg.length; i++) {
		        list.push(arraylg[i]+','+arrayla[i]+','+arraydt[i]+','+arrayms[i]+','+arrayst[i]);
		    }
		    return list;
		}   
	
        
         var data = createPoints(arraylg,arrayla)  
       /* var data= ['120.412618,36.382612',
           '113.370643,22.938827',
           '113.890205,22.798043']  */  
         window.pointSimplifierIns = pointSimplifierIns;
          
          $('<div id="loadingTip">加载数据，请稍候...</div>').appendTo(document.body);
          distCluster.setData(data);
		  pointSimplifierIns.setData(data); 
          $('#loadingTip').remove();
     
      }
      
   
	     //加载相关组件
     AMapUI.load(['ui/geo/DistrictCluster', 'ui/misc/PointSimplifier', 'lib/$'], function(DistrictCluster, PointSimplifier, $) {

        //启动页面
        initPage(DistrictCluster, PointSimplifier, $);
    }); 
                    	  
    </script>
</body>

</html>