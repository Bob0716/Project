<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>

<html lang="zh-CN">

<head>
    <!-- 原始地址：//webapi.amap.com/ui/1.0/ui/misc/PointSimplifier/examples/index.html -->
    <base href="//webapi.amap.com/ui/1.0/ui/misc/PointSimplifier/examples/" />
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <!-- <script type="text/javascript" src="js/createPoints.js"></script> -->
    <title>海量点展示</title>
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
    
    /* var arraydt = new Array();  */ 
    var arrayms = new Array(); 
    var arraylg = new Array(); 
    var arrayla = new Array(); 
    var arrayst = new Array(); 
	<c:forEach items="${t}" var="d" >
	    /* arraydt.push(${d.flashTime}) */
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
    AMapUI.load(['ui/misc/PointSimplifier', 'lib/$'], function(PointSimplifier, $) {

        if (!PointSimplifier.supportCanvas) {
            alert('当前环境不支持 Canvas！');
            return;  
        }
   /*     initPage(PointSimplifier); */
    /* function initPage(PointSimplifier) { */
    //创建组件实例
    var pointSimplifierIns = new PointSimplifier({
            map: map, //所属的地图实例

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
                    height: 6
                },
                //鼠标hover时的title信息
                hoverTitleStyle: {
                    position: 'top'
                }
            }
        });
/* } */

        window.pointSimplifierIns = pointSimplifierIns;

        $('<div id="loadingTip">加载数据，请稍候...</div>').appendTo(document.body);
        
         var data = createPoints(arraylg,arrayla); 
       /* var data= ['120.412618,36.382612',
            '113.864691,22.942327',
           '113.370643,22.938827',
           '113.001181,23.120518',
           '112.985037,23.15046',
           '113.890205,22.798043']  */

            pointSimplifierIns.setData(data);

            $('#loadingTip').remove();
      /*   });
         */
      pointSimplifierIns.on('pointClick pointMouseover pointMouseout', function(e, record) {
            //console.log(e.type, record);
            });
            
      function createPoints(arraylg,arrayla) {
		    var list = [];
		    for(var i = 0; i< arraylg.length; i++) {
		        list.push(arraylg[i]+','+arrayla[i]+','+arrayms[i]+','+arrayst[i]);
		    }
		    return list;
		}   
		  
         });              	  
    </script>
</body>

</html>