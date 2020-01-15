import mcpi.minecraft as minecraft
friendsIP = "45.33.105.164"
friendsPort = 25565
hackedMC = minecraft.Minecraft.create(friendsIP, friendsPort)
hackedMC.postToChat("Hello World")
