rename_process("mkftouch")
be.api.setvar("return", "1")
vr("opts", be.api.xarg())
if not ("h" in vr("opts")["o"] or "help" in vr("opts")["o"]):
    vr("i2c", 0)
    if "i2c" in vr("opts")["o"]:
        vr("i2ct", vr("opts")["o"]["i2c"])
        if vr("i2ct") is not None and vr("i2ct").startswith("/dev/i2c"):
            try:
                vr("i2c", int(vr("i2ct")[8:]))
            except:
                term.write("Error: Invalid I2C bus!")
        else:
            term.write("Error: Invalid I2C bus!")
    try:
        vr("i2c", be.devices["i2c"][vr("i2c")])
        if not vr("i2c").try_lock():
            raise RuntimeError("I2C bus in use")
        vr("i2c").unlock()
        be.based.run("mknod ftouch")
        vr("node", be.api.getvar("return"))
        be.api.subscript("/bin/stringproccessing/devid.py")
        try:
            from adafruit_focaltouch import Adafruit_FocalTouch
            be.devices["ftouch"][vr("dev_id")] = Adafruit_FocalTouch(vr("i2c"))
            del Adafruit_FocalTouch
            be.api.setvar("return", "0")
            dmtex("ftouch device registered at /dev/ftouch" + str(vr("dev_id")))
        except:
            term.write("Could not init display!")
    except:
        term.write("Error: Invalid I2C bus!")
else:
    term.write("Usage:\n    mkftouch --i2c /dev/i2cX\n")
    be.api.setvar("return", "0")
