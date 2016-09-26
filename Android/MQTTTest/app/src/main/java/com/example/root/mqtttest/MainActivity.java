package com.example.root.mqtttest;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Toast;
import android.widget.ToggleButton;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import de.tavendo.autobahn.WebSocketConnection;
import de.tavendo.autobahn.WebSocketException;
import de.tavendo.autobahn.WebSocketHandler;


public class MainActivity extends AppCompatActivity implements CompoundButton.OnCheckedChangeListener {
    private boolean mIsBound = false;
//    private TemperatureNotificationService mBoundService;

    private String SERVER_IP = "";
    private int SERVER_PORT = -1;

    private EditText etServerIpAddress;
    private EditText etServerPort;

    private ExecutorService threadPoolExecutor = Executors.newSingleThreadExecutor();
    private Future connectFuture;



//    private ServiceConnection mConnection = new ServiceConnection() {
//        @Override
//        public void onServiceConnected(ComponentName name, IBinder service) {
//            mBoundService = ((LocalBinder)service).getService();
//        }
//
//        @Override
//        public void onServiceDisconnected(ComponentName name) {
//            mBoundService = null;
//        }
//    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.etServerIpAddress = (EditText)findViewById(R.id.et_id_server_ip_address);
        this.etServerPort = (EditText)findViewById(R.id.et_id_port);

        ToggleButton tglBtnConnection = (ToggleButton) findViewById(R.id.btn_id_connect);
        tglBtnConnection.setOnCheckedChangeListener(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
//        this.doUnbindService();
    }

//    private void doBindService() {
//        bindService(new Intent(
//                MainActivity.this,
//                TemperatureNotificationService.class
//        ), mConnection, Context.BIND_AUTO_CREATE);
//        mIsBound = true;
//
//        if (mBoundService != null) {
//            mBoundService.IsBoundable();
//        }
//    }
//
//    private void doUnbindService() {
//        if (mIsBound) {
//            unbindService(mConnection);
//            mIsBound = false;
//        }
//    }

    @Override
    public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
        if (isChecked) {

            Toast.makeText(this, "Connected", Toast.LENGTH_SHORT).show();

            Log.w("TCP", "Connected");

            this.SERVER_IP =
                    this.etServerIpAddress.getText().toString();
            this.SERVER_PORT =
                    Integer.parseInt(this.etServerPort.getText().toString());

//            startService(new Intent(MainActivity.this, TemperatureNotificationService.class));
//            this.doBindService();

            Runnable connect = new connectSocket();
            connectFuture = this.threadPoolExecutor.submit(connect);
        } else {
            Toast.makeText(this, "Disconnected", Toast.LENGTH_SHORT).show();

            Log.w("TCP", "Disconnected");

            connectFuture.cancel(true);
        }
    }

    private void checkFields () {}

    class connectSocket implements Runnable {
        @Override
        public void run() {
//            try {
//                InetAddress serverAddr = InetAddress.getByName(SERVER_IP);
                final String serverAddr = "ws://" + SERVER_IP + ":" + SERVER_PORT;
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
                        }
                    });
                } catch (WebSocketException e) {
                    e.printStackTrace();
                }


//                Socket socket = new Socket(serverAddr, SERVER_PORT);
//                PrintWriter out;
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
//                    out = null;
//                }
//
//                if (out != null && !out.checkError()) {
//                    Log.w("TCP", "Send message: " + "hello Server");
//                    out.println("hello Server");
//                    out.flush();
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
//                        Toast.makeText(MainActivity.this, serverMessage, Toast.LENGTH_SHORT).show();
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
        }
    }
}
