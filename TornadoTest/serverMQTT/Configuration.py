import configparser
import ConfigConstants


class Configuration:

    def __init__(self, config_file_path):
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
