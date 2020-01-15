import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
friendsIP = "45.33.105.164"
friendsPort = 25565
hackedMC = minecraft.Minecraft.create(friendsIP)
hackedMC.postToChat("Hello World")
