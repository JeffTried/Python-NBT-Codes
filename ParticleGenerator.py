from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()
while True:
    particleID = input('ENTER PARTICLE ID >')
    try:
        int(particleID)
        break
    except:
        print ('INVALID PARTICLE ID. PARTICLE ID MUST BE AN INTEGER.')
radius = input('ENTER RADIUS (IN METERS\\BLOCKS) (DAFAULT:3) >')
try:
    int(radius)
except:
    print ('INVALID RADIUS. SETTING TO DEFAULT OF 3')
    radius = '3'
radius = radius + 'f'
particleColor = input('ENTER PARTICLE COLOR (DEFAULT:65520) >')
try:
    int(particleColor)
except:
    print ('INVALID PARTICLE COLOR. SETTING TO DEFAULT OF 65520')
    particleColor = '65520'
duration = input('ENTER DURATION (IN TICKS [20TICKS = 1SECOND]) (DEFAULT:600 TICKS [30SECONDS]) >')
try:
    int(duration)
except:
    print ('INVALID DURATION. SETTING TO DEFAULT OF 600')
    duration = '600'
name = 'Custom Particle Generator'
lore = '"'+particleID+':'+particleColor+':'+duration+'"'
nbt = '{Items:[{Count:1b,Damage:5s,Name:"minecraft:bucket",Slot:2b,tag:{EntityType:95,Duration:'+duration+',DurationOnUse:'+duration+',InitialRadius:'+radius+'f,Invulnerable:1b,ParticleColor:'+particleColor+',ParticleId:'+particleID+',Pos:[6.5f,4.5f,8.5f],PotionId:11s,Radius:'+radius+'f,Persistant:1b,RadiusChangeOnPickup:0f,RadiusOnUse:0f,RadiusPerTick:0f,ReapplicationDelay:40,Rotation:[19.8044f,0f],Variant:0,definitions:["+minecraft:area_effect_cloud"],mobEffects:[],display:{Lore:['+lore+'],Name:"Custom Particle Generator"}}}],display:{Lore:['+lore+'],Name:"'+name+'"}}'
print ('USE [.nbt write] ON A STORAGE BLOCK (CHEST, SHULKER, FURNACE, DISPENSER\\DROPPER) AND TAKE PUFFERFISH BUCKET OUT AND PLACE BUCKET DOWN TO USE')
print (nbt)
askCopyClip(nbt)
