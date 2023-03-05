import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ACCURACY_DECIMALS,
    CONF_DEVICE_CLASS,
    CONF_ICON,
    CONF_ID,
    CONF_STATE_CLASS,
    CONF_TYPE,
    CONF_UNIT_OF_MEASUREMENT,
    DEVICE_CLASS_APPARENT_POWER,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    ICON_BATTERY,
    ICON_POWER,
    ICON_THERMOMETER,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_KILOWATT_HOURS,
    UNIT_MINUTE,
    UNIT_PERCENT,
    UNIT_VOLT,
    UNIT_VOLT_AMPS,
    UNIT_WATT,
)

from .. import CONF_VICTRON_BLE_ID, VictronBle, victron_ble_ns

DEPENDENCIES = ["victron_ble"]
CODEOWNERS = ["@Fabian-Schmidt"]

UNIT_AMPERE_HOURS = "Ah"

VictronSensor = victron_ble_ns.class_("VictronSensor", sensor.Sensor, cg.Component)

VICTRON_SENSOR_TYPE = victron_ble_ns.namespace("VICTRON_SENSOR_TYPE")

CONF_SUPPORTED_TYPE = {
    "ACTIVE_AC_IN": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.ACTIVE_AC_IN,
    },
    "ACTIVE_AC_IN_POWER": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.ACTIVE_AC_IN_POWER,
        CONF_UNIT_OF_MEASUREMENT: UNIT_WATT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_POWER,
    },
    "AC_APPARENT_POWER": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.AC_APPARENT_POWER,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT_AMPS,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_APPARENT_POWER,
    },
    "AC_CURRENT": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.AC_CURRENT,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 1,
        CONF_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    },
    "AC_OUT_POWER": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.AC_OUT_POWER,
        CONF_UNIT_OF_MEASUREMENT: UNIT_WATT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_POWER,
    },
    "AC_VOLTAGE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.AC_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "ALARM_REASON": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.ALARM_REASON,
    },
    "AUX_VOLTAGE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.AUX_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "BATTERY_CURRENT": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_CURRENT,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 3,  # between 1 and 3 depending on device.
        CONF_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    },
    "BATTERY_VOLTAGE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "BATTERY_POWER": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_POWER,
        CONF_UNIT_OF_MEASUREMENT: UNIT_WATT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_POWER,
    },
    "CHARGER_ERROR": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CHARGER_ERROR,
    },
    "CONSUMED_AH": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CONSUMED_AH,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE_HOURS,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 1,
        # device_class=???,
    },
    "DEVICE_STATE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.DEVICE_STATE,
    },
    "ERROR": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.ERROR,
    },
    "INPUT_VOLTAGE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.INPUT_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "LOAD_CURRENT": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.LOAD_CURRENT,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 1,
        CONF_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    },
    "MID_VOLTAGE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.MID_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "OFF_REASON": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.OFF_REASON,
    },
    "OUTPUT_VOLTAGE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.OUTPUT_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "PV_POWER": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.PV_POWER,
        CONF_UNIT_OF_MEASUREMENT: UNIT_WATT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_POWER,
    },
    "STATE_OF_CHARGE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.STATE_OF_CHARGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_PERCENT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 1,
        CONF_DEVICE_CLASS: DEVICE_CLASS_BATTERY,
    },
    "TEMPERATURE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.TEMPERATURE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_CELSIUS,
        CONF_ICON: ICON_THERMOMETER,
        CONF_ACCURACY_DECIMALS: 2,  # between 0 and 2 depending on device.
        CONF_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    },
    "TIME_TO_GO": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.TIME_TO_GO,
        CONF_UNIT_OF_MEASUREMENT: UNIT_MINUTE,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_DURATION,
    },
    "YIELD_TODAY": {
        CONF_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
        CONF_TYPE: VICTRON_SENSOR_TYPE.YIELD_TODAY,
        CONF_UNIT_OF_MEASUREMENT: UNIT_KILOWATT_HOURS,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    },
    # SMART_LITHIUM
    "BMS_FLAGS": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BMS_FLAGS,
    },
    "CELL1": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL1,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "CELL2": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL2,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "CELL3": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL3,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "CELL4": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL4,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "CELL5": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL5,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "CELL6": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL6,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "CELL7": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL7,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "CELL8": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.CELL8,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "BALANCER_STATUS": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BALANCER_STATUS,
    },
    # SMART_BATTERY_PROTECT
    "OUTPUT_STATE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.OUTPUT_STATE,
    },
    "WARNING_REASON": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.WARNING_REASON,
    },
    # LYNX_SMART_BMS
    "IO_STATUS": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.IO_STATUS,
    },
    "WARNINGS_ALARMS": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.WARNINGS_ALARMS,
    },
    # VE_BUS
    "ALARM": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.ALARM,
    },
    # DC_ENERGY_METER
    "BMV_MONITOR_MODE": {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BMV_MONITOR_MODE,
    },
}


def set_default_based_on_type():
    def set_defaults_(config):
        type = config[CONF_TYPE]
        # set defaults based on sensor type:
        if CONF_STATE_CLASS not in config:
            if CONF_STATE_CLASS in CONF_SUPPORTED_TYPE[type]:
                config[CONF_STATE_CLASS] = sensor.validate_state_class(
                    CONF_SUPPORTED_TYPE[type][CONF_STATE_CLASS]
                )
            else:
                config[CONF_STATE_CLASS] = sensor.validate_state_class(
                    STATE_CLASS_MEASUREMENT
                )

        if (
            CONF_UNIT_OF_MEASUREMENT not in config
            and CONF_UNIT_OF_MEASUREMENT in CONF_SUPPORTED_TYPE[type]
        ):
            config[CONF_UNIT_OF_MEASUREMENT] = CONF_SUPPORTED_TYPE[type][
                CONF_UNIT_OF_MEASUREMENT
            ]

        if CONF_ICON not in config and CONF_ICON in CONF_SUPPORTED_TYPE[type]:
            config[CONF_ICON] = CONF_SUPPORTED_TYPE[type][CONF_ICON]

        if (
            CONF_ACCURACY_DECIMALS not in config
            and CONF_ACCURACY_DECIMALS in CONF_SUPPORTED_TYPE[type]
        ):
            config[CONF_ACCURACY_DECIMALS] = CONF_SUPPORTED_TYPE[type][
                CONF_ACCURACY_DECIMALS
            ]

        if (
            CONF_DEVICE_CLASS not in config
            and CONF_DEVICE_CLASS in CONF_SUPPORTED_TYPE[type]
        ):
            config[CONF_DEVICE_CLASS] = CONF_SUPPORTED_TYPE[type][CONF_DEVICE_CLASS]

        return config

    return set_defaults_


CONFIG_SCHEMA = (
    sensor.sensor_schema()
    .extend(
        {
            cv.GenerateID(): cv.declare_id(VictronSensor),
            cv.GenerateID(CONF_VICTRON_BLE_ID): cv.use_id(VictronBle),
            cv.Required(CONF_TYPE): cv.enum(CONF_SUPPORTED_TYPE, upper=True),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)
FINAL_VALIDATE_SCHEMA = set_default_based_on_type()


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    await cg.register_parented(var, config[CONF_VICTRON_BLE_ID])

    cg.add(var.set_type(CONF_SUPPORTED_TYPE[config[CONF_TYPE]][CONF_TYPE]))
