package com.example.root.mqtttest.Other;

import android.os.Binder;

import com.example.root.mqtttest.Services.TemperatureNotificationService;

/**
 * Created by leo on 26.9.16..
 */

public class LocalBinder extends Binder {
    public TemperatureNotificationService getService() {
        System.out.println("LocalBinderClass");
        return new TemperatureNotificationService();
    }
}
