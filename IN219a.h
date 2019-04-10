#include <unistd.h>			
#include <fcntl.h>			
#include <sys/ioctl.h>			
#include <linux/i2c-dev.h>		
#include <stdint.h> 
#include <stdio.h>
#include <unistd.h>
/* 
 *  I2c Hardware address and corresponding registers 
 *    
 */
#define IN219A_I2C_ADDRESS		0x40
#define IN219A_CURRENT_REG		0x04
#define IN219A_CONFIG_REG 		0x00
#define IN219A_CALIBRATION_REG		0x05	
#define IN219A_BUS_VOLTAGE_REG		0x02
#define IN219A_POWER_REG		0x03
#define IN219A_SHUNT_VOLTAGE_REG	0x01
#define IN219A_RESET			0x0080
#define	IN219A_CONFIG_REG_BVOLTAGERANGE_32V 			0x2000
#define IN219A_CONFIG_REG_GAIN_8_320MV 				0x1800
#define IN219A_CONFIG_REG_BADCRES_12BIT 			0x0180
#define IN219A_CONFIG_REG_SADCRES_12BIT_1S_532US 		0x0018
#define IN219A_CONFIG_REG_MODE_SANDBVOLT_CONTINUOUS		0x0007
#define BUS_MILLIVOLTS_LSB					0x04  //4mV

void IN219A_calibration(int i2c_bus_fd);
uint16_t i2c_read_word(int i2c_bus_fd, uint8_t reg_addr);
void IN219A_reset(int i2c_bus_fd);
uint8_t i2c_write(uint8_t* data, int i2c_bus_fd, uint8_t num_bytes);
float get_current_in_mA(int i2c_bus_fd);
float get_power_in_mW(int i2c_bus_fd);

