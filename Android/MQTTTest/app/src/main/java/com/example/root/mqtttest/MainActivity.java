package com.example.root.mqtttest;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Toast;
import android.widget.ToggleButton;

import com.example.root.mqtttest.Activities.RaspConfigActivity;
import com.example.root.mqtttest.Runnables.ConnectSocket;
//import com.example.root.mqtttest.Services.MqttService;
import com.example.root.mqtttest.Services.NotificationService;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;


public class MainActivity extends AppCompatActivity implements CompoundButton.OnCheckedChangeListener {
    private boolean mIsBound = false;

    public static String SERVER_IP = "";
    public static int SERVER_PORT = -1;

    private EditText etServerIpAddress;
    private EditText etServerPort;
    public static EditText etServerMessage;

    public static String temperatureString = "";

    private boolean notificationServiceRuns = false;

    ToggleButton tglBtnConnection;

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
        etServerMessage = (EditText)findViewById(R.id.et_id_server_messages);

        this.tglBtnConnection = (ToggleButton) findViewById(R.id.btn_id_connect);
        this.tglBtnConnection.setOnCheckedChangeListener(this);
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

            if (!this.checkFields())
            {
                this.tglBtnConnection.setChecked(false);
                Toast.makeText(this, "Fill fields correctly", Toast.LENGTH_SHORT).show();
                return;
            }

            Log.w("LEO--ConnectBtn", "Connect");

            SERVER_IP =
                    this.etServerIpAddress.getText().toString();
            SERVER_PORT =
                    Integer.parseInt(this.etServerPort.getText().toString());

            startService(new Intent(this, NotificationService.class));
            this.notificationServiceRuns = true;
//            startService(new Intent(this, MqttService.class));
        }
        else
        {
            Log.w("LEO--ConnectBtn", "Disconnect");

            stopService(new Intent(this, NotificationService.class));
            this.notificationServiceRuns = false;
//            stopService(new Intent(this, MqttService.class));
        }
    }

    @Override
    public void onBackPressed()
    {
        if (this.notificationServiceRuns)
        {
            stopService(new Intent(this, NotificationService.class));
        }

        super.onBackPressed();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_main_acitivty, menu);

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        Intent intent;

        switch (item.getItemId()) {
            case R.id.raspberry_config:
                // rasp config
                intent = new Intent(this, RaspConfigActivity.class);
                startActivity(intent);
                break;

            case R.id.arduino_config:
                // arduino config
                break;

            case R.id.raspberry_data:
                // rasp data
                break;

            case R.id.arduino_data:
                // arduino data
                break;

            default:
                return super.onOptionsItemSelected(item);
        }

        return super.onOptionsItemSelected(item);
    }

    private boolean checkFields ()
    {
        return !this.etServerIpAddress.getText().toString().equals("")
                && !this.etServerPort.getText().toString().equals("");
    }
}
