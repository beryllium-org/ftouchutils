rename_process("rmftouch")
be.api.setvar("return", "1")
vr("opts", be.api.xarg())
if not ("h" in vr("opts")["o"] or "help" in vr("opts")["o"]):
    if len(vr("opts")["w"]):
        vr("devt", vr("opts")["w"][0])
        if vr("devt").startswith("/dev/ftouch"):
            be.based.run("rmnod " + vr("devt")[5:])
            be.api.setvar("return", "0")
        else:
            term.write("Error: Invalid device!")
    else:
        term.write("Error: No device node specified!")
else:
    term.write("Usage:\n    rmftouch /dev/ftouchX\n")
    be.api.setvar("return", "0")
