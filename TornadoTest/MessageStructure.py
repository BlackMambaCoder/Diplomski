import json
import Constants

#   __time gives number of seconds from epoche
class MessageStructure():

    # Constructor
    def __init__(self,
                 source_arg,
                 sensor_arg,
                 value_arg,
                 time_arg,
                 message_arg):
        self.__source = source_arg
        self.__sensor = sensor_arg
        self.__value = value_arg
        self.__time = time_arg
        self.__message = message_arg

    # GETTERS & SETTERS
    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, input_arg):
        self.__source = input_arg

    @property
    def sensor(self):
        return self.__sensor
    @sensor.setter
    def sensor(self, input_arg):
        self.__sensor = input_arg

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, input_arg):
        self.__value = input_arg

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, input_arg):
        self.__time = input_arg

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, input_arg):
        self.__message = input_arg

    # Gets json from MessageStructure object (self)
    def to_json(self):
        entire_data = dict()

        entire_data[Constants.SOURCE_ATTR] \
            = str(self.__source)
        entire_data[Constants.SENSOR_ATTR] \
            = str(self.__sensor)
        entire_data[Constants.VALUE_ATTR] \
            = str(self.__value)
        entire_data[Constants.TIME_ATTR] \
            = str(self.__time)
        entire_data[Constants.MESSAGE_ATTR] \
            = self.__message

        return json.dumps(entire_data)

    # Creates MessageStructure object from
    # JSON data
    def from_json(self, data_arg):
        json_data = json.loads(data_arg)

        self.__source = json_data[Constants.SOURCE_ATTR]
        self.__sensor = json_data[Constants.SENSOR_ATTR]
        self.__value = json_data[Constants.VALUE_ATTR]
        self.__time = json_data[Constants.TIME_ATTR]
        self.__message = json_data[Constants.MESSAGE_ATTR]
