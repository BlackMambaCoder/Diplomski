package com.example.root.mqtttest.Runnables;

import android.util.Log;

import com.example.root.mqtttest.MainActivity;

import java.text.DateFormat;
import java.util.Date;

import de.tavendo.autobahn.WebSocketConnection;
import de.tavendo.autobahn.WebSocketException;
import de.tavendo.autobahn.WebSocketHandler;

public class ConnectSocket implements Runnable {
    public static boolean work = false;
    @Override
    public void run()
    {
//        int counter = 0;
//
//        while(work) {
//            Log.w("LEO--Thread", "Counter: " + String.valueOf(counter++));
//            try {
//                Thread.sleep(1500);
//            } catch (InterruptedException e) {
//                e.printStackTrace();
//                Log.e("LEO--Thread", "Error: " + e.getMessage());
//                break;
//            }
//        }
        final String serverAddr = "ws://" + MainActivity.SERVER_IP + ":" + MainActivity.SERVER_PORT;
        Log.w("TCP Client", "C: Connecting...");

        final WebSocketConnection webSocketConnection = new WebSocketConnection();

        try {
            webSocketConnection.connect(serverAddr, new WebSocketHandler() {
                @Override
                public void onOpen() {
                    Log.d("WEBSocket", "Status: Connected to " + serverAddr);
                    webSocketConnection.sendTextMessage("Hello, world!");
                }

                @Override
                public void onTextMessage(String payload) {
                    Log.d("WEBSocket", "Server message: " + payload);
                    String content = MainActivity.etServerMessage.getText().toString();
                    content += "\n";
                    content += new Date().getTime() + ": " + payload;
                    MainActivity.etServerMessage.setText(content);

                }
            });
        } catch (WebSocketException e) {
            e.printStackTrace();
            Log.e("LEO--Thread", "Error: " + e.getMessage());
        }
    }
}