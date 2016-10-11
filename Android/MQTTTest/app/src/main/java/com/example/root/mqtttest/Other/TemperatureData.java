package com.example.root.mqtttest.Other;

import java.util.Date;

/**
 * Created by leo on 5.10.16..
 */

public class TemperatureData {
    private Date measureDate;
    private Double temperature;

    public TemperatureData(Date dateArg, Double tempArg) {
        this.measureDate = dateArg;
        this.temperature = tempArg;
    }

    public Date getMeasureDate() {
        return this.measureDate;
    }

    public Double getTemperature() {
        return this.temperature;
    }

    public void setMeasureDate(Date dateArg) {
        this.measureDate = dateArg;
    }

    public void setMeasureDate(long millisecondsArg) {
        this.measureDate = new Date(millisecondsArg);
    }

    public void setTemperature(Double temperatureArg) {
        this.temperature = temperatureArg;
    }
}
