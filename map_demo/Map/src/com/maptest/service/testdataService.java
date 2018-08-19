package com.maptest.service;

import com.maptest.domain.testdata;

public interface testdataService {
	public void deliver(testdata data) throws Exception;
	
	public testdata confirm(testdata data)throws Exception;

}
