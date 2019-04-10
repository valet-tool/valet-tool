#include "IN219a.h"


static float current_lsb = 0.000077;

void IN219A_reset(int i2c_bus_fd)
{
	uint8_t buffer [3] = {IN219A_CONFIG_REG,IN219A_RESET & 0x00FF, IN219A_RESET >> 8};
	i2c_write(buffer, i2c_bus_fd, 3 );
	usleep(500);	
}
float get_power_in_mW(int i2c_bus_fd)
{
	IN219A_calibration(i2c_bus_fd);
	return i2c_read_word(i2c_bus_fd, IN219A_POWER_REG) * current_lsb * 20 * 1000;
}

float get_current_in_mA(int i2c_bus_fd)
{
	IN219A_calibration(i2c_bus_fd);
	return i2c_read_word(i2c_bus_fd, IN219A_CURRENT_REG) * current_lsb * 1000;
}	

/*
 *The Power Register and Current Register default to '0' because the Calibration Register defaults to '0', yielding a zero current value until
 the Calibration Register is programmed.
 */

void IN219A_calibration(int i2c_bus_fd)
{	//Configured for 32V 2A
	uint8_t buffer[3] = { 0x00,0x00,0x00 }; 
	uint16_t config_reg = 0;
	config_reg = IN219A_CONFIG_REG_BVOLTAGERANGE_32V |
                    IN219A_CONFIG_REG_GAIN_8_320MV |
                    IN219A_CONFIG_REG_BADCRES_12BIT |
                    IN219A_CONFIG_REG_SADCRES_12BIT_1S_532US |
                    IN219A_CONFIG_REG_MODE_SANDBVOLT_CONTINUOUS;

	buffer[0] = IN219A_CONFIG_REG;
	buffer[2] = (uint8_t) (config_reg & 0x00FF);
	buffer[1] = (uint8_t) (config_reg >> 8);
	i2c_write(buffer, i2c_bus_fd, 3);
	usleep(600);
        buffer[0] = IN219A_CALIBRATION_REG;
	buffer[1] = 0x14;// Calculated from TI INA219 EVM software
	buffer[2] = 0xC7;// Calculated from TI INA219 EVM software
	
	i2c_write(buffer, i2c_bus_fd, 3);
	usleep(600);
}

uint16_t i2c_read_word(int i2c_bus_fd, uint8_t reg_addr)
{
	uint8_t data[2] = {0x00, 0x00};
	if (write(i2c_bus_fd,&reg_addr, 1) != 1)
	{
		printf("Failed to write to the i2c bus\r\n");
	}

	if (read(i2c_bus_fd, data, 2) != 2)
	{
		printf("Failed to read from the i2c bus.\r\n");
	}	
	return (data[0] << 8 | data[1]);//Hey TI. Why... ugh
}


uint8_t i2c_write(uint8_t* data, int i2c_bus_fd, uint8_t num_bytes)
{	
	if (write(i2c_bus_fd, data, num_bytes) != num_bytes ) // Num bytes written returned.
	{
		printf("Failed to write to the i2c bus.\r\n");
		return 1;
	}
	
	return 0;
}
