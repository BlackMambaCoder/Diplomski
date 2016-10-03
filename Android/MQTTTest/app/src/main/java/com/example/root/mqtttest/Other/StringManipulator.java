package com.example.root.mqtttest.Other;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * Created by leo on 3.10.16..
 */

public class StringManipulator {
    public static String inputStreamToString(InputStream inputStream)
    {
        String line = "";
        StringBuilder total = new StringBuilder();

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

        try {
            while ((line = bufferedReader.readLine()) != null)
            {
                total.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
            total = null;
        }

        return total != null ? total.toString() : null;
    }
}
