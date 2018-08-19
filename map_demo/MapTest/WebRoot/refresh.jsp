<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<!-- <script type="text/javascript">   
var t=10;   
function refresh()   
{   
t=t-1;  
document.getElementById("refresh").innerHTML="离下次刷新时间还有 "+t+" 秒";  
    if (t==0) {   
        document.location.reload();   
        t = 11 ;  
    }   
}   
</script>  --> 
</head>
<body>
    <!-- onload="window.setInterval(refresh,1000);" -->
	<form action="${pageContext.request.contextPath}/servlet/RefreshServlet" method="post">
		StartFlashTime:<input type="text" name="startFlashTime" size='30'/><br/>
		<!-- StartMicroSeconds:<input type="text" name="startMicroSeconds" /><br/> -->
		EndFlashTime:<input type="text" name="endFlashTime" size='30'/><br/>
		<!-- EndMicroSeconds:<input type="text" name="endMicroSeconds" /><br/> -->
	    Latitude:<input type="text" name="latitude" /><br/>
		Longitude:<input type="text" name="longitude" /><br/> 
		<!-- Strength:<input type="text" name="strength" /><br/> -->
		
	<input type="submit" value="确认"/><br/>
	</form>
	<!-- <font id="refresh" style="color:blue" >离下次刷新时间还有10秒</font><br/>  -->
</body>
</html>