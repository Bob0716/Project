package com.maptest.domain;

import java.io.Serializable;
import java.util.Date;
import java.sql.Timestamp;



public class refresh implements Serializable{
	
	private String startFlashTime;
	private String endFlashTime;
	private String flashTime;
	private int microSeconds;
	private String strength;

	private String latitude;
	private String longitude;
	
	
	
	
	public int getMicroSeconds() {
		return microSeconds;
	}
	public void setMicroSeconds(int microSeconds) {
		this.microSeconds = microSeconds;
	}

	
	public String getLatitude() {
		return latitude;
	}
	public void setLatitude(String latitude) {
		this.latitude = latitude;
	}
	public String getLongitude() {
		return longitude;
	}
	public void setLongitude(String longitude) {
		this.longitude = longitude;
	}
	public String getStrength() {
		return strength;
	}
	public void setStrength(String strength) {
		this.strength = strength;
	}
	public String getStartFlashTime() {
		return startFlashTime;
	}
	public void setStartFlashTime(String startFlashTime) {
		this.startFlashTime = startFlashTime;
	}
	public String getEndFlashTime() {
		return endFlashTime;
	}
	public void setEndFlashTime(String endFlashTime) {
		this.endFlashTime = endFlashTime;
	}
	public String getFlashTime() {
		return flashTime;
	}
	public void setFlashTime(String flashTime) {
		this.flashTime = flashTime;
	}
    
	
	
	
	
	
	
	

	
	
}
