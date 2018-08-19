package com.maptest.domain;

import java.io.Serializable;

public class testdata implements Serializable{
	
	private String lattitude;
	private String longitude;
	
	
	public String getLattitude() {
		return lattitude;
	}
	public void setLattitude(String lattitude) {
		this.lattitude = lattitude;
	}
	public String getLongitude() {
		return longitude;
	}
	public void setLongitude(String longitude) {
		this.longitude = longitude;
	}
	
	
}
