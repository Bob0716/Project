package com.maptest.service.impl;

import com.maptest.dao.testdataDao;
import com.maptest.dao.impl.testdataDaoImpl;
import com.maptest.domain.testdata;
import com.maptest.service.testdataService;

public class testdataServiceImpl implements testdataService {

	testdataDao dataDao=new testdataDaoImpl();
	public void deliver(testdata data) throws Exception {
		dataDao.addtestdata(data);

	}
	
	public testdata confirm(testdata data) throws Exception {
		// TODO Auto-generated method stub
		testdata d=null;
		d=dataDao.findtestdata(data);
		return d;
	}

}
