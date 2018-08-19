package com.maptest.web.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.beanutils.BeanUtils;
import org.apache.commons.beanutils.ConvertUtils;
import org.apache.commons.beanutils.Converter;
import org.apache.commons.beanutils.locale.converters.DateLocaleConverter;

import com.maptest.domain.refresh;
import com.maptest.service.refreshService;
import com.maptest.service.impl.refreshServiceImpl;
import com.sun.org.apache.xerces.internal.impl.xpath.regex.ParseException;


import java.text.SimpleDateFormat;

public class RefreshServlet extends HttpServlet {

	/**
		 * The doGet method of the servlet. <br>
		 *
		 * This method is called when a form has its tag value method equals to get.
		 * 
		 * @param request the request send by the client to the server
		 * @param response the response send by the server to the client
		 * @throws ServletException if an error occurred
		 * @throws IOException if an error occurred
		 */
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		
	}

	/**
		 * The doPost method of the servlet. <br>
		 *
		 * This method is called when a form has its tag value method equals to post.
		 * 
		 * @param request the request send by the client to the server
		 * @param response the response send by the server to the client
		 * @throws ServletException if an error occurred
		 * @throws IOException if an error occurred
		 */
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

//		System.out.print(request);
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
//		获取表单数据
		refresh time=new refresh();
		try {
			/*ConvertUtils.register(new Converter(){
				public Object convertf(Class type,Object value){
					Date date1=null;
					if(value instanceof String){
						String date=(String)value;	
						SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd");
						try{
							date1=sdf.parse(value);
						}catch(ParseException e){
							e.printStackTrace();
						}	
				       }
					return date1;
				}
				}
			},Date.class);*/
			ConvertUtils.register(new DateLocaleConverter(),Date.class);//时间转换器
			BeanUtils.populate(time, request.getParameterMap());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
//		System.out.print(time.getNyr());
		
//		调用业务逻辑
		refreshService ts=new refreshServiceImpl();
		ArrayList<refresh> t = null;
		try {
//			根据表单time获取查询对象 结果
			t = ts.showrefresh(time);
			//分发转向
			if(t!=null){//如果取得，就把t对象放到session对象 中
				request.getSession().setAttribute("t",t);
				/*request.getRequestDispatcher("/testrefresh.jsp").forward(request, response);*/
			   /* SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
			    String s = sdf.format(sdf.parse("2017-07-01 00:00:02.000"));
				request.setAttribute("t",s);
				request.getRequestDispatcher("/index.jsp").forward(request, response);*/
				request.getRequestDispatcher("/HL.jsp").forward(request, response);				
			}else{
				request.getRequestDispatcher("/refresh.jsp").forward(request, response);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}       
//        String nyr=request.getParameter("nyr");
////        System.out.print(lattitude);
//        String longitude=request.getParameter("longitude");
////        System.out.print(longitude);
//        request.setAttribute("value1", lattitude);
//        request.setAttribute("value2", longitude);
	}

}
