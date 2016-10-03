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
        final String serverAddr = "ws://" + MainActivity.SERVER_IP + ":" + MainActivity.SERVER_PORT;
        Log.w("WEBSocket", "C: Connecting...");

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

                    webSocketConnection.sendTextMessage("Hello, send again");
                }

                @Override
                public void onClose(int code, String reason) {
                    Log.d("WEBSocket", "Connection lost. Reason: "
                            + reason
                            + ". Code: "
                            + String.valueOf(code)
                    );
                }
            });

            Log.d("WEBSocket", "Web socket succeeded");
        } catch (WebSocketException e) {
            e.printStackTrace();
            Log.e("WebSocket", "Error: " + e.getMessage());
        }
    }
}