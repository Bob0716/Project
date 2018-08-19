package com.maptest.web.servlet;

import java.io.Console;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.beanutils.BeanUtils;

import com.maptest.domain.testdata;
import com.maptest.service.testdataService;
import com.maptest.service.impl.testdataServiceImpl;

public class ConfirmServlet extends HttpServlet {

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
		System.out.print(request);
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
//		获取表单数据
		testdata data=new testdata();
			try {
				BeanUtils.populate(data, request.getParameterMap());
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} 
//		调用业务逻辑
			testdataService ts = new testdataServiceImpl();
			
			testdata d;
			try {
				d = ts.confirm(data);
			
				//分发转向
				if(d!=null){//如果取得，就把data对象放到session对象 中
					request.getSession().setAttribute("d",data );
				/*	request.getSession().setAttribute("e","hello" );*/
					request.getRequestDispatcher("/map.jsp").forward(request, response);
					
				}else{
					
					request.getRequestDispatcher("/confirm.jsp").forward(request, response);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		
	}
}
