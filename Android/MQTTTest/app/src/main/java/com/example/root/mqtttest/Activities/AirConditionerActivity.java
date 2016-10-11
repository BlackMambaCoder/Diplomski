package com.example.root.mqtttest.Activities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.example.root.mqtttest.R;
import com.example.root.mqtttest.Runnables.ConnectSocket;

public class AirConditionerActivity extends AppCompatActivity implements View.OnClickListener {

    private Button airConditionerControll;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_air_conditioner);

        this.airConditionerControll = (Button)findViewById(R.id.btnDeActivateAirConditioner);
        this.airConditionerControll.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btnDeActivateAirConditioner:
                this.controllAirConditioner();
                break;
        }
    }

    private void controllAirConditioner() {
        ConnectSocket.sendMessage("Turn air conditioner on");
    }
}
