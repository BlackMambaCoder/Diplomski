package com.example.root.mqtttest.Runnables;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.support.v4.app.NotificationCompat;
import android.support.v4.app.TaskStackBuilder;
import android.util.Log;

import com.example.root.mqtttest.Activities.AirConditionerActivity;
import com.example.root.mqtttest.MainActivity;
import com.example.root.mqtttest.Other.TemperatureData;
import com.example.root.mqtttest.R;
import com.example.root.mqtttest.Services.NotificationService;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.text.DateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import de.tavendo.autobahn.WebSocketConnection;
import de.tavendo.autobahn.WebSocketException;
import de.tavendo.autobahn.WebSocketHandler;

//import static com.example.root.mqtttest.Services.NotificationService.webSocketConnection;

public class ConnectSocket implements Runnable {
    private Context callerContext;
    private final String DEBUG_TAG = "ConnectSocket";

    public static String serverAddr = "ws://" + MainActivity.SERVER_IP + ":" + MainActivity.SERVER_PORT;
    public static WebSocketConnection webSocketConnection = null;
//    public static boolean work = false;

    public ConnectSocket(Context callerContextArg) {
        this.callerContext = callerContextArg;
    }
    @Override
    public void run()
    {
        if (webSocketConnection == null) {
            webSocketConnection = new WebSocketConnection();
        }
//        final String serverAddr = "ws://" + MainActivity.SERVER_IP + ":" + MainActivity.SERVER_PORT;
        Log.w("WEBSocket", "C: Connecting...");

        final WebSocketConnection webSocketConnection = new WebSocketConnection();

        try {
            webSocketConnection.connect(serverAddr, new WebSocketHandler() {
                private final String DEBUG_TAG = "WebSocket";
                @Override
                public void onOpen() {
                    Log.d(this.DEBUG_TAG, "Status: Connected to " + serverAddr);
                    webSocketConnection.sendTextMessage("Hello, world!");
                }

                @Override
                public void onTextMessage(String payload) {
                    Log.d(this.DEBUG_TAG, "Server message: " + payload);
                    String content = MainActivity.etServerMessage.getText().toString();
                    content += "\n";

                    List<TemperatureData> payLoadData;

                    try {
                        payLoadData = payloadToString(payload);
                    } catch (JSONException e) {
                        e.printStackTrace();
                        Log.e(this.DEBUG_TAG, "Error: " + e.getMessage());
                        content += "ERROR";
                        payLoadData = null;
                    }

                    if (payLoadData != null && payLoadData.size() > 0) {
                        createTemperatureNotification(
                                payLoadData.get(0).getTemperature().toString()
                        );

                        for (int iterator = 0; iterator < payLoadData.size(); iterator++) {
                            content += "Date: " + payLoadData.get(iterator)
                                    .getMeasureDate().toGMTString();

                            content += "\n";
                            content += "Temperature: " + payLoadData.get(iterator)
                                    .getTemperature().toString();

                            content += "\n\n";
                        }
                    }

                    MainActivity.etServerMessage.setText(content);

//                    webSocketConnection.sendTextMessage("Hello, send again");
                }

                @Override
                public void onClose(int code, String reason) {
                    Log.d(this.DEBUG_TAG, "Connection lost. Reason: "
                            + reason
                            + ". Code: "
                            + String.valueOf(code)
                    );
                }
            });

            Log.d(this.DEBUG_TAG, "Web socket succeeded");
        } catch (WebSocketException e) {
            e.printStackTrace();
            Log.e(this.DEBUG_TAG, "Error: " + e.getMessage());
        }
    }

    private List<TemperatureData> payloadToString (String payloadArg) throws JSONException {
        JSONArray payloadArray = new JSONArray(payloadArg);
        List<TemperatureData> payLoadList =
                new ArrayList<>();

        for (int iterator = 0; iterator < payloadArray.length(); iterator++) {
            JSONObject payLoadElement = payloadArray.getJSONObject(iterator);

            double dateFP = payLoadElement.getDouble("date");

            Date date = new Date((long)dateFP);
            Double temperature = payLoadElement.getDouble("temperature");

            TemperatureData data = new TemperatureData(
                    date,
                    temperature
            );

            payLoadList.add(data);
        }

        return payLoadList;
    }

    private void createTemperatureNotification(String contentTextArg) {
        NotificationCompat.Builder notificationBuilder =
                new NotificationCompat.Builder(this.callerContext)
                .setSmallIcon(
                        R.drawable.ic_stat_action_info_outline
                )
                .setContentTitle("Temperature")
                .setContentText("Temperature: " + contentTextArg);

        Intent resultIntent = new Intent(this.callerContext, AirConditionerActivity.class);

        TaskStackBuilder stackBuilder = TaskStackBuilder.create(this.callerContext);
        stackBuilder.addParentStack(AirConditionerActivity.class);
        stackBuilder.addNextIntent(resultIntent);

        PendingIntent resultPendingIntent =
                stackBuilder.getPendingIntent(
                        0,
                        PendingIntent.FLAG_UPDATE_CURRENT
                );

        notificationBuilder.setContentIntent(resultPendingIntent);
        NotificationManager notificationManager =
                (NotificationManager) this.callerContext.getSystemService(
                        Context.NOTIFICATION_SERVICE
                );
        notificationManager.notify(9999, notificationBuilder.build());
    }

    public static void sendMessage(String messageArg) {
        webSocketConnection.sendTextMessage(messageArg);
    }
}