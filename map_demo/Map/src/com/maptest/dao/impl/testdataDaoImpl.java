package com.maptest.dao.impl;

import com.maptest.dao.testdataDao;
import com.maptest.domain.testdata;
import com.maptest.utils.jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;



public class testdataDaoImpl implements testdataDao {

	public void addtestdata(testdata data) throws Exception {
		Connection conn = null;
		PreparedStatement ps = null;
		
		try {
			conn = jdbc.getConnection();
			ps = conn.prepareStatement("INSERT INTO testdata(lattitude,longitude) VALUES(?,?)");
			ps.setString(1,data.getLattitude() );
			ps.setString(2,data.getLongitude() );
		
			
			int i = ps.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("添加失败！");
		}finally{
			jdbc.closeAll(null, ps, conn);
		}
	}
	public testdata findtestdata(testdata data) throws Exception {
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		testdata u = null;
		try {
			conn = jdbc.getConnection();
			ps = conn.prepareStatement("select * from testdata  where lattitude=? and longitude=?");
//			ps = conn.prepareStatement("select * from testdata  where nyr=? and sfm=?");
			ps.setString(1,data.getLattitude());
			ps.setString(2,data.getLongitude());
			
			rs = ps.executeQuery();
			if(rs.next()){
				u = new testdata();
				u.setLattitude(rs.getString(1));
				u.setLongitude(rs.getString(2));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally{
			jdbc.closeAll(rs, ps, conn);
		}
		return u;
	}

}
