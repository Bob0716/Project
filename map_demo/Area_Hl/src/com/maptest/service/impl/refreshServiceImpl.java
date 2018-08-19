package com.maptest.service.impl;

import java.util.ArrayList;
import java.util.List;

import com.maptest.dao.refreshDao;
import com.maptest.dao.impl.refreshDaoImpl;
import com.maptest.domain.refresh;

import com.maptest.service.refreshService;

public class refreshServiceImpl implements refreshService {

	refreshDao freshDao=new refreshDaoImpl();
	public List<refresh> showrefresh(refresh time) throws Exception {
		List<refresh> t=null;
		t=freshDao.getrefresh(time);
		return t;
		
	}

}
