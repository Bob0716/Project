package com.maptest.dao.impl;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;

import com.maptest.dao.refreshDao;
import com.maptest.domain.refresh;

import com.maptest.utils.jdbc;

public class refreshDaoImpl implements refreshDao {

	
	public List<refresh> getrefresh(refresh time) throws Exception {
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		refresh t = null;
		List<refresh> list=new ArrayList<refresh>();
		try {
			conn = jdbc.getConnection();
			//ps = conn.prepareStatement("select FlashTime,MicroSeconds,Longitude,Latitude,Strength from flash where FlashTime between ? and ? and abs(Latitude-?)<0.2 and abs(Longitude-?)<0.2;");
			ps = conn.prepareStatement("select FlashTime,MicroSeconds,Longitude,Latitude,Strength from flash where FlashTime between ? and ? ;");
			
			ps.setString(1,time.getStartFlashTime());
			ps.setString(2,time.getEndFlashTime());
			//ps.setString(3, time.getLatitude());
			//ps.setString(4, time.getLongitude());
//			ps.setString(7, time.getLattitude2());
//			ps.setString(8, time.getLongitude2());
		
			rs = ps.executeQuery();
			
			while(rs.next()){
				t = new refresh();
				/*SimpleDateFormat sdf=new SimpleDateFormat();
				String date=sdf.format();*/
				t.setFlashTime("\"" + rs.getTimestamp(1) + "\"");
				/*t.setFlashTime(rs.getString(1));*/
				t.setMicroSeconds(rs.getInt(2));
				t.setLongitude(rs.getString(3));
				t.setLatitude(rs.getString(4));
				t.setStrength(rs.getString(5));
//				System.out.print(t);
				list.add(t);
			}
			
		} catch (Exception e){
			e.printStackTrace();
		}finally{
			jdbc.closeAll(rs, ps, conn);
		}
		return list;
	}

}
