//package com.example.root.mqtttest.Services;
//
//import android.app.Service;
//import android.content.Intent;
//import android.os.Handler;
//import android.os.IBinder;
//import android.os.Message;
//import android.support.annotation.Nullable;
//import android.util.Log;
//import android.widget.Toast;
//
//import com.example.root.mqtttest.Other.LocalBinder;
//
//import java.io.BufferedReader;
//import java.io.BufferedWriter;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.io.OutputStreamWriter;
//import java.io.PrintWriter;
//import java.net.InetAddress;
//import java.net.Socket;
//import java.net.UnknownHostException;
//
///**
// * Created by leo on 26.9.16..
// */
//
//public class TemperatureNotificationService extends Service {
//    public static String SERVER_IP = "";
//    public static int SERVER_PORT = -1;
//    PrintWriter out;
//    Socket socket;
//    InetAddress serverAddr;
//
//    private String clientMessage = null;
//    private static Handler handler = new Handler() {
//        @Override
//        public void handleMessage(Message msg) {
//            super.handleMessage(msg);
//        }
//    };
//
//    private final IBinder myBinder = new LocalBinder();
////    TCPClient mTcpClient = new TCPClient();
//
//    @Nullable
//    @Override
//    public IBinder onBind(Intent intent) {
//        Log.w("TCP", "TemperatureNotificationService::onBind");
//        return this.myBinder;
//    }
//
//    @Override
//    public void onCreate() {
//        super.onCreate();
//        Log.w("TCP", "TemperatureNotificationService::onCreate");
//    }
//
//    public void IsBoundable () {
//        Toast.makeText(this, "Boundable", Toast.LENGTH_SHORT).show();
//    }
//
//    public void sendMessage(String message) {
//        if (this.out != null && !this.out.checkError()) {
//            Log.w("TCP", "Send message: " + message);
//            this.out.println(message);
//            this.out.flush();
//        }
//    }
//
//    @Override
//    public int onStartCommand(Intent intent, int flags, int startId) {
//        super.onStartCommand(intent, flags, startId);
//        Log.w("TCP", "TemperatureNotificationService::onStartCommand");
//        Runnable connect = new connectSocket();
//        new Thread(connect).start();
//        return START_STICKY;
//    }
//
//    class connectSocket implements Runnable {
//        String serverMessage = null;
//        @Override
//        public void run() {
//            try {
//                serverAddr = InetAddress.getByName(SERVER_IP);
//                Log.w("TCP Client", "C: Connecting...");
//
//                socket = new Socket(serverAddr, SERVER_PORT);
//
//                try {
//                    out = new PrintWriter(
//                            new BufferedWriter(new OutputStreamWriter(
//                                    socket.getOutputStream()
//                            )), true
//                    );
//
//                    Log.w("TCP Client", "C: Sent.");
//                    Log.w("TCP Client", "C: Done.");
//                } catch (IOException e) {
//                    e.printStackTrace();
//                    Log.e("TCP", "IOException: Error", e);
//                }
//
//                while (!Thread.currentThread().isInterrupted()) {
////                    Message message = new Message();
//                    {
////                        BufferedReader input = null;
//                        InputStreamReader inputStreamReader = new InputStreamReader(
//                                socket.getInputStream()
//                        );
//
//                        BufferedReader reader = new BufferedReader(inputStreamReader);
//                        serverMessage = reader.readLine();
//                        clientMessage = serverMessage;
//                        Toast.makeText(TemperatureNotificationService.this, serverMessage, Toast.LENGTH_SHORT).show();
////                        handler.sendMessage(message);
//                    }
//                }
//            } catch (UnknownHostException e) {
//                e.printStackTrace();
//                Log.e("TCP", "UnknownHostException: Error", e);
//            } catch (IOException e) {
//                e.printStackTrace();
//                Log.e("TCP", "IOException: Error", e);
//            }
//        }
//    }
//
//    @Override
//    public void onDestroy() {
//        super.onDestroy();
//        try {
//            socket.close();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        socket = null;
//    }
//}
