import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.creat()
friendsIP = "24.16.163.30"
hackedMC = minecraft.Minecraft.create(friendsIP)
hackedMC.postToChat("Hello World")
