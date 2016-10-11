package com.example.root.mqtttest.StaticAttributes;

/**
 * Created by leo on 3.10.16..
 */

public class ServerStaticAttributes {
    public static int _readTimeOut = 10000;
    public static int _connectTimeOut = 15000;
    public static String _requestMethod = "POST";

    public static int USER_NAME_ERROR = 125;
    public static int PASSWORD_ERROR = 126;

    public static String _SERVER_ROOT_URL = "http://192.168.1.5:8820";

    public static String URL_RASP_CONFIG = "/rasp_config";
    public static String URL_RASP_GET_CONFIG = "/rasp_get_config";
    public static String URL_RASP_GET_ROOM_TEMP = "/room_temp";
}
