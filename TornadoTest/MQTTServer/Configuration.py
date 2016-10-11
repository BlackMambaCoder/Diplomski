import configparser
import ConfigConstants


class Configuration:

    def __init__(self, config_file_path):
        self.config_path = config_file_path

        # self.config_write = open(config_file_path, "a")

        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_file_path)

    def read_temp_level(self):
        return float(self.cfg.get(ConfigConstants.TEMPERATURE, ConfigConstants.LEVEL))

    def read_temp_measure(self):
        return str(self.cfg.get(ConfigConstants.TEMPERATURE, ConfigConstants.MEASURE))

    def read_update_period_interval(self):
        return float(self.cfg.get(ConfigConstants.UPDATE_PERIOD, ConfigConstants.INTERVAL))

    def read_update_period_measure(self):
        return str(self.cfg.get(ConfigConstants.UPDATE_PERIOD, ConfigConstants.MEASURE))

    def read_mqtt_publisher_ip_address(self):
        return str(self.cfg.get(ConfigConstants.MQTT_HOME_ROOM_TEMPERATURE_PUBLISHER, ConfigConstants.IP_ADDRESS))

    def read_mqtt_subscriber_ip_address(self):
        return str(self.cfg.get(ConfigConstants.MQTT_HOME_ROOM_TEMPERATURE_SUBSCRIBER, ConfigConstants.IP_ADDRESS))

    def read_server_port(self):
        return int(self.cfg.get(ConfigConstants.SERVER, ConfigConstants.PORT))

    def read_bottle_server_port(self):
        return int(self.cfg.get(ConfigConstants.SERVER, ConfigConstants.BOTTLE_SERVER_PORT))

    def read_bottle_server_ip_address(self):
        return str(self.cfg[ConfigConstants.SERVER][ConfigConstants.IP_ADDRESS])
        # return str(self.cfg.get(ConfigConstants.SERVER, ConfigConstants.IP_ADDRESS))

    def read_broker_server_ip_address(self):
        return str(self.cfg.get(ConfigConstants.BROKER_SERVER, ConfigConstants.IP_ADDRESS))

    def read_broker_port(self):
        return int(self.cfg.get(ConfigConstants.BROKER_SERVER, ConfigConstants.PORT))

    # def read_topic_unread_flag(self):
    #     return str(
    #         self.cfg
    #         [ConfigConstants.HOME_ROOM_TEMPERATURE]
    #         [ConfigConstants.UNREAD]
    #     )
    #
    # def read_topic_value(self):
    #     return str(
    #         self.cfg
    #         [ConfigConstants.HOME_ROOM_TEMPERATURE]
    #         [ConfigConstants.VALUE]
    #     )

    def write_period_interval(self, arg):
        self.cfg.set(ConfigConstants.UPDATE_PERIOD, ConfigConstants.INTERVAL, arg)
        with open(self.config_path, "w") as configfile:
            self.cfg.write(configfile)

    def write_temp_level(self, arg):
        self.cfg.set(ConfigConstants.TEMPERATURE, ConfigConstants.LEVEL, arg)
        with open(self.config_path, "w") as configfile:
            self.cfg.write(configfile)
