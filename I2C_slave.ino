#include <Wire.h>

#define I2C_SLAVE_ADRESS 11
int instruction  = 0;

void setup()
{
    Wire.begin(I2C_SLAVE_ADRESS);
    Serial.begin(57600);
    Serial.println(I2C_SLAVE_ADRESS);
    Serial.print(" is a slave");
}

void loop()
{
    Wire.onRequest(requestEvents);
    Wire.onReceive(receiveEvents);
    test();
}

int requestEvents()
{
    Serial.println("--< Request receive");
    Wire.write("Ok");
}

int receiveEvents()
{
    Serial.println("-->Instruction receive");
    instruction = Wire.read();
}

//Code ici

int test()
{
    if (instruction == 1)
    {
        Serial.println("DOOOOOOOOOOOONE");
    }
    else if (instruction == 0)
    {
        Serial.println("Fondamental state");
    }
    else
    {
        Serial.println("Instruction = ");
        Serial.print(instruction);
    }
    delay(500);
    
    
}