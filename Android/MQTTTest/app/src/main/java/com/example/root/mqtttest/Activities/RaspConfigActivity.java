package com.example.root.mqtttest.Activities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.root.mqtttest.AsyncTasks.HttpRequestAsyncTask;
import com.example.root.mqtttest.R;
import com.example.root.mqtttest.StaticAttributes.ServerStaticAttributes;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

import static android.R.attr.id;

public class RaspConfigActivity extends AppCompatActivity implements View.OnClickListener {

    private EditText etRaspPeriodValue;
    private EditText etRaspTempTreshold;

    private Button btnRaspGetConfig;
    private Button btnRaspConfigSubmit;

    private String period;
    private String tempTreshold;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rasp_config);

        this.etRaspPeriodValue = (EditText)findViewById(R.id.etRaspPeriod);
        this.etRaspTempTreshold = (EditText)findViewById(R.id.etRaspTreshold);

        this.btnRaspGetConfig = (Button)findViewById(R.id.btnGetRaspConfigSettings);
        this.btnRaspGetConfig.setOnClickListener(this);
        this.btnRaspConfigSubmit = (Button)findViewById(R.id.btnRaspConfigSubmit);
        this.btnRaspConfigSubmit.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {
        String url;
        HttpRequestAsyncTask asyncTask = new HttpRequestAsyncTask();
        String responseData;

        switch (v.getId()) {
            case R.id.btnGetRaspConfigSettings:
                // getRequest for config data
                url = ServerStaticAttributes._SERVER_ROOT_URL +
                        ServerStaticAttributes.URL_RASP_GET_CONFIG;

                try {
                    asyncTask.execute(url, "").get();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                    Log.e("RaspGetConfig", "AsyncTask execute().get(): " + e.getMessage());
                    return;
                } catch (ExecutionException e) {
                    e.printStackTrace();
                    Log.e("RaspGetConfig", "AsyncTask execute().get(): " + e.getMessage());
                    return;
                }

                responseData = asyncTask.getResponseData();
                Toast.makeText(this, "GetConfigResponse: " + responseData, Toast.LENGTH_SHORT).show();

                break;

            case R.id.btnRaspConfigSubmit:
                // send new config data
                if (this.getEditTextData()) {
                    url = ServerStaticAttributes._SERVER_ROOT_URL +
                            ServerStaticAttributes.URL_RASP_CONFIG;
                    JSONObject jsonObject = new JSONObject();
                    try {
                        jsonObject.put("period", this.period);
                        jsonObject.put("threshold", this.tempTreshold);
                    }
                    catch (JSONException e) {
                        e.printStackTrace();
                        Log.e("RaspConfig", "Error in getting period and threshold");
                        return;
                    }

                    String postValue = jsonObject.toString();

                    try {
                        asyncTask.execute(url, postValue).get();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                        Log.e("RaspConfig", "AsyncTask execute().get(): " + e.getMessage());
                        return;
                    } catch (ExecutionException e) {
                        e.printStackTrace();
                        Log.e("RaspConfig", "AsyncTask execute().get(): " + e.getMessage());
                        return;
                    }

                    responseData = asyncTask.getResponseData();
                    Toast.makeText(this, "ConfigResponse: " + responseData, Toast.LENGTH_SHORT).show();
                }
                else {
                    Toast.makeText(this, "Fill text fields", Toast.LENGTH_SHORT).show();
                }
                break;

            default:

        }
    }

    private boolean getEditTextData() {
        return !(
                (this.period = this.etRaspPeriodValue.getText().toString()).equals("") ||
                (this.tempTreshold = this.etRaspTempTreshold.getText().toString()).equals("")
        );
    }
}
