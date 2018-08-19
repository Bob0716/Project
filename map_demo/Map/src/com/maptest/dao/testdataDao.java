package com.maptest.dao;

import com.maptest.domain.testdata;

public interface testdataDao {
	
	public void addtestdata(testdata data) throws Exception;
	
	public testdata findtestdata(testdata data)throws Exception;

}
