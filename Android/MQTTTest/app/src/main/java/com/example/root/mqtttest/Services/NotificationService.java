package com.example.root.mqtttest.Services;

import android.app.Service;
import android.content.Intent;
import android.os.Handler;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.util.Log;
import android.widget.Toast;

import com.example.root.mqtttest.MainActivity;
import com.example.root.mqtttest.Runnables.ConnectSocket;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * Created by leo on 26.9.16..
 */

public class NotificationService extends Service {

    private int counter = 0;

    private ExecutorService threadPoolExecutor = Executors.newSingleThreadExecutor();
    private Future connectFuture;
    Runnable connectSocket = new ConnectSocket();

    @Override
    public void onCreate() {
        Log.w("LEO--Service", "Service::onCreate");
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId)
    {
        Log.w("LEO--Service", "Service::onStartCommand");
        ConnectSocket.work = true;
        this.connectFuture = this.threadPoolExecutor.submit(connectSocket);

        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public void onDestroy()
    {
        Log.w("LEO--Service", "Service::onDestroy");
        ConnectSocket.work = false;
        this.connectFuture.cancel(true);
//        new Handler().removeCallbacks(connectSocket);
        super.onDestroy();
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
